import streamlit as st
from utils.session import init_session

init_session()

st.set_page_config(page_title="Project Management", page_icon="✅")

st.title("Welcome to the Project Management Tool!")

