import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")

# API Setup
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key Missing!")
    st.stop()

# Caching Function (Quota Bachane ke liye)
@st.cache_resource
def analyze_video(video_file, prompt_text):
    # SPECIFIC VERSION jo teri list mein tha
    model = genai.GenerativeModel('gemini-2.0-flash-001') 
    
    with st.spinner("AI video dekh raha hai..."):
        # Uploading
        with open("temp_video.mp4", "wb") as f:
            f.write(video_file.getbuffer())
        
        myfile = genai.upload_file("temp_video.mp4")
        
        # Processing wait loop
        while myfile.state.name == "PROCESSING":
            time.sleep(2)
            myfile = genai.get_file(myfile.name)
            
    # Content Generation
    result = model.generate_content([myfile, prompt_text])
    return result.text

video_input = st.file_uploader("Upload Video", type=['mp4', 'mov'])

if video_input:
    st.video(video_input)
    
    if st.button("RUN VIRAL AUDIT"):
        try:
            report = analyze_video(video_input, "Give 3 viral tips for this video.")
            st.subheader("Audit Result")
            st.write(report)
            st.balloons()
            
        except Exception as e:
            # Agar ab bhi error aaye, toh error padhenge
            st.error(f"Error: {e}")
            st.info("💡 Agar 'Quota' error aaye, toh Nayi API Key bana lena.")
            
