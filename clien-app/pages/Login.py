import streamlit as st
from utils.session import init_session, login_user
from api.user import login
from models.models import User

st.set_page_config(page_title="Log In", page_icon="🔑")
st.title("Log In")

init_session()

if st.session_state["user"]:
    st.success("Done")
    st.page_link("pages/Projects.py", label="Go to your projects", icon="📁")
else:
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Log In"):
        user: User = login(email, password)
        if user:
            login_user(user)
            
            print(st.session_state["user"].username)
            
            st.success("Login successful!")
            st.switch_page("pages/Projects.py")
        else:
            st.error("Incorrect username or password.")
