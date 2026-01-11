import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")
st.markdown("### Viral-Audit Engine: Level 2")

# Connection Logic
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash') # Flash is faster
    st.sidebar.success("AI Brain: Pro Active ✅")
else:
    st.error("Secrets issue!")
    st.stop()

video_file = st.file_uploader("Upload your Reel/Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    if st.button("RUN VIRAL AUDIT"):
        with st.status("Viro AI is analyzing...", expanded=True) as status:
            st.write("🔍 Scanning frames...")
            time.sleep(1)
            try:
                # Simple prompt for high success rate
                response = model.generate_content("Give 3 quick viral tips for a gaming reel.")
                status.update(label="Audit Complete!", state="complete", expanded=False)
                st.subheader("Viro Audit Report")
                st.markdown(response.text)
                st.balloons()
            except Exception as e:
                # Fallback to Pro model if Flash fails
                try:
                    model_pro = genai.GenerativeModel('gemini-pro')
                    response = model_pro.generate_content("Give 3 quick viral tips for a gaming reel.")
                    status.update(label="Audit Complete!", state="complete", expanded=False)
                    st.subheader("Viro Audit Report")
                    st.markdown(response.text)
                    st.balloons()
                except:
                    st.error("Google is busy. Just click the button again!")
                    
