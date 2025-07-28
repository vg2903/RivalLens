import streamlit as st
from gsc_utils import get_gsc_data  # Placeholder for GSC integration

st.set_page_config(page_title="RivalLens", layout="wide")

st.title("🔍 RivalLens - SEO Audit & Competitor Analyzer")

with st.sidebar:
    st.header("🔑 API Keys")
    openai_key = st.text_input("OpenAI API Key", type="password")
    gemini_key = st.text_input("Gemini API Key", type="password")
    semrush_key = st.text_input("Semrush API Key", type="password")
    gsc_json_key = st.file_uploader("GSC Service Account JSON", type="json")

    st.header("⚙️ Feature Toggles")
    use_semantic = st.checkbox("Enable Semantic Expansion", value=True)
    use_competitor = st.checkbox("Enable Competitor Comparison", value=False)
    use_export = st.checkbox("Enable Export Options", value=True)

st.markdown("### Enter your URLs")
url = st.text_input("🔗 Your Page URL")
competitor_url = st.text_input("🥊 Competitor Page URL (optional)")

if url and openai_key:
    st.success("🧠 Content analysis and keyword research modules will run here.")
    st.info("Next step: Integrate GPT, Semrush, GSC logic here.")
else:
    st.warning("Please enter your URL and OpenAI API key to proceed.")
