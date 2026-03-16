import streamlit as st

# Immediate redirect (0 seconds)
st.markdown(
    '<meta http-equiv="refresh" content="0; url=https://moon-papers.com">',
    unsafe_allow_html=True
)

st.markdown(
    '<script>window.location.href = "https://moon-papers.com";</script>',
    unsafe_allow_html=True
)
