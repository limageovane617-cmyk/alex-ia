import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Alex IA", page_icon="🤖")

st.title("🤖 Alex IA")

api_key = st.text_input("Digite sua chave da API Gemini:", type="password")

if api_key:
    genai.configure(api_key=api_key)

    modelo = genai.GenerativeModel("gemini-1.5-flash")

    pergunta = st.text_input("Pergunte alguma coisa:")

    if st.button("Enviar") and pergunta:
        resposta = modelo.generate_content(pergunta)
        st.write(resposta.text)
