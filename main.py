import streamlit as st

st.set_page_config(
    page_title="301 Moved Permanently",
    page_icon="🌙",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide all Streamlit chrome for clean look
st.markdown("""
<style>
    #MainMenu, footer, header, .stDeployButton {visibility: hidden;}
    .stApp {background-color: #0a0a0a;}
    .block-container {max-width: 700px; padding-top: 80px;}
</style>
""", unsafe_allow_html=True)

# Content
st.markdown("""
<div style="text-align: center; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
    
    <div style="font-size: 72px; margin-bottom: 24px;">🌙</div>
    
    <div style="color: #888; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 16px;">
        301 Moved Permanently
    </div>
    
    <h1 style="color: #fff; font-size: 42px; margin-bottom: 32px; font-weight: 700;">
        Moon Papers Has Relocated
    </h1>
    
    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 32px; margin: 32px 0;">
        <p style="color: #aaa; font-size: 16px; margin: 0 0 12px 0;">
            This application has permanently moved to:
        </p>
        <div style="color: #4ade80; font-size: 32px; font-weight: bold; margin: 16px 0; word-break: break-all;">
            moon-papers.com
        </div>
        <p style="color: #666; font-size: 14px; margin: 0;">
            Please update your bookmarks. The old URL is no longer active.
        </p>
    </div>
    
    <a href="https://moon-papers.com" target="_top" style="
        display: inline-block;
        background: #2563eb;
        color: #fff;
        text-decoration: none;
        padding: 18px 40px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 18px;
        margin-top: 16px;
        border: 2px solid #2563eb;
        transition: all 0.2s;
    ">Visit New Site →</a>
    
    <p style="color: #444; font-size: 13px; margin-top: 48px;">
        Clicking the button above will navigate to the new domain.<br>
        Automatic redirect is unavailable due to browser security restrictions.
    </p>
    
</div>
""", unsafe_allow_html=True)
