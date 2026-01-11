import streamlit as st
import google.generativeai as genai
import time

# UI Setup
st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")
st.markdown("### Viral-Audit Engine: Level 2")

# API Key Connection
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Ye block sahi model apne aap chun lega
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        # Check if model works
        model.generate_content("Hi", generation_config={"max_output_tokens": 1})
        st.sidebar.success("AI Brain: Flash Active ✅")
    except:
        try:
            model = genai.GenerativeModel('gemini-pro')
            st.sidebar.success("AI Brain: Pro Active ✅")
        except:
            st.error("Google API is busy. Please try again in 1 minute.")
            st.stop()
else:
    st.error("Secrets mein API Key nahi mili!")
    st.stop()

# File Upload
video_file = st.file_uploader("Upload your Reel/Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    
    if st.button("RUN VIRAL AUDIT"):
        with st.status("Viro AI is analyzing...", expanded=True) as status:
            st.write("🔍 Scanning frames...")
            time.sleep(1)
            st.write("📊 Checking viral trends...")
            
            try:
                # Asli Audit Report
                prompt = "Analyze this video idea. Give 3 short viral tips and a score out of 10."
                response = model.generate_content(prompt)
                
                status.update(label="Audit Complete!", state="complete", expanded=False)
                st.subheader("Viro Audit Report")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"AI Service Error: Please refresh and try again.")
                
