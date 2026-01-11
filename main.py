import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")

# API Setup
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Sabse stable model: gemini-1.0-pro
    model = genai.GenerativeModel('gemini-1.0-pro')
    st.sidebar.success("Engine: Stable Active ✅")
else:
    st.error("API Key Missing!")
    st.stop()

video_file = st.file_uploader("Upload Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    if st.button("RUN VIRAL AUDIT"):
        with st.spinner("AI is generating report..."):
            try:
                # Direct response
                response = model.generate_content("Give 3 viral tips for this video idea. Keep it very short.")
                st.subheader("Viro Audit Report")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}. Please try clicking the button one more time.")
                
