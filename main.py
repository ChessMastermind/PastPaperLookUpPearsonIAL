import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Moon Papers",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Maximum UI Stripping (Hides 'Manage app', Header, and Footer)
st.markdown(
    """
    <style>
    /* Hide the 'Manage app' button and status widget */
    [data-testid="stStatusWidget"], 
    button[title="Manage app"],
    .stDeployButton {
        display: none !important;
    }

    /* Hide the Main Menu (Hamburger) and Header */
    #MainMenu, header, [data-testid="stHeader"] {
        visibility: hidden !important;
        display: none !important;
    }

    /* Hide the Footer */
    footer {
        visibility: hidden !important;
        display: none !important;
    }

    /* Total Screen Reset */
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
        height: 100vh !important;
    }

    [data-testid="stVerticalBlock"] {
        gap: 0rem;
    }

    /* Force the background to black and remove scrollbars */
    body, .stApp {
        background-color: #000000 !important;
        margin: 0;
        overflow: hidden !important;
    }

    iframe {
        border: none;
        width: 100vw;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. The Proxy Logic
# We use the Streamlit components to embed the GitHub Pages site.
target_url = "https://chessmastermind.github.io/moon-papers/"

st.components.v1.html(
    f"""
    <script data-goatcounter="https://moon-papers.goatcounter.com/count"
            async src="//gc.zgo.at/count.js"></script>

    <iframe 
        src="{target_url}" 
        style="position:fixed; top:0; left:0; width:100vw; height:100vh; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;"
        allowfullscreen
    ></iframe>
    """,
    height=2000, # Large height to ensure the iframe has room to expand
)
