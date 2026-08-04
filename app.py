import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Alex IA", page_icon="🤖")

st.title("🤖 Alex IA")
st.write("Sua IA usando Google Gemini")

api_key = st.text_input(
    "Digite sua chave da API Gemini:",
    type="password"
)

if api_key:
    genai.configure(api_key=api_key)

    pergunta = st.text_input("Pergunte alguma coisa:")

    if st.button("Enviar") and pergunta:
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")

            resposta = model.generate_content(pergunta)

            st.success(resposta.text)

        except Exception as e:
            st.error(e)
