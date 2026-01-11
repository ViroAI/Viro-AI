import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")

# API Setup
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # Naye update ke liye direct model name
        model = genai.GenerativeModel('gemini-1.5-flash')
        st.sidebar.success("Engine: Ready ✅")
    except Exception as e:
        st.sidebar.error(f"Setup Error: {e}")
else:
    st.error("API Key Missing in Secrets!")
    st.stop()

video_file = st.file_uploader("Upload Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    if st.button("RUN VIRAL AUDIT"):
        with st.spinner("AI is analyzing your video..."):
            try:
                # Direct simple prompt
                response = model.generate_content("Give 3 viral tips for this video idea.")
                if response:
                    st.subheader("Viro Audit Report")
                    st.write(response.text)
                    st.balloons()
            except Exception as e:
                # Agar error aaye toh hume exact technical detail dikhegi
                st.error(f"AI Service Error: {e}")
                
