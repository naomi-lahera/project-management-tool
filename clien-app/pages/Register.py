import streamlit as st
from api.user import register_api
from utils.session import reset_session

st.set_page_config(page_title="Register", page_icon="📝")
st.title("Register")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    success, msg = register_api(username, email, password)
    if success:
        st.success("Registration successful! You can now log in.")
        reset_session()
        st.switch_page("pages/Login.py")
    else:
        st.error(msg)
