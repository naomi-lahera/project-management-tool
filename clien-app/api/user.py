import streamlit as st

BASE_URL = st.session_state["BASE_URL"]

def register(username, email, password):
    return True