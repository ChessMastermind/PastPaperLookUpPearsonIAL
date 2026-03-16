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

st.stop()import streamlit as st

st.set_page_config(
    page_title="Moon Papers - New Location",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# Immediate redirect with user-friendly message
st.markdown(f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="robots" content="noindex, nofollow">
    <title>Redirecting to Moon Papers</title>
    <style>
        body {{
            font-family: sans-serif;
            background: #000;
            color: #fff;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            text-align: center;
        }}
        .container {{
            max-width: 600px;
            padding: 2rem;
        }}
        h1 {{ font-size: 2.5rem; margin-bottom: 1rem; }}
        p {{ font-size: 1.2rem; color: #ccc; margin-bottom: 2rem; }}
        .btn {{
            display: inline-block;
            background: #2563eb;
            color: white;
            text-decoration: none;
            padding: 12px 30px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 1.1rem;
        }}
        .btn:hover {{ background: #1d4ed8; }}
    </style>
</head>
<body>
    <div class="logo">🌙</div>
    <h1 style="font-size: 2.5em; margin-bottom: 10px;">Moon Papers</h1>
    <h2 style="color: #888; margin-bottom: 50px;">Has Moved to a New Domain</h2>
    
    <div class="info">
        <h3>📢 Important Update</h3>
        <p>Our website is now permanently located at <strong>moon-papers.com</strong>. The old Streamlit hosting will be discontinued soon.</p>
        <p><strong>Why the change?</strong> Our new domain provides faster loading, better reliability, and an improved experience.</p>
    </div>
    
    <p style="font-size: 1.2em; margin-bottom: 30px;">
        Please update your bookmarks and continue to:
    </p>
    
    <div class="domain">
        moon-papers.com
    </div>
    
    <a href="https://moon-papers.com/old-ial" class="btn">
        → Visit the New Site Now
    </a>
    
    <div class="warning">
        ⚠️ <strong>Note:</strong> The old Streamlit link will no longer show the website content.<br>
        Click the button above to access Moon Papers.
    </div>
    
    <p style="margin-top: 60px; color: #666; font-size: 0.9em; line-height: 1.6;">
        Thank you for your support during our migration.<br>
        If you experience any issues accessing the new site, please check your internet connection.
    </p>
</body>
</html>
""", unsafe_allow_html=True)

st.stop()
