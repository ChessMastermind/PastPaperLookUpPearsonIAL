import streamlit as st
import streamlit.components.v1 as components
import requests
from bs4 import BeautifulSoup
import os

# --- 1. CONFIGURATION ---
TARGET_URL = "https://chessmastermind.github.io/moon-papers/"
GOATCOUNTER_URL = "https://moon-papers.goatcounter.com/count"
TRACKING_PATH = "redirect_from_web1"

# Force Server-Side Dark Mode (Prevents white flash)
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

# --- 2. CSS LAYOUT FIXES ---
# We force the Streamlit iframe to be 100vw/100vh using a brute-force CSS selector.
st.markdown("""
    <style>
        /* Hide Streamlit UI */
        header, footer, [data-testid="stToolbar"] {display: none !important;}
        
        /* Force background black */
        .stApp, .block-container {
            background-color: #000000 !important;
            padding: 0 !important; margin: 0 !important;
            overflow: hidden !important;
        }

        /* BRUTE FORCE IFRAME SIZING */
        /* This targets the iframe created by components.html */
        iframe {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            z-index: 999999 !important;
            border: none !important;
            background: #000000;
        }
    </style>
""", unsafe_allow_html=True)

# --- 3. PROXY LOGIC ---
@st.cache_data(ttl=600)
def get_proxy_content(url):
    try:
        # A. Python fetches the raw HTML
        response = requests.get(url)
        response.raise_for_status()
        
        # B. Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # C. [CRITICAL FIX] INJECT <BASE> TAG
        # This fixes the "Flash": it forces all CSS/JS links to load from the real site.
        base_tag = soup.new_tag("base", href=url)
        if soup.head:
            soup.head.insert(0, base_tag)

        # D. [CRITICAL FIX] REMOVE INTEGRITY CHECKS
        # Often causes the "Black Screen". We strip 'integrity' attributes so 
        # the browser doesn't block the scripts.
        for tag in soup.find_all(attrs={"integrity": True}):
            del tag['integrity']

        # E. INJECT GOATCOUNTER (Safe Mode)
        gc_script = f"""
            window.goatcounter = {{
                endpoint: '{GOATCOUNTER_URL}',
                path: '{TRACKING_PATH}',
                no_onload: false
            }};
        """
        script_tag = soup.new_tag("script")
        script_tag.string = gc_script
        soup.head.append(script_tag)
        
        soup.head.append(soup.new_tag("script", attrs={"async": "", "src": "//gc.zgo.at/count.js"}))

        # F. [VISIBILITY ENFORCER]
        # This script runs last. It finds any "Loading" overlays or hidden body tags
        # and forces them to be visible.
        forcer = soup.new_tag("script")
        forcer.string = """
            document.addEventListener("DOMContentLoaded", function() {
                // 1. Force Body Visible
                document.body.style.display = 'block';
                document.body.style.opacity = '1';
                document.body.style.visibility = 'visible';
                
                // 2. Kill potential loading overlays
                // (If your site uses a div id="loader" or class="loading", this helps)
                var overlays = document.querySelectorAll('[id*="load"], [class*="load"]');
                overlays.forEach(el => {
                    // Only hide if it covers the whole screen
                    if(el.offsetWidth > 100 && el.offsetHeight > 100) {
                        el.style.display = 'none';
                    }
                });
            });
        """
        soup.body.append(forcer)

        return str(soup)

    except Exception as e:
        return f"<h1 style='color:red'>Proxy Error: {e}</h1>"

# --- 4. RENDER ---
html_payload = get_proxy_content(TARGET_URL)

# We use scrolling=True to allow the *internal* site to scroll,
# but the iframe itself is locked to 100vh by the CSS above.
components.html(html_payload, height=1000, scrolling=True)
