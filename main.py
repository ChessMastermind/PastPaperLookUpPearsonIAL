import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Moon Papers",
    page_icon="🌙",
    layout="wide", # Essential for full-width
    initial_sidebar_state="collapsed"
)

# 2. Complete UI Wipeout (Dark Theme)
# This removes all Streamlit margins and bars so the iframe fills everything.
st.markdown(
    """
    <style>
    /* Hide Streamlit UI */
    #MainMenu, footer, header, [data-testid="stToolbar"], 
    [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
        display: none !important;
    }
    
    /* Remove all padding from the Streamlit container */
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
        height: 100vh !important;
    }

    /* Ensure the iframe container is full height */
    [data-testid="stVerticalBlock"] {
        gap: 0rem;
    }

    body {
        background-color: #000000;
        margin: 0;
        overflow: hidden; /* Prevent double scrollbars */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. The Proxy Logic (Iframe + GoatCounter)
target_url = "https://chessmastermind.github.io/moon-papers/"

st.components.v1.html(
    f"""
    <script data-goatcounter="https://moon-papers.goatcounter.com/count"
            async src="//gc.zgo.at/count.js"></script>

    <iframe 
        src="{target_url}" 
        style="position:fixed; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;"
    >
        Your browser doesn't support iframes.
    </iframe>
    """,
    height=1000, # This is a fallback; the CSS above handles the real height
)
