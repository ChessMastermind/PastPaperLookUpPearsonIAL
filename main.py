import streamlit as st
import streamlit.components.v1 as components

# 1. Page Config: Wide layout is required to reset margins
st.set_page_config(
    page_title="Moon Papers",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hide Developer Toolbar (This hides the hamburger menu for users)
st.set_option("client.toolbarMode", "viewer")

# 3. CSS: Remove ALL padding, headers, and UI elements
st.markdown(
    """
    <style>
    /* Nuke the top header and the 'Manage app' button area */
    header[data-testid="stHeader"],
    [data-testid="stStatusWidget"],
    .stDeployButton {
        display: none !important;
        visibility: hidden !important;
    }

    /* Remove ALL padding from the main Streamlit container */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        margin-top: 0rem !important;
        max-width: 100vw !important;
    }
    
    /* Remove padding from the view container to prevent top whitespace */
    .stAppViewContainer {
        padding: 0 !important;
    }

    /* Force background to black to hide any loading flashes */
    .stApp, body {
        background-color: #000000 !important;
        overflow: hidden !important; /* Prevent double scrollbars */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 4. The "Fixed Overlay" Iframe
# We use position:fixed to ignore Streamlit's layout engine entirely.
target_url = "https://chessmastermind.github.io/moon-papers/"

components.html(
    f"""
    <script data-goatcounter="https://moon-papers.goatcounter.com/count"
            async src="//gc.zgo.at/count.js"></script>
            
    <iframe 
        src="{target_url}" 
        style="
            position: fixed; 
            top: 0; 
            left: 0; 
            bottom: 0; 
            right: 0; 
            width: 100%; 
            height: 100%; 
            border: none; 
            margin: 0; 
            padding: 0; 
            overflow: hidden; 
            z-index: 999999; 
        "
        allowfullscreen
    ></iframe>
    """,
    height=0, # Height doesn't matter because we used position: fixed
)
