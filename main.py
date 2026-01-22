import streamlit as st
import datetime
import streamlit.components.v1 as components

# 1. Page Config (Must be the first command)
st.set_page_config(
    page_title="Moon Papers",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Configuration
# Current Date: Jan 22, 2026
# Redirect Date: Jan 8, 2026
# Result: This app will currently ALWAYS redirect immediately.
redirect_date = datetime.datetime(2026, 1, 8)

# 3. Logic Flow
if datetime.datetime.now() > redirect_date:
    # --- REDIRECT LOGIC ---
    # This renders a meta-refresh tag to send the user to GitHub immediately.
    # The 'st.empty()' and CSS hides the Streamlit UI during the split-second transition.
    st.markdown(
        """
        <style>
            .stApp { display: none; } /* Hide the app interface */
        </style>
        <meta http-equiv="refresh" content="0; url=https://chessmastermind.github.io/moon-papers/" />
        <script>
            window.location.href = "https://chessmastermind.github.io/moon-papers/";
        </script>
        """,
        unsafe_allow_html=True
    )
    # Stop the script here so nothing else loads
    st.stop()

else:
    # --- PROXY LOGIC (If you extend the date) ---
    # If the deadline hasn't passed, we show the app with the popup logic you asked for.
    
    # A. Hide UI Elements
    st.markdown("""
        <style>
            header, footer, [data-testid="stToolbar"] {display: none !important;}
            .block-container {padding: 0 !important; margin: 0 !important;}
            .stApp {background-color: #000000; overflow: hidden;}
        </style>
        """, unsafe_allow_html=True)

    # B. Popup Logic (Session State)
    if 'popup_closed' not in st.session_state:
        st.session_state['popup_closed'] = False

    if not st.session_state['popup_closed']:
        # Show a simple announcement (optional)
        with st.container():
            st.info("Notice: We are migrating to a new server soon.")
            if st.button("Got it"):
                st.session_state['popup_closed'] = True
                st.rerun()
    
    # C. The Iframe Payload (Only loads if popup is closed or ignored)
    html_content = """
    <!DOCTYPE html>
    <html style="background: black; overflow: hidden;">
    <body style="margin: 0; padding: 0; background: black;">
        <iframe src="https://chessmastermind.github.io/moon-papers/" 
                style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; border: none;"
                allowfullscreen></iframe>
    </body>
    </html>
    """
    components.html(html_content, height=1000, scrolling=False)
