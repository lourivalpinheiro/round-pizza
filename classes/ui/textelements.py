# Importing necessary libraries
import streamlit as st 

# Text elements' class
class TextElement:
    def __init__(self, text: str):
        st.markdown(text)
        self.text = text

    @classmethod
    def write_caption(cls, caption: str):
        st.caption(caption)
