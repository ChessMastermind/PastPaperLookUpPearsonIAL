import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Redirecting...",
    page_icon="🌙",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Complete UI Wipeout
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div[data-testid="stToolbar"] {display: none;}
    div[data-testid="stDecoration"] {display: none;}
    div[data-testid="stStatusWidget"] {visibility: hidden;}
    [data-testid="stAppViewContainer"] {background-color: #ffffff;}
    .block-container {padding: 0rem;}
    </style>
    """,
    unsafe_allow_html=True
)

# 3. The Unconditional Redirect & Tracker
target_url = "https://chessmastermind.github.io/moon-papers/"

st.markdown(
    f"""
    <div style="text-align: center; padding-top: 30vh; font-family: sans-serif;">
        <h2 style="color: #333;">Moving to Moon Papers</h2>
        <p style="color: #666;">Redirecting you now...</p>
        <p style="font-size: 0.8em;">If nothing happens, <a href="{target_url}">click here</a>.</p>
    </div>

    <script data-goatcounter="https://moon-papers.goatcounter.com/count"
            async src="//gc.zgo.at/count.js"></script>

    <img src="https://moon-papers.goatcounter.com/count?p=/streamlit-proxy&title=Streamlit%20Redirect" 
         style="display:none" 
         alt="">

    <script>
        // Use double curly braces to escape them in a Python f-string
        setTimeout(function() {{
            window.location.href = "{target_url}";
        }}, 500);
    </script>
    """,
    unsafe_allow_html=True
)
