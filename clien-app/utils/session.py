import streamlit as st

def init_session():
    st.session_state["BASE_URL"] = "http://127.0.0.1:5000"
    st.session_state["user"] = None