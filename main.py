import streamlit as st

st.set_page_config(
    page_title="Moon Papers - New Location",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    /* Hide Streamlit UI completely */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { 
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 40px 20px;
        text-align: center;
    }
    .logo {
        font-size: 4em;
        margin-bottom: 20px;
    }
    .domain {
        font-size: 2em;
        color: #4ade80;
        font-weight: bold;
        margin: 30px 0;
        word-break: break-all;
    }
    .btn {
        display: inline-block;
        background: #2563eb;
        color: white !important;
        text-decoration: none;
        padding: 18px 50px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 1.3em;
        margin: 40px 0;
        transition: all 0.3s;
        border: 2px solid #2563eb;
    }
    .btn:hover {
        background: #1d4ed8;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
    }
    .info {
        background: rgba(255, 255, 255, 0.05);
        border-left: 4px solid #4ade80;
        padding: 20px;
        margin: 30px 0;
        text-align: left;
    }
    .info h3 {
        margin-top: 0;
        color: #4ade80;
    }
    .warning {
        color: #fbbf24;
        font-size: 0.9em;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="container">
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
</div>
""", unsafe_allow_html=True)

# Optional: Add basic analytics tracking
st.markdown("""
<script>
    // Track page view (add your analytics code here if needed)
    console.log('User viewed the moved notice page');
    
    // Example: Google Analytics event
    // gtag('event', 'page_view', {
    //     'page_title': 'Moon Papers - Moved Notice',
    //     'page_location': window.location.href
    // });
</script>
""", unsafe_allow_html=True)

st.stop()
