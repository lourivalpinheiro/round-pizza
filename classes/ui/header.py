# Importing necessary libraries
import streamlit as st

class Header:
    @classmethod
    def hide_header(cls):
        # Hiding humburguer menu
        hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_st_style, unsafe_allow_html=True)