import streamlit as st
from api.user import register

st.title("Register")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    success = register(username, email, password)
    if success:
        st.success("Registration successful! You can now log in.")
    else:
        st.error("Registration failed. Try another username or email.")
