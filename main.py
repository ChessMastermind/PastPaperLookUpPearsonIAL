import streamlit as st
import streamlit.components.v1 as components
import requests
from bs4 import BeautifulSoup
import os

# --- 1. CONFIGURATION ---
TARGET_URL = "https://chessmastermind.github.io/moon-papers/"
GOATCOUNTER_URL = "https://moon-papers.goatcounter.com/count"
TRACKING_PATH = "redirect_from_web1"

# Force Dark Mode Server-Side
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

# --- 2. CSS RESET (The "Container" Fix) ---
# Even though we are proxying, we still need to hide Streamlit's UI 
# to make the iframe look like the native app.
st.markdown("""
    <style>
        header, footer, [data-testid="stToolbar"] {display: none !important;}
        .stApp {
            background-color: #000000 !important;
            overflow: hidden !important;
        }
        .block-container {
            padding: 0 !important; margin: 0 !important; max-width: 100% !important;
        }
        iframe[title="streamlit.components.v1.html.html_component"] {
            position: fixed !important;
            top: 0 !important; left: 0 !important;
            width: 100vw !important; height: 100vh !important;
            border: none !important; z-index: 99999;
        }
    </style>
""", unsafe_allow_html=True)

# --- 3. THE PROXY ENGINE ---
@st.cache_data(ttl=600)  # Cache for 10 mins to speed up reload
def fetch_and_process_content(url):
    try:
        # A. Fetch the raw HTML from GitHub
        response = requests.get(url)
        response.raise_for_status()
        
        # B. Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # C. INJECT <BASE> TAG (Critical for Proxy)
        # This tells the browser: "All relative links (css, images, js) 
        # should be loaded from GitHub, not this Streamlit app."
        base_tag = soup.new_tag("base", href=url)
        if soup.head:
            soup.head.insert(0, base_tag)

        # D. INJECT GOATCOUNTER (With Custom Path)
        # We define the settings *before* loading the script.
        gc_script_config = soup.new_tag("script")
        gc_script_config.string = f"""
            window.goatcounter = {{
                endpoint: '{GOATCOUNTER_URL}',
                path: '{TRACKING_PATH}',
                no_onload: false
            }};
        """
        gc_script_loader = soup.new_tag("script", attrs={"async": "", "src": "//gc.zgo.at/count.js"})
        
        if soup.head:
            soup.head.append(gc_script_config)
            soup.head.append(gc_script_loader)

        # E. INJECT RESIZER SCRIPT
        # This ensures the proxied content fits the iframe perfectly without scrollbars.
        resizer_style = soup.new_tag("style")
        resizer_style.string = "body { margin: 0; overflow-x: hidden; background-color: #000000; }"
        
        if soup.head:
            soup.head.append(resizer_style)

        return str(soup)

    except Exception as e:
        return f"<h1 style='color:white'>Error loading proxy: {e}</h1>"

# --- 4. RENDER ---
# Get the modified HTML
proxy_content = fetch_and_process_content(TARGET_URL)

# Serve it. 
# height=1000 is a placeholder; CSS forces it to 100vh.
components.html(proxy_content, height=1000, scrolling=True)
