import streamlit as st
import streamlit.components.v1 as components

# 1. Configuration: Set wide layout and basic page metadata
st.set_page_config(
    page_title="Moon Papers",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Aggressive CSS Injection
# - Hides the Streamlit toolbar, footer, and hamburger menu.
# - Resets padding on the main block containers to 0.
# - Forces a black background to prevent white flash on load.
hide_streamlit_ui = """
    <style>
        /* Hide the header/toolbar/hamburger */
        header[data-testid="stHeader"] {display: none !important;}
        section[data-testid="stSidebar"] {display: none !important;}
        .stDeployButton {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        footer {display: none !important;}
        
        /* Remove all margins and padding from the main container */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            margin: 0 !important;
        }
        
        /* Force background to black for dark mode consistency */
        .stApp {
            background-color: #000000 !important;
        }
        
        /* Ensure the iframe container takes up the full space if needed */
        iframe {
            display: block;
        }
    </style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

# 3. The Payload (Iframe + Analytics)
# We use a raw HTML component to inject the iframe. 
# Key Technical Details:
# - position: fixed: This breaks the iframe out of the Streamlit 'flow', allowing it to cover headers/padding.
# - height: 100dvh: Ensures the viewport height is dynamic on mobile browsers (handles address bar resizing).
# - z-index: 99999: Forces the iframe to sit on top of any residual UI elements.
# - Sandbox: Added 'allow-same-origin' and 'allow-scripts' to satisfy strict browser security (DuckDuckGo/Brave).

html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body, html {
            margin: 0; 
            padding: 0; 
            overflow: hidden; 
            background-color: #000000;
            height: 100%;
        }
        iframe {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100dvh;
            border: none;
            z-index: 99999;
            background-color: #000000;
        }
    </style>
    <script data-goatcounter="https://moon-papers.goatcounter.com/count"
            async src="//gc.zgo.at/count.js"></script>
</head>
<body>
    <iframe 
        src="https://chessmastermind.github.io/moon-papers/"
        sandbox="allow-scripts allow-same-origin allow-forms allow-popups allow-modals"
        allowfullscreen
    ></iframe>
</body>
</html>
"""

# Render the HTML component with a specific height to prevent initial layout shift,
# though the CSS 'position: fixed' handles the actual display logic.
components.html(html_content, height=800, scrolling=False)
