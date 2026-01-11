import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")

# Simple Connection
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Hum 'gemini-pro' use karenge jo sabse stable hai
    model = genai.GenerativeModel('gemini-pro')
    st.sidebar.success("Engine Ready ✅")
else:
    st.error("API Key Missing in Secrets!")
    st.stop()

video_file = st.file_uploader("Upload Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    if st.button("RUN VIRAL AUDIT"):
        with st.spinner("AI is thinking..."):
            try:
                # Bahut chota prompt taaki server par load na pade
                response = model.generate_content("Viral tips for gaming reel")
                st.subheader("Viro Audit Report")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                # Ye line hume asli error batayegi
                st.error(f"Google Busy: {e}")
                
