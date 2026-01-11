import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")

# API Setup
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # Tera bataya hua naya experimental model
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        st.sidebar.success("Engine: 2.0 Experimental Active ✅")
    except Exception as e:
        st.sidebar.error(f"Setup Error: {e}")
else:
    st.error("API Key Missing!")
    st.stop()

video_file = st.file_uploader("Upload Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    if st.button("RUN VIRAL AUDIT"):
        with st.spinner("AI 2.0 is analyzing..."):
            try:
                # Naye model ke liye simple request
                response = model.generate_content("Give 3 viral tips for this video idea.")
                st.subheader("Viro Audit Report (2.0)")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Model Error: {e}")
                st.info("Bhai agar ab bhi 404 aaye, toh wahi 'Model Finder' wala code daal ke asli list check karni padegi.")
                
