# Importing the necessary modules
import streamlit as st
from streamlit_gsheets import GSheetsConnection

class ApiConnection:
    @classmethod
    @st.cache_data
    def get_data(cls):
        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read(spreadsheet=st.secrets["dataset"]["data"]).copy()

        # Converts all likely numerical columns
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].astype(str).str.replace(",", ".").str.strip()
            try:
                df[col] = df[col].astype(float)
            except ValueError:
                pass  # Non-numerical columns will remain as they are.

        return df
