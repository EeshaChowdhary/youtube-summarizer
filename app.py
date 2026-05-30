import streamlit as st
from transcript import get_transcript
from summarize import summarize

st.set_page_config(page_title="YouTube Summarizer", page_icon="🎥")
st.title("🎥 YouTube Video Summarizer")
st.write("Paste any YouTube link and get instant notes, summary and key terms.")

url = st.text_input("YouTube URL")

if st.button("Summarize"):
    if not url:
        st.warning("Please enter a YouTube URL")
    else:
        with st.spinner("Fetching transcript..."):
            try:
                transcript = get_transcript(url)
                st.success("Transcript fetched!")
            except Exception as e:
                st.error(f"Could not get transcript: {e}")
                st.stop()

        with st.spinner("Summarizing with AI..."):
            result = summarize(transcript)

        st.markdown("## 📝 Your Summary")
        st.markdown(result)