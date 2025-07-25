import streamlit as st

st.set_page_config(page_title="RivalLens", layout="wide")

st.title("🔍 RivalLens - SEO Audit & Competitor Analyzer")

st.markdown("""
Welcome to **RivalLens** – an advanced SEO and content analyzer.

Use the sidebar to enter your:
- 🔑 API keys (OpenAI, Gemini, Semrush, Ahrefs, GKP)
- 🔗 Your target URL
- 🥊 Optional competitor URL
- ⚙️ Toggle features like semantic expansion, keyword export, etc.
""")

st.info("🚧 Full version includes keyword audit, semantic expansion, and competitor comparison modules.")
st.warning("This is a starter app template. Insert your logic in `app.py` based on modules.")
