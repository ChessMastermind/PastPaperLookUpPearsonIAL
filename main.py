import streamlit as st

# 1. Page Configuration (Minimalist)
st.set_page_config(
    page_title="Redirecting",
    page_icon="🌙",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Total "Dark Ghost" UI Overhaul
# This hides all Streamlit UI and makes the background dark immediately.
st.markdown(
    """
    <style>
    /* Hide all Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div[data-testid="stToolbar"] {display: none;}
    div[data-testid="stDecoration"] {display: none;}
    div[data-testid="stStatusWidget"] {visibility: hidden;}
    
    /* Dark background and hide content */
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117;
    }
    .block-container {padding: 0rem;}
    
    /* Make the text nearly invisible/subtle for a cleaner look */
    .redirect-text {
        color: #555;
        text-align: center;
        padding-top: 45vh;
        font-family: sans-serif;
        font-size: 0.9em;
    }
    </style>

    <div class="redirect-text">
        Loading...
    </div>
    """,
    unsafe_allow_html=True
)

# 3. Fast Redirect & GoatCounter
target_url = "https://chessmastermind.github.io/moon-papers/"

st.markdown(
    f"""
    <script data-goatcounter="https://moon-papers.goatcounter.com/count"
            async src="//gc.zgo.at/count.js"></script>

    <img src="https://moon-papers.goatcounter.com/count?p=/streamlit-proxy&title=Streamlit%20Dark%20Redirect" 
         style="display:none" 
         alt="">

    <script>
        // Redirect as fast as possible (300ms is usually enough for the pixel to fire)
        setTimeout(function() {{
            window.location.replace("{target_url}");
        }}, 300);
    </script>
    """,
    unsafe_allow_html=True
)
