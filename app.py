import streamlit as st
from pathlib import Path

ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "ChatGPT Image.jpg"

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ AI Travel Planner for Students")

st.image(
    str(ASSETS_PATH),
    use_container_width=True
)

st.markdown("""
## Explore India Smartly

Plan affordable student trips across India.

Use the sidebar to navigate through the application.
""")

st.success("Website Loaded Successfully")