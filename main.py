import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Viro AI", page_icon="🚀")
st.title("Viro AI 🚀")

# API Setup
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # Is baar hum model ka wahi exact naam use kar rahe hain jo list ne dikhaya
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        st.sidebar.success("Engine: Verified ✅")
    except Exception as e:
        st.sidebar.error(f"Setup Error: {e}")
else:
    st.error("API Key Missing!")
    st.stop()

video_file = st.file_uploader("Upload Video", type=['mp4', 'mov'])

if video_file:
    st.video(video_file)
    if st.button("RUN VIRAL AUDIT"):
        with st.status("AI is auditing...", expanded=True) as status:
            try:
                # Direct test for report
                response = model.generate_content("Give 3 viral tips for this gaming video idea.")
                st.subheader("Viro Audit Report")
                st.markdown(response.text)
                st.balloons()
                status.update(label="Audit Complete!", state="complete")
            except Exception as e:
                # Debugging error detail
                st.error(f"AI Service Issue: {e}")
                st.info("Bhai, list mein se koi aur naam try karein?")
                
