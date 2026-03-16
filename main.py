import streamlit as st
import datetime

st.set_page_config(
    page_title="Moon Papers - New Location",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide ALL Streamlit UI elements
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp { 
    background-color: #000000 !important;
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# Simple redirect page
st.markdown(f"""
<div style="
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    text-align: center;
    padding: 20px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
">
    <div style="font-size: 5rem; margin-bottom: 20px;">🌙</div>
    <h1 style="font-size: 3rem; margin: 0 0 10px 0; color: white;">Moon Papers</h1>
    <h2 style="font-size: 1.8rem; color: #888; margin: 0 0 40px 0; font-weight: normal;">
        Has Moved to a New Domain
    </h2>
    
    <div style="
        background: rgba(255,255,255,0.05);
        border-radius: 12px;
        padding: 30px;
        max-width: 600px;
        margin: 0 auto 30px auto;
        border-left: 4px solid #4ade80;
    ">
        <p style="font-size: 1.2rem; line-height: 1.6; margin: 0; color: #ddd;">
            Our website is now permanently located at:
        </p>
        <div style="
            font-size: 2rem; 
            color: #4ade80; 
            font-weight: bold; 
            margin: 20px 0;
            word-break: break-all;
        ">
            moon-papers.com
        </div>
        <p style="font-size: 1rem; color: #aaa; margin: 10px 0 0 0;">
            The old Streamlit app is no longer in use.<br>
            Please update your bookmarks.
        </p>
    </div>
    
    <a href="https://moon-papers.com" 
       style="
        display: inline-block;
        background: #2563eb;
        color: white;
        text-decoration: none;
        padding: 18px 50px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 1.3rem;
        margin-top: 20px;
        transition: all 0.3s;
        border: 2px solid #2563eb;
    "
    onmouseover="this.style.background='#1d4ed8'; this.style.transform='translateY(-2px)';"
    onmouseout="this.style.background='#2563eb'; this.style.transform='translateY(0)';">
        → Visit New Site Now
    </a>
    
    <p style="
        margin-top: 40px;
        color: #666;
        font-size: 0.9rem;
        max-width: 500px;
    ">
        <strong>Note:</strong> If you're not redirected automatically,<br>
        click the button above to access Moon Papers.
    </p>
</div>

<script>
    // Optional: Try to redirect automatically after 2 seconds
    setTimeout(function() {{
        window.location.replace("https://moon-papers.com");
    }}, 2000);
    
    // Optional: Track that user saw this page (add your analytics)
    console.log("User viewed: Old Streamlit app -> moon-papers.com migration page");
    
    // Example: Google Analytics event
    // if (typeof gtag !== 'undefined') {{
    //     gtag('event', 'migration_page_view', {{
    //         'event_category': 'migration',
    //         'event_label': 'streamlit_to_github_pages'
    //     }});
    // }}
</script>
""", unsafe_allow_html=True)

st.stop()
