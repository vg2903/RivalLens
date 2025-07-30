import streamlit as st

st.set_page_config(page_title="RivalLens - SEO Analyzer", layout="wide")

# Step 1: API Keys
st.sidebar.header("🔐 API Keys")
openai_key = st.sidebar.text_input("OpenAI API Key", type="password")
gemini_key = st.sidebar.text_input("Gemini API Key", type="password")
semrush_key = st.sidebar.text_input("Semrush API Key", type="password")
ahrefs_key = st.sidebar.text_input("Ahrefs API Key", type="password")
gkp_key = st.sidebar.text_input("Google Keyword Planner API Key", type="password")
gsc_json = st.sidebar.file_uploader("Upload GSC JSON", type="json")

# Step 2: URL Input
st.header("🔗 Step 1: Enter Target & Competitor URLs")
url = st.text_input("Your Page URL")
competitor_urls = st.text_area("Competitor URLs (one per line)").splitlines()

# Step 3: Optional Keyword Upload
st.header("📥 Step 2: Upload Keyword File (Optional)")
keyword_file = st.file_uploader("Upload Excel/CSV with keywords", type=["csv", "xlsx"])

# Step 4: Analysis Trigger
if st.button("🚀 Next: Start Analysis"):
    if not url:
        st.warning("Please enter your URL.")
    else:
        st.success("All set! In full version, analysis will now run with content scraping, GSC fetch, keyword research, etc.")

st.markdown("Made with ❤️ by RivalLens")
