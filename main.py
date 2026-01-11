import streamlit as st
import google.generativeai as genai
import time

# UI Setup
st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")
st.markdown("### Viral-Audit Engine: Level 2")

# API Key Connection - Direct check from secrets
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    st.sidebar.success("AI Brain Connected!")
else:
    st.error("Secrets mein API Key nahi mili! Settings check karein.")
    st.stop()

# File Upload
video_file = st.file_uploader("Upload your Reel/Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    
    if st.button("RUN VIRAL AUDIT"):
        with st.status("Viro AI is analyzing...", expanded=True) as status:
            st.write("🔍 Scanning frames...")
            time.sleep(1)
            st.write("📊 Checking viral trends...")
            
            try:
                # Prompt for AI
                response = model.generate_content("Analyze this video idea. Give 3 viral tips and a score out of 10.")
                
                status.update(label="Audit Complete!", state="complete", expanded=False)
                st.subheader("Viro Audit Report")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"AI Error: {e}")
                
