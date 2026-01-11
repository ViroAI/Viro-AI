import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Viro AI Debugger", page_icon="🔍")
st.title("Viro AI: Model Finder 🔍")

if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        st.sidebar.success("Connection Check: OK ✅")
        
        # Google ki batayi hui ListModels method
        st.write("### Aapke account ke liye available models:")
        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
                st.code(m.name) # Ye screen par model ka asli naam dikhayega
        
        # Select box taaki hum turant test kar sakein
        selected_model = st.selectbox("Inmein se ek chuno:", available_models)
        
        if st.button("Is Model Ko Test Karo"):
            model_test = genai.GenerativeModel(selected_model)
            response = model_test.generate_content("Hi")
            st.success(f"Success! Model '{selected_model}' kaam kar raha hai.")
            st.write(response.text)
            st.balloons()

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.error("Secrets mein API Key nahi mili!")
    
