import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")

# API Setup
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Hum specific model version try karenge
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    st.sidebar.success("System: Connected ✅")
else:
    st.error("API Key Missing!")
    st.stop()

video_file = st.file_uploader("Upload Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    if st.button("RUN VIRAL AUDIT"):
        try:
            # Bahut chota prompt taaki turant reply aaye
            response = model.generate_content("Give 3 viral tips for gaming.")
            st.subheader("Viro Audit Report")
            st.write(response.text)
            st.balloons()
        except Exception as e:
            # Agar ab bhi error aaye toh hum asli technical error dekhenge
            st.error(f"Technical Detail: {str(e)}")
            st.info("Hard Refresh The Page")
            
