import streamlit as st
from google import genai

st.set_page_config(page_title="Alex IA", page_icon="🤖")

st.title("🤖 Alex IA")

api_key = st.text_input("Digite sua chave da API Gemini:", type="password")

if api_key:
    try:
        cliente = genai.Client(api_key=api_key)

        pergunta = st.text_input("Pergunte alguma coisa:")

        if st.button("Enviar") and pergunta:
            resposta = cliente.models.generate_content(
                model="gemini-2.5-flash",
                contents=pergunta
            )
            st.write(resposta.text)

    except Exception as e:
        st.error(f"Erro: {e}")
