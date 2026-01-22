import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="Moon Papers",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hide Developer Toolbar
st.set_option("client.toolbarMode", "viewer")

# 3. The "No-Gap" CSS Reset
st.markdown(
    """
    <style>
    /* Hide Streamlit UI elements */
    header, footer, [data-testid="stHeader"], .stDeployButton, [data-testid="stStatusWidget"] {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
    }

    /* Reset ALL margins/padding */
    .block-container, .stApp, .stAppViewContainer {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100vw !important;
        overflow: hidden !important;
    }

    /* Force background to black */
    body, .stApp {
        background-color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 4. The Responsive Iframe (Using 'dvh' for mobile support)
target_url = "https://chessmastermind.github.io/moon-papers/"

components.html(
    f"""
    <!DOCTYPE html>
    <html style="margin: 0; padding: 0; height: 100%;">
    <body style="margin: 0; padding: 0; height: 100%; background-color: black; overflow: hidden;">
        
        <script data-goatcounter="https://moon-papers.goatcounter.com/count"
                async src="//gc.zgo.at/count.js"></script>

        <iframe 
            src="{target_url}" 
            style="
                position: absolute; 
                top: 0; 
                left: 0; 
                width: 100%; 
                height: 100dvh; 
                border: none; 
                z-index: 999999;
            "
            allow="fullscreen; encrypted-media; picture-in-picture"
            sandbox="allow-forms allow-scripts allow-same-origin allow-popups allow-downloads"
        ></iframe>

    </body>
    </html>
    """,
    height=0, 
    scrolling=False 
)
