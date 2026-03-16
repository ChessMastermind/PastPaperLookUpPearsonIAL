import streamlit as st

# ==========================================
# PERMANENT REDIRECT TO NEW DOMAIN
# ==========================================
st.set_page_config(
    page_title="Moon Papers - New Location",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Your new domain
NEW_DOMAIN = "https://moon-papers.com"

# Immediate redirect with user-friendly message
st.markdown(f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url={NEW_DOMAIN}">
    <meta name="robots" content="noindex, nofollow">
    <title>Moving to Moon Papers</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
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
        h1 {{
            color: #fff;
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }}
        p {{
            font-size: 1.2rem;
            color: #ccc;
            line-height: 1.6;
            margin-bottom: 2rem;
        }}
        .btn {{
            display: inline-block;
            background: #2563eb;
            color: white;
            text-decoration: none;
            padding: 12px 30px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 1.1rem;
            transition: background 0.3s;
            border: 2px solid #2563eb;
        }}
        .btn:hover {{
            background: #1d4ed8;
            border-color: #1d4ed8;
        }}
        .spinner {{
            margin: 20px auto;
            width: 40px;
            height: 40px;
            border: 4px solid rgba(255,255,255,0.3);
            border-radius: 50%;
            border-top-color: #fff;
            animation: spin 1s ease-in-out infinite;
        }}
        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🌙 Moon Papers has moved!</h1>
        <p>
            We've relocated to our new permanent home at<br>
            <strong style="color: #4ade80; font-size: 1.4rem;">{NEW_DOMAIN}</strong>
        </p>
        <div class="spinner"></div>
        <p style="font-size: 1rem; color: #888;">
            You will be redirected automatically in 3 seconds...<br>
            If not, click the button below:
        </p>
        <a href="{NEW_DOMAIN}/old-ial" class="btn">Go to Moon Papers Now →</a>
    </div>
    
    <script>
        // Automatic redirect after 3 seconds (in case meta refresh fails)
        setTimeout(function() {{
            window.location.replace("{NEW_DOMAIN}/old-ial");
        }}, 3000);
        
        // Prevent back button from staying on redirect page
        if (window.history && window.history.pushState) {{
            history.pushState("", document.title, window.location.pathname);
        }}
    </script>
</body>
</html>
""", unsafe_allow_html=True)

# Stop Streamlit from rendering anything else
st.stop()
