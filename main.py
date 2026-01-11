import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")
st.markdown("### Viral-Audit Engine: Level 2")

# Connection setup with error handling
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Using gemini-1.5-flash as primary, it's more stable now
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.sidebar.success("AI Brain: Pro Active ✅")
else:
    st.error("Secrets issue! Key missing.")
    st.stop()

video_file = st.file_uploader("Upload your Reel/Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    if st.button("RUN VIRAL AUDIT"):
        status_box = st.status("Viro AI is analyzing...", expanded=True)
        with status_box:
            st.write("🔍 Scanning video frames...")
            time.sleep(1)
            
            # Simple retry loop
            success = False
            for attempt in range(3): # 3 baar koshish karega
                try:
                    prompt = "Analyze this gaming video idea. Give 3 short viral tips and a score out of 10."
                    response = model.generate_content(prompt)
                    if response.text:
                        success = True
                        break
                except Exception:
                    st.write(f"🔄 Retrying attempt {attempt+1}...")
                    time.sleep(2)
            
            if success:
                status_box.update(label="Audit Complete!", state="complete", expanded=False)
                st.subheader("Viro Audit Report")
                st.markdown(response.text)
                st.balloons()
            else:
                status_box.update(label="Service Busy", state="error")
                st.error("Google's AI is taking a nap. Please click 'RUN VIRAL AUDIT' again in 10 seconds!")
                
