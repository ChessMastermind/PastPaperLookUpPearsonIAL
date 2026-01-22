import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. WHITE FLASH KILLER (Server-Side Config) ---
# We create a config.toml file on the fly. This tells Streamlit to 
# render the initial skeleton in black, preventing the blinding white flash.
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

# --- 2. PAGE SETUP ---
st.set_page_config(
    page_title="Moon Papers",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- 3. NUCLEAR CSS RESET ---
# This fixes the "weird" desktop view by killing the centered layout 
# and removing all margins.
hide_streamlit_ui = """
    <style>
        /* Global Background Reset */
        html, body, [class*="ViewContainer"], [class*="stApp"] {
            background-color: #000000 !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important; /* Lock main scrollbar */
        }

        /* Hide Streamlit UI */
        header, footer, .stDeployButton, [data-testid="stToolbar"], [data-testid="stHeader"] {
            display: none !important;
        }
        
        /* Kill the "Centered" Layout on Desktop */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        section.main {
            width: 100vw !important;
            height: 100vh !important;
        }
        
        /* Force the Component Container to be Full Screen */
        iframe[title="streamlit.components.v1.html.html_component"] {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            z-index: 999999 !important;
            border: none !important;
        }
    </style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

# --- 4. THE JAVASCRIPT PAYLOAD ---
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body, html {
            margin: 0; padding: 0;
            width: 100%; height: 100%;
            background-color: #000000;
            overflow: hidden; /* Prevent parent scrollbars */
        }
        #content-frame {
            border: none;
            display: block;
            /* We set width/height via JS, but start with 100% */
            width: 100%;
            height: 100%;
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
        // JAVASCRIPT RESIZER
        // This ensures the iframe is exactly the size of the screen,
        // fixing the mobile address bar issues and desktop centering.
        function resizeFrame() {
            var frame = document.getElementById("content-frame");
            var w = window.innerWidth;
            var h = window.innerHeight;
            
            frame.style.width = w + "px";
            frame.style.height = h + "px";
        }

        // Run on load and whenever the screen resizes (rotation, etc)
        window.addEventListener("load", resizeFrame);
        window.addEventListener("resize", resizeFrame);
        // Force run immediately
        resizeFrame();
    </script>
</body>
</html>
"""

# We set height=1000 just to render the box, but the CSS 'fixed' position overrides it.
components.html(html_content, height=1000, scrolling=False)
