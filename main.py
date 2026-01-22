import streamlit as st
import streamlit.components.v1 as components

# 1. Configuration
st.set_page_config(
    page_title="Moon Papers",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Aggressive CSS: Hide UI + Lock Resolution
# We add 'overflow: hidden' to .stApp to prevent Streamlit from 
# adding its own scrollbars, forcing the app to match the screen resolution exactly.
hide_streamlit_ui = """
    <style>
        /* Hide all standard Streamlit UI elements */
        header[data-testid="stHeader"],
        section[data-testid="stSidebar"],
        .stDeployButton,
        [data-testid="stToolbar"],
        footer {
            display: none !important;
        }
        
        /* Reset Block Container */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* FORCE FULL SCREEN RESOLUTION */
        /* This removes the scrollbar from the main Streamlit app, 
           ensuring the iframe is the only thing the user interacts with. */
        .stApp {
            background-color: #000000 !important;
            overflow: hidden !important; 
        }
        
        iframe {
            display: block;
        }
    </style>
"""
st.markdown(hide_streamlit_ui, unsafe_allow_html=True)

# 3. The Responsive Payload
# The CSS below dynamically captures the "Current Screen Resolution"
# regardless of the device.
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        /* Reset standard HTML margins */
        body, html {
            margin: 0; 
            padding: 0; 
            overflow: hidden; /* Prevent internal scrolling */
            background-color: #000000;
            width: 100%;
            height: 100%;
        }
        
        /* The Iframe Container */
        iframe {
            position: fixed;   /* Break out of document flow */
            top: 0;
            left: 0;
            
            /* DYNAMIC RESOLUTION SETTINGS */
            width: 100vw;      /* 100% of the Viewport Width */
            height: 100dvh;    /* 100% of the Dynamic Viewport Height (ignores mobile address bars) */
            
            border: none;
            z-index: 99999;    /* Sit on top of everything */
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

# Height must be set here to render the component, but the CSS 'fixed' position
# overrides this visually.
components.html(html_content, height=1000, scrolling=False)
