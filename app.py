import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Alex IA", page_icon="🤖")

st.title("🤖 Alex IA")

api_key = st.text_input("Digite sua chave da OpenAI:", type="password")

if api_key:
    try:
        client = OpenAI(api_key=api_key)

        pergunta = st.text_input("Pergunte alguma coisa:")

        if st.button("Enviar") and pergunta:
            resposta = client.responses.create(
                model="gpt-5-mini",
                input=pergunta
            )

            st.write(resposta.output_text)

    except Exception as e:
        st.error(f"Erro: {e}")
