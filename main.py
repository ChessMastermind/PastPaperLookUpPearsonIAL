import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Moon Papers",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. The "Extreme" UI Stripper
st.markdown(
    """
    <style>
    /* Target the root containers that Streamlit uses */
    [data-testid="stHeader"], 
    [data-testid="stToolbar"], 
    [data-testid="stDecoration"],
    footer, 
    .stDeployButton,
    #MainMenu {
        display: none !important;
        visibility: hidden !important;
    }

    /* This targets the "Manage app" button specifically */
    div[data-testid="stStatusWidget"] {
        display: none !important;
    }

    /* Force the main container to be the full viewport */
    .main .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100vw !important;
        height: 100vh !important;
    }

    /* Hide the scrollbar on the Streamlit layer */
    [data-testid="stAppViewContainer"] {
        overflow: hidden !important;
    }

    /* Dark theme background */
    body, .stApp {
        background-color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. The Proxy Component
# We place the Iframe inside a container that ignores all Streamlit boundaries.
target_url = "https://chessmastermind.github.io/moon-papers/"

st.components.v1.html(
    f"""
    <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background-color: #000; z-index: 9999999;">
        <script data-goatcounter="https://moon-papers.goatcounter.com/count"
                async src="//gc.zgo.at/count.js"></script>

        <iframe 
            src="{target_url}" 
            style="width: 100%; height: 100%; border: none; outline: none;"
            allowfullscreen
        ></iframe>
    </div>
    """,
    height=2000, # Overflow doesn't matter because of the 'fixed' positioning above
)
