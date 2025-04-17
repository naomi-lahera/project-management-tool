import streamlit as st
from models.models import User

BASE_URL = st.session_state["BASE_URL"]

def register(username, email, password):
    return True

def login(email, password):
    return User("Leiliana", "lei@gmail.com", "fvgbhjnjmlk,sxdcfvghjntrytuyukillçk,mnbvcxcfghj,k")