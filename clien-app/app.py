import streamlit as st
from utils.session import init_session

init_session()

st.set_page_config(page_title="Task Manager", page_icon="✅")
st.title("Welcome to your Task Manager")

user = st.session_state["user"]

if user:
    st.success(f"Hello, {user.username}!")
    st.page_link("pages/Projects.py", label="Go to your projects", icon="📁")
else:
    st.info("New here or already have an account?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Log In 🔐"):
            st.switch_page("pages/Login.py")
    
    with col2:
        if st.button("Register 📝"):
            st.switch_page("pages/Register.py")
