import streamlit as st

# 1. Page Configuration - Standard settings for stability
st.set_page_config(
    page_title="Moon Papers",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Stable UI Cleanup
# We only hide the most intrusive parts to avoid layout bugs.
st.markdown(
    """
    <style>
    /* Hide the header and footer which are the most distracting */
    header, footer, .stDeployButton {
        visibility: hidden;
        height: 0;
    }
    
    /* Reset margins so the content fills the space naturally */
    .block-container {
        padding: 0rem !important;
        margin-top: -50px; /* Moves the content up to cover the header area */
    }

    /* Dark background to match your theme */
    .stApp {
        background-color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. The Proxy Logic
target_url = "https://chessmastermind.github.io/moon-papers/"

# We use the standard iframe component - it's the most stable way.
st.components.v1.html(
    f"""
    <div style="margin: 0; padding: 0;">
        <script data-goatcounter="https://moon-papers.goatcounter.com/count"
                async src="//gc.zgo.at/count.js"></script>

        <iframe 
            src="{target_url}" 
            style="width: 100%; height: 100vh; border: none; margin: 0; padding: 0;"
            allowfullscreen
        ></iframe>
    </div>
    """,
    height=800, # This ensures the iframe has a defined height to start
)
