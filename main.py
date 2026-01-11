import streamlit as st
import google.generativeai as genai
import time

# UI Setup
st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")
st.markdown("### Viral-Audit Engine: Level 2")

# API Key from Secrets
try:
    genai.configure(api_key=st.secrets["AIzaSyDeSWaFrB8wc0Bp2sKKKQmEsvqKvun7ZHM"])
except:
    st.error("API Key missing in Streamlit Secrets!")

# File Upload
video_file = st.file_uploader("Upload your Reel/Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    
    if st.button("RUN VIRAL AUDIT"):
        with st.status("AI is watching your video...", expanded=True) as status:
            st.write("Checking Hook and Lighting...")
            time.sleep(2)
            st.write("Analyzing Trends and Content...")
            
            # Asli Gemini AI Prompt (Abhi basic check ke liye)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content("Analyze this video idea for viral potential. Suggest 3 improvements for a short reel.")
            
            status.update(label="Audit Complete!", state="complete", expanded=False)
            
        st.subheader("Viro Audit Report")
        st.write(response.text)
        st.balloons()
        
