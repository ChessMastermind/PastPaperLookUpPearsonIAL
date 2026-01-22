import streamlit as st
import streamlit.components.v1 as components

# 1. Page Config: Wide mode is essential for full-width capability
st.set_page_config(
    page_title="Moon Papers",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Outer Shell CSS (Python Side)
# We must break the Streamlit Component container out of the document flow
# so it can access the full screen dimensions.
hide_streamlit_ui = """
    <style>
        /* Hide all Streamlit UI elements */
        header[data-testid="stHeader"],
        section[data-testid="stSidebar"],
        .stDeployButton,
        [data-testid="stToolbar"],
        footer {
            display: none !important;
        }
        
        /* Remove padding from the main app container */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        .stApp {
            background-color: #000000 !important;
            overflow: hidden !important; /* Lock scrollbars on the python side */
        }

        /* CRITICAL: Force the Streamlit Component Iframe to cover the screen.
           This ensures the 'window' our JS measures is the actual browser window. */
        iframe[title="streamlit.components.v1.html.html_component"] {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            z-index: 99999 !important;
            border: none !important;
        }
    </style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

# 3. Inner Logic (HTML/JS Side)
# This script calculates the exact Width and Height in pixels and applies it.
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body, html {
            margin: 0;
            padding: 0;
            background-color: #000000;
            overflow: hidden; /* Prevent double scrollbars */
        }
        #content-frame {
            border: none;
            display: block;
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
        function maximizeFrame() {
            var frame = document.getElementById("content-frame");
            
            // 1. Get the exact available screen geometry
            var w = window.innerWidth;
            var h = window.innerHeight;
            
            // 2. Force the iframe to match these pixels exactly
            frame.style.width = w + "px";
            frame.style.height = h + "px";
        }

        // Run immediately on load
        maximizeFrame();

        // Run whenever the window is resized (e.g. rotating phone)
        window.addEventListener("resize", maximizeFrame);
        
        // Run continuously for the first second to catch any layout shifts
        setInterval(maximizeFrame, 100);
    </script>
</body>
</html>
"""

# Render the component
components.html(html_content, height=1000, scrolling=False)
