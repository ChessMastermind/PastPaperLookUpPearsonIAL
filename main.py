import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Moon Papers",
    page_icon="🌙",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Immediate Dark Ghost UI
# This forces the background to dark immediately with no text.
st.markdown(
    """
    <style>
    #MainMenu, footer, header, [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
        display: none !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117;
    }
    .block-container {padding: 0rem;}
    </style>
    """,
    unsafe_allow_html=True
)

# 3. The "Ghost" Proxy Logic
target_url = "https://chessmastermind.github.io/moon-papers/"

st.markdown(
    f"""
    <script data-goatcounter="https://moon-papers.goatcounter.com/count"
            async src="//gc.zgo.at/count.js"></script>

    <img src="https://moon-papers.goatcounter.com/count?p=/streamlit-immediate&title=Instant%20Redirect" 
         style="display:none" 
         alt="">

    <script>
        // No delay - fire immediately
        window.location.replace("{target_url}");
    </script>
    """,
    unsafe_allow_html=True
)
