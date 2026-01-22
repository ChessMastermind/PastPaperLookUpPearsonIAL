import streamlit as st
import streamlit.components.v1 as components

# 1. Configuration
st.set_page_config(
    page_title="Moon Papers",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Aggressive CSS: Unlock the Streamlit Sandbox
# We must target the Streamlit Component iframe itself and force it 
# to break out of the standard layout flow.
hide_streamlit_ui = """
    <style>
        /* 1. Hide standard Streamlit UI */
        header[data-testid="stHeader"],
        section[data-testid="stSidebar"],
        .stDeployButton,
        [data-testid="stToolbar"],
        footer {
            display: none !important;
        }
        
        /* 2. Remove Layout Padding */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        .stApp {
            background-color: #000000 !important;
            overflow: hidden !important;
        }

        /* 3. CRITICAL: Force the Streamlit Component Iframe to Full Screen
           This targets the iframe created by components.html and makes it
           overlay the entire page. */
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

# 3. JavaScript-Driven Payload
# instead of relying on CSS percentages, we use JS to read the exact
# window dimensions and apply them to our target iframe.
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            background-color: #000000;
            overflow: hidden; /* No scrollbars allowed */
        }
        #target-frame {
            border: none;
            display: block;
        }
    </style>
    <script data-goatcounter="https://moon-papers.goatcounter.com/count"
            async src="//gc.zgo.at/count.js"></script>
</head>
<body>
    <iframe 
        id="target-frame"
        src="https://chessmastermind.github.io/moon-papers/"
        sandbox="allow-scripts allow-same-origin allow-forms allow-popups allow-modals"
        allowfullscreen
    ></iframe>

    <script>
        // THE JAVASCRIPT RESIZER
        // This function reads the exact pixel size of the visible window
        // and forces the iframe to match it.
        function resizeIframe() {
            const frame = document.getElementById('target-frame');
            
            // Get exact viewport dimensions
            const w = window.innerWidth;
            const h = window.innerHeight;
            
            // Apply to iframe
            frame.style.width = w + 'px';
            frame.style.height = h + 'px';
            
            console.log(`Resized to ${w}x${h}`);
        }

        // Listen for window resize events (e.g., rotating phone)
        window.addEventListener('resize', resizeIframe);
        
        // Listen for initial load
        window.addEventListener('load', resizeIframe);
        
        // Force one run immediately just in case
        resizeIframe();
    </script>
</body>
</html>
"""

# Render the component. 
# The height here is irrelevant because our CSS overrides it, 
# but we set it to avoid Streamlit warnings.
components.html(html_content, height=1000, scrolling=False)
