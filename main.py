import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")

# Simple Sidebar Status
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.sidebar.success("AI Brain: Active ✅")
else:
    st.error("API Key Missing!")
    st.stop()

video_file = st.file_uploader("Upload your Reel/Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    if st.button("RUN VIRAL AUDIT"):
        with st.status("AI is thinking...", expanded=True) as status:
            # Simple direct request
            try:
                response = model.generate_content("Give me 3 viral tips for this video idea. Keep it short.")
                st.subheader("Viro Audit Report")
                st.write(response.text)
                st.balloons()
                status.update(label="Done!", state="complete")
            except:
                st.error("Google's server is currently full. Try again in 2 minutes.")
                
