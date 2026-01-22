import streamlit as st
import streamlit.components.v1 as components
import requests
from bs4 import BeautifulSoup
import re
import os

# --- 1. CONFIGURATION ---
TARGET_URL = "https://chessmastermind.github.io/moon-papers"  # No trailing slash for cleaner joins
GOATCOUNTER_URL = "https://moon-papers.goatcounter.com/count"
TRACKING_PATH = "redirect_from_web1"

# --- 2. ANTI-FLASH CONFIG ---
# Force dark mode instantly to hide loading glitches
if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")
with open(".streamlit/config.toml", "w") as f:
    f.write("""
[theme]
base="dark"
backgroundColor="#000000"
secondaryBackgroundColor="#000000"
textColor="#FFFFFF"
[server]
headless = true
    """)

st.set_page_config(page_title="Moon Papers", layout="wide")

# --- 3. CSS "FULL TAKEOVER" ---
# This CSS hides Streamlit and prepares the viewport for the incoming site
st.markdown("""
    <style>
        /* Hide all Streamlit UI */
        header, footer, [data-testid="stToolbar"], .stDeployButton {display: none !important;}
        
        /* Reset containers to 0 padding/margin */
        .stApp, .block-container {
            background-color: #000000 !important;
            padding: 0 !important; margin: 0 !important;
            overflow: hidden !important;
        }

        /* Force the component to be fullscreen */
        iframe[title="streamlit.components.v1.html.html_component"] {
            position: fixed !important;
            top: 0 !important; left: 0 !important;
            width: 100vw !important; height: 100vh !important;
            border: none !important; z-index: 99999;
        }
    </style>
""", unsafe_allow_html=True)

# --- 4. THE ROBUST PROXY ENGINE ---
@st.cache_data(ttl=300) # Cache for 5 mins for speed
def get_rewritten_site(url):
    try:
        # A. Fetch Raw Content
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        
        # B. AGGRESSIVE LINK REWRITING (The Fix for "Black Screen")
        # We physically replace relative paths with absolute GitHub paths.
        # This fixes Webpack chunks, CSS files, and Images.
        
        # Regex patterns to find relative URLs (e.g. src="/_next/...")
        # We look for src=", href=", and content=" starting with /
        base_url = url
        
        # 1. Fix src="/..." -> src="https://base/..."
        html = re.sub(r'src="/([^"]*)"', f'src="{base_url}/\\1"', html)
        
        # 2. Fix href="/..." -> href="https://base/..."
        html = re.sub(r'href="/([^"]*)"', f'href="{base_url}/\\1"', html)
        
        # 3. Fix standard CSS url('/...') -> url('https://base/...')
        html = re.sub(r'url\(\'\/([^\']*)\'\)', f'url(\'{base_url}/\\1\')', html)
        
        # C. SOUP CLEANING
        soup = BeautifulSoup(html, 'html.parser')
        
        # 1. Remove Integrity Checks (Fixes "Flash" crashes)
        # Browsers block proxied scripts with integrity checks because the domain changed.
        for tag in soup.find_all(attrs={"integrity": True}):
            del tag['integrity']
            
        # 2. Inject Tracking (GoatCounter)
        # We inject it at the top of HEAD to ensure it captures the hit.
        gc_script = f"""
            window.goatcounter = {{
                endpoint: '{GOATCOUNTER_URL}',
                path: '{TRACKING_PATH}',
                no_onload: false
            }};
        """
        script_tag = soup.new_tag("script")
        script_tag.string = gc_script
        if soup.head:
            soup.head.insert(0, script_tag)
            soup.head.insert(1, soup.new_tag("script", attrs={"async": "", "src": "//gc.zgo.at/count.js"}))

        return str(soup)

    except Exception as e:
        return f"""
        <div style="color:white; padding:20px; font-family:sans-serif;">
            <h1>Proxy Error</h1>
            <p>Could not fetch content. Error details:</p>
            <pre>{e}</pre>
        </div>
        """

# --- 5. EXECUTION ---
# Get the "Safe" HTML
proxy_html = get_rewritten_site(TARGET_URL)

# Render it. 
# We use scrolling=True so the proxied site handles its own scrolling.
components.html(proxy_html, height=1000, scrolling=True)
