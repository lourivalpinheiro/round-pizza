# Importing necessary modules
import streamlit as st
from streamlit_gsheets import GSheetsConnection

class ApiConnection:
    @classmethod
    @st.cache_data
    def get_data(cls):
        conn = st.connection("gsheets", type=GSheetsConnection)
        spreadsheet_data = conn.read(
            spreadsheet=st.secrets["dataset"]["data"]
        )
        return spreadsheet_data