import streamlit as st

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
</body>
</html>
""", unsafe_allow_html=True)

st.stop()
