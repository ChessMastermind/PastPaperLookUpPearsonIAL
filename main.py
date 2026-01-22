import streamlit as st

# 1. Page Config: Wide mode is essential to remove side margins
st.set_page_config(
    page_title="Moon Papers",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS to Remove Streamlit's "Weird Upper Part" & Branding
st.markdown(
    """
    <style>
    /* 1. Remove the big white/black bar at the top (Streamlit's Header) */
    header[data-testid="stHeader"] {
        display: none !important;
    }

    /* 2. Remove the "Manage App" button and Developer Menu */
    .stDeployButton, [data-testid="stStatusWidget"] {
        display: none !important;
        visibility: hidden !important;
    }

    /* 3. Remove the internal padding that "squashes" the site */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }

    /* 4. Remove the footer "Made with Streamlit" */
    footer {
        display: none !important;
    }

    /* 5. Ensure the background is seamless */
    .stApp {
        background-color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. The Full-Screen Iframe
# We use 'scrolling="yes"' and 'height: 100vh' to make it feel native.
target_url = "https://chessmastermind.github.io/moon-papers/"

st.components.v1.html(
    f"""
    <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #000;">
        <script data-goatcounter="https://moon-papers.goatcounter.com/count"
                async src="//gc.zgo.at/count.js"></script>

        <iframe 
            src="{target_url}" 
            style="width: 100%; height: 100%; border: none;"
            scrolling="yes"
            allowfullscreen
        ></iframe>
    </div>
    """,
    height=2000, # This height is a fallback; the CSS '100vh' above handles the real sizing
)
