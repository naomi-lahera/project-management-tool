import streamlit as st
from api.projects import get_all

st.set_page_config(page_title="Projects", page_icon="📁")
st.title("Projects")

user = st.session_state["user"]
projects = st.session_state["projects"]

if not user:
    st.warning("You need to log in first")
    st.switch_page("pages/Login.py")
else:
    pass