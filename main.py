import streamlit as st
import google.generativeai as genai

# --- CONFIG ---
API_KEY = "AIzaSyDeSWaFrB8wc0Bp2sKKKQmEsvqKvun7ZHM" # <--- Yahan apni key dalo
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Viro AI", layout="centered")

# --- STYLE ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .stButton>button { background-color: #00FFCC; color: black; border-radius: 10px; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("Viro AI")

# --- UI ---
file = st.file_uploader("Upload your Reel/Video", type=['mp4', 'mov'])

if file:
    st.video(file)
    if st.button("AUDIT VIDEO"):
        st.balloons()
        st.success("AI is analyzing your video... Please wait.")
      
