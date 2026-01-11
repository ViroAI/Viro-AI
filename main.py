import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")

# 1. API Key Setup
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key Missing!")
    st.stop()

# 2. Caching Function (Ye hai asli bachat!)
# Ye function yaad rakhega ki is video ka jawab pehle diya tha ya nahi
@st.cache_resource
def analyze_video(video_file, prompt_text):
    # Model: Experimental wala jo fast hai
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Uploading to Gemini
    with st.spinner("Uploading video to AI brain... (Free account, thoda time lagega)"):
        # Temporary file save karni padti hai upload ke liye
        with open("temp_video.mp4", "wb") as f:
            f.write(video_file.getbuffer())
        
        myfile = genai.upload_file("temp_video.mp4")
        
        # Wait for processing
        while myfile.state.name == "PROCESSING":
            time.sleep(2)
            myfile = genai.get_file(myfile.name)
            
    # Generating Content
    with st.spinner("Analyzing viral potential..."):
        result = model.generate_content([myfile, prompt_text])
    return result.text

# 3. User Interface
video_input = st.file_uploader("Upload Video", type=['mp4', 'mov'])

if video_input:
    st.video(video_input)
    
    # Button
    if st.button("RUN VIRAL AUDIT"):
        try:
            # Ye function call cache use karega
            report = analyze_video(video_input, "Give 3 viral tips for this video. Be specific.")
            
            st.subheader("Viro Audit Result")
            st.markdown(report)
            st.balloons()
            
        except Exception as e:
            st.error("Quota Over! 10 min ruko ya nayi API Key banao.")
            st.error(f"Error Details: {e}")
            
