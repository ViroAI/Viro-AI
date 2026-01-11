import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")

# API Connection
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Sirf ye ek naam hai jo ab chalege: gemini-1.5-flash
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.sidebar.success("Engine: Ready ✅")
else:
    st.error("API Key Missing!")
    st.stop()

video_file = st.file_uploader("Upload Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    if st.button("RUN VIRAL AUDIT"):
        with st.spinner("Viro AI is analyzing..."):
            try:
                # Direct response
                response = model.generate_content("Give 3 viral tips for this video.")
                st.subheader("Viro Audit Report")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error("Google's server is busy. Wait 10 seconds and click again!")
                
