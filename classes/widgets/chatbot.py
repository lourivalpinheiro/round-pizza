import streamlit as st
import pandas as pd
from classes.models.linearregression import Model
from classes.ui.footer import Footer


def chatbot():
    # This list keeps the record of the conversation
    if "message_list" not in st.session_state:
        st.session_state["message_list"] = []

    # Button to clear the chat
    if st.button("Limpar conversa"):
        st.session_state["message_list"] = []
        st.rerun()

    # User's input
    prompt = st.chat_input(placeholder='Qual o diâmetro da pizza?')

    if prompt:
        st.chat_message("assistant").write("Olá! Eu me chamo **Gregor**, algoritmo de **Machine Learning** capaz de prever o preço de uma pizza com base em seu diâmetro. Os preços não necessariamente correspondem à realidade do mercado, pois posso cometer erros.")
        # Adds user's message to the record
        st.session_state["message_list"].append({"role": "user", "content": prompt})

        try:
            # Loads data and trains the model
            path = st.secrets["dataset"]["data"]
            df = pd.read_csv(path)

            model_chat = Model()
            model_chat.get_data(df, target_column="preço")
            model_chat.train_model()

            # Shows the chat history
            for msg in st.session_state["message_list"]:
                st.chat_message(msg["role"]).write(msg["content"])

            # Prepares data for prediction
            diameter = float(prompt.replace(",", "."))
            novo_dado = pd.DataFrame({"diâmetro": [diameter]})

            # Makes the prediction
            predicted_price = model_chat.predict(novo_dado)[0]

            answer = f"🍕 Para uma pizza com **{diameter:.1f} cm**, o preço estimado é **R$ {predicted_price:.2f}**."

        except Exception:
            answer = (
                "Para que eu consiga prever o preço, preciso de um número válido como, por exemplo: 30 ou 30.0 (você também pode usar vírgula no lugar do ponto se quiser)."
            )

        # Adds the assistant's answer to the chat history
        st.session_state["message_list"].append({"role": "assistant", "content": answer})

        # Shows the last assistant's message
        st.chat_message("assistant").write(answer)

        Footer.footer()
