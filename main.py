import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. THE "ANTI-FLASH" CONFIG ---
# This file MUST exist to tell the server "Send black background immediately".
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
runOnSave = false
    """)

# --- 2. PAGE SETUP ---
st.set_page_config(
    page_title="Moon Papers",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- 3. AGGRESSIVE CSS OVERRIDES ---
hide_streamlit_ui = """
    <style>
        /* 1. FORCE ROOT BLACK */
        :root, html, body, .stApp {
            background-color: #000000 !important;
            background: #000000 !important;
        }

        /* 2. HIDE LOADING SKELETONS */
        /* This hides the "Please wait..." text and skeletons if they try to appear */
        .stSkeleton {
            display: none !important;
        }

        /* 3. REMOVE ALL PADDING & MARGINS */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }

        /* 4. HIDE UI ELEMENTS */
        header, footer, .stDeployButton, [data-testid="stToolbar"] {
            display: none !important;
        }
        
        /* 5. FIX IFRAME CONTAINER */
        iframe[title="streamlit.components.v1.html.html_component"] {
            position: fixed !important;
            top: -1vh !important;    /* Slight negative offset for overscan */
            left: -1vw !important;   /* Slight negative offset for overscan */
            width: 102vw !important; /* Make it slightly bigger than screen */
            height: 102vh !important; /* Make it slightly bigger than screen */
            z-index: 999999 !important;
            border: none !important;
            background: #000000 !important; /* Ensure iframe itself is black */
        }
    </style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

# --- 4. THE OVERSCAN PAYLOAD ---
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
            background-color: #000000; /* Black immediately */
            overflow: hidden;
        }
        
        /* FADE IN EFFECT */
        /* We hide the iframe initially (opacity 0) and fade it in only when loaded.
           This prevents seeing a white box while the external site connects. */
        #content-frame {
            opacity: 0;
            transition: opacity 0.5s ease-in;
            background-color: #000000;
            border: none;
            display: block;
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
        var frame = document.getElementById("content-frame");

        function maximizeFrame() {
            // OVERSCAN LOGIC
            // We calculate 102% of the screen size to ensure edges are covered
            var w = window.innerWidth * 1.02;
            var h = window.innerHeight * 1.02;
            
            frame.style.width = w + "px";
            frame.style.height = h + "px";
            
            // Center the overscanned content (move it back up/left slightly)
            frame.style.marginTop = "-1vh";
            frame.style.marginLeft = "-1vw";
        }

        // FADE IN LOGIC
        // When the external site inside the iframe actually loads, we turn opacity to 1
        frame.onload = function() {
            frame.style.opacity = "1";
        };

        // Listeners
        window.addEventListener("load", maximizeFrame);
        window.addEventListener("resize", maximizeFrame);
        maximizeFrame();
    </script>
</body>
</html>
"""

components.html(html_content, height=1000, scrolling=False)
