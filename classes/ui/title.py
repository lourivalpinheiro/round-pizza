# Importing necessary modules
import streamlit as st 

# Titles
class Title:
    def __init__(self, title: str):
        st.title(title)
        self.title = title