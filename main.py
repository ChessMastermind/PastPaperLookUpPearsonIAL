import streamlit as st
from streamlit.components.v1 import html

# Configure page
st.set_page_config(
    page_title="Moon Papers - Moved",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide all Streamlit chrome (menu, footer, headers)
st.markdown("""
<style>
#MainMenu, footer, header, .stDeployButton, .stSpinner {
    visibility: hidden;
    display: none;
}
.stApp {
    background-color: #000000;
    margin: 0;
    padding: 0;
}
iframe {
    border: none;
}
</style>
""", unsafe_allow_html=True)

# Your complete HTML content
HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moon Papers - Moved</title>
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            text-align: center;
            padding: 20px;
        }
        .container {
            max-width: 600px;
        }
        .info-box {
            background: rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 30px;
            margin: 0 auto 30px;
            border-left: 4px solid #4ade80;
        }
        .info-box p {
            margin: 0;
            line-height: 1.6;
        }
        .domain {
            font-size: 2rem;
            color: #4ade80;
            font-weight: bold;
            margin: 20px 0;
            word-break: break-all;
        }
        .btn {
            display: inline-block;
            background: #2563eb;
            color: #fff;
            text-decoration: none;
            padding: 18px 50px;
            border-radius: 10px;
            font-weight: 600;
            font-size: 1.3rem;
            margin-top: 20px;
            transition: all 0.3s;
            border: 2px solid #2563eb;
        }
        .btn:hover {
            background: #1d4ed8;
            transform: translateY(-2px);
        }
        .note {
            margin-top: 40px;
            color: #666;
            font-size: 0.9rem;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <div style="font-size: 5rem; margin-bottom: 20px;">🌙</div>
        <h1 style="font-size: 3rem; margin: 0 0 10px 0;">Moon Papers</h1>
        <h2 style="color: #888; margin: 0 0 40px 0; font-weight: normal;">Has Moved to a New Domain</h2>
        <div class="info-box">
            <p>Our website is now permanently located at:</p>
            <div class="domain">moon-papers.com</div>
            <p>The old Streamlit app is no longer in use.<br>Please update your bookmarks.</p>
        </div>
        <a href="https://moon-papers.com" class="btn">→ Visit New Site Now</a>
        <p class="note">
            <strong>Note:</strong> If you're not redirected automatically,<br>
            click the button above to access Moon Papers.
        </p>
    </div>
</body>
</html>"""

# Render full-screen
html(HTML_CONTENT, height=800, scrolling=False)
