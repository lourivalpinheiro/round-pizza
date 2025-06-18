import streamlit as st
import pandas as pd
from classes.data.apiconnection import ApiConnection
from classes.models.linearregression import Model
from classes.ui.footer import Footer


def chatbot():
    # This list keeps the record of the conversation
    if "message_list" not in st.session_state:
        st.session_state["message_list"] = []

    # # Button to clear the chat
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
            # Shows the chat history
            for msg in st.session_state["message_list"]:
                st.chat_message(msg["role"]).write(msg["content"])

            # Prepares data for prediction
            diameter = float(prompt.replace(",", "."))
            new_data = pd.DataFrame({"diametro": [diameter]})

            # Makes the prediction
            # Loads data and trains the model
            df = ApiConnection.get_data()
            model_chat = Model()
            model_chat.get_data(df, target_column="preco")
            model_chat.train_model()
            predicted_price = model_chat.predict(new_data)[0]

            answer = f"🍕 Para uma pizza com **{diameter:.1f} cm**, o preço estimado é **R$ {predicted_price:.2f}**."


        except ValueError:

            answer = "Para que eu consiga prever o preço, preciso de um **número válido e positivo** como, por exemplo: `30` ou `30.0` (você também pode usar vírgula no lugar do ponto)."

        except Exception as e:

            # Catch other potential errors gracefully

            answer = f"Ocorreu um erro inesperado. Por favor, tente novamente. (Detalhes do erro: {e})"

        # Adds the assistant's answer to the chat history
        st.session_state["message_list"].append({"role": "assistant", "content": answer})

        # Shows the last assistant's message
        st.chat_message("assistant").write(answer)

        Footer.footer()
