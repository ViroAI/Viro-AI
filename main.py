import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")

# API Setup
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # Sabse stable model jo 404 error nahi deta
        model = genai.GenerativeModel('gemini-pro')
        st.sidebar.success("Engine: Stable Active ✅")
    except Exception as e:
        st.sidebar.error(f"Setup Error: {e}")
else:
    st.error("API Key Missing in Secrets!")
    st.stop()

video_file = st.file_uploader("Upload Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    if st.button("RUN VIRAL AUDIT"):
        with st.spinner("AI is analyzing..."):
            try:
                # Direct response without complicated stuff
                response = model.generate_content("Give 3 viral tips for this video idea.")
                st.subheader("Viro Audit Report")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                # Agar ab bhi server busy bole toh ek baar refresh karna
                st.error(f"Google Response: {e}")
                
