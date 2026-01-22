import streamlit as st
import streamlit.components.v1 as components
import os

# --- STEP 0: FORCE DARK THEME CONFIGURATION ---
# We write a config.toml file on the fly to ensure Streamlit 
# boots up in dark mode (black) instead of light mode (white).
if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")

with open(".streamlit/config.toml", "w") as f:
    f.write("""
[theme]
base="dark"
backgroundColor="#000000"
secondaryBackgroundColor="#000000"
textColor="#FFFFFF"
font="sans serif"
[server]
headless = true
    """)

# --- STEP 1: PAGE SETUP ---
st.set_page_config(
    page_title="Moon Papers",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- STEP 2: NUCLEAR CSS RESET ---
# This targets every specific Streamlit container that might hold a white background
# and forces it to black with !important.
hide_streamlit_ui = """
    <style>
        /* 1. Global Reset for HTML/Body */
        html, body, [class*="ViewContainer"], [class*="stApp"] {
            background-color: #000000 !important;
            background: #000000 !important;
            color: #000000 !important; /* Hide text cursor artifacts */
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important; /* Kill scrollbars on desktop */
        }

        /* 2. Hide Interface Elements */
        header, footer, .stDeployButton, [data-testid="stToolbar"], [data-testid="stHeader"] {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
        }
        
        /* 3. Collapse the main container */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }

        /* 4. Desktop Specific Fixes */
        /* Sometimes the main container has a default width on desktop. We kill it. */
        section.main {
            background-color: #000000 !important;
            width: 100vw !important;
            height: 100vh !important;
        }
        
        /* 5. Force Iframe Component to be Full Screen */
        iframe[title="streamlit.components.v1.html.html_component"] {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            z-index: 999999 !important;
            border: none !important;
            background: #000000 !important;
        }
    </style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

# --- STEP 3: THE APP PAYLOAD ---
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Ensure the iframe environment is also black */
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            background-color: #000000 !important;
            overflow: hidden;
        }
        #content-frame {
            display: block;
            border: none;
            background-color: #000000;
        }
    </style>
    <script data-goatcounter="https://moon-papers.goatcounter.com/count"
            async src="//gc.zgo.at/count.js"></script>
</head>
<body>
    <iframe 
        id="content-frame"
        src="https://chessmastermind.github.io/moon-papers/"
        sandbox="allow-scripts allow-same-origin allow-forms allow-popups allow-modals"
        allowfullscreen
    ></iframe>

    <script>
        function resizeFrame() {
            var frame = document.getElementById("content-frame");
            // Capture the viewport dimensions
            var w = window.innerWidth;
            var h = window.innerHeight;
            
            // Force the iframe to match
            frame.style.width = w + "px";
            frame.style.height = h + "px";
        }

        // Trigger on load and resize
        window.addEventListener("load", resizeFrame);
        window.addEventListener("resize", resizeFrame);
        resizeFrame();
    </script>
</body>
</html>
"""

components.html(html_content, height=1000, scrolling=False)
