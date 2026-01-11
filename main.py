import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")

# API Setup from Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash') # 1.5 use karo, iski limit 2.0 se zyada hai
else:
    st.error("Secrets mein API Key nahi mili!")
    st.stop()

video_file = st.file_uploader("Upload Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    if st.button("RUN VIRAL AUDIT"):
        try:
            with st.spinner("Google AI ko active kar rahe hain... 5 sec rukiye"):
                time.sleep(5) # Yeh 'Google Busy' error se bachayega
                
                # Chota test prompt
                response = model.generate_content("Give 3 viral hooks for a gaming video.")
                
                st.subheader("Viro Audit Report")
                st.write(response.text)
                st.balloons()
        except Exception as e:
            if "429" in str(e):
                st.error("Bhai, Google thak gaya hai. 1 minute ruko, phir button dabana.")
            else:
                st.error(f"Error: {e}")
                
