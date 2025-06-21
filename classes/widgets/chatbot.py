import streamlit as st
import pandas as pd
from classes.data.apiconnection import ApiConnection
from classes.models.linearregression import Model
from classes.ui.footer import Footer
import traceback


def is_valid_number(text):
    """Validates if the string represents a positive float number."""
    try:
        value = float(text.replace(",", "."))
        return value > 0
    except ValueError:
        return False


def chatbot():
    # Initializes the chat history
    if "message_list" not in st.session_state:
        st.session_state["message_list"] = []

    # Button to clean the chat history
    if st.button("🧹 Limpar conversa"):
        st.session_state["message_list"] = []
        st.rerun()

    # User's input
    prompt = st.chat_input(placeholder="Qual o diâmetro da pizza?")

    if prompt:
        # Greeting
        st.chat_message("assistant").write("Olá! Me chamo Gregor, modelo de Machine Learning capaz de prever o preço de uma pizza com base no diâmetro.")
        # Adds the user input to the chat history
        st.session_state["message_list"].append({"role": "user", "content": prompt})

        if is_valid_number(prompt):
            try:
                # Shows previous chat history
                for msg in st.session_state["message_list"]:
                    st.chat_message(msg["role"]).write(msg["content"])

                diametro = float(prompt.replace(",", "."))

                # Entry data for prediction
                new_data = pd.DataFrame({"diametro": [diametro]})

                # Loads data and prepares the model
                df = ApiConnection.get_data()
                model_chat = Model()
                model_chat.get_data(df, target_column="preco")
                model_chat.train_model()

                # Makes the prediction and corrects the result properly
                predicted_price = float(model_chat.predict(new_data)[0])

                answer = (
                    f"Para uma pizza com **{diametro:.1f} cm**, "
                    f"o preço estimado é **R$ {predicted_price:.2f}**."
                )

            except Exception:
                st.error("Erro inesperado:\n\n" + traceback.format_exc())
                answer = "⚠️ Ocorreu um erro inesperado ao tentar prever o preço. Por favor, tente novamente."

        else:
            answer = (
                "⚠️ Para prever o preço da pizza, digite um **número positivo** como `30`, `25.5` ou `22,0`."
            )

        # Adds the assistant's answer to the chat history
        st.session_state["message_list"].append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)

    Footer.footer()
