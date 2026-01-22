import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Moon Papers",
    page_icon="🌙",
    layout="wide"
)

# 2. Force Viewer Mode (Removes the Developer UI)
st.set_option("client.toolbarMode", "viewer")

# 3. Clean UI CSS
st.markdown(
    """
    <style>
    /* Completely hide the header, footer, and status widget */
    header, footer, .stDeployButton, [data-testid="stStatusWidget"] {
        visibility: hidden !important;
        height: 0 !important;
        padding: 0 !important;
    }
    
    /* Remove margins to let the iframe fill the screen */
    .block-container {
        padding: 0rem !important;
        margin-top: -60px !important; /* Pulls content up into header space */
    }

    /* Force black background */
    body, .stApp {
        background-color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 4. The Proxy (100vh Dynamic Height)
target_url = "https://chessmastermind.github.io/moon-papers/"

st.components.v1.html(
    f"""
    <div style="margin: 0; padding: 0; height: 100vh; background-color: #000;">
        <script data-goatcounter="https://moon-papers.goatcounter.com/count"
                async src="//gc.zgo.at/count.js"></script>

        <iframe 
            src="{target_url}" 
            style="width: 100%; height: 100%; border: none; overflow: hidden;"
            allowfullscreen
        ></iframe>
    </div>
    """,
    height=1000 # Fallback height for older browsers
)
