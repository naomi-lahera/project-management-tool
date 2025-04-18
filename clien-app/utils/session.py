import streamlit as st
from enum import Enum 

def init_session():
    st.session_state["BASE_URL"] = "http://127.0.0.1:5000"
    if not "user" in st.session_state:
        st.session_state["user"] = None
    if not "projects" in st.session_state:
        st.session_state["projects"] = None
    if not "tasks" in st.session_state:
        st.session_state["tasks"] = None
    
def login_session(user):
    st.session_state["user"] = user
    
def save_projects(projects):
    st.session_state["projects"] = projects
    
class Errors(Enum):
    server_error = "Server error."
    login_fail = "Login failed. Incorrect user or email"
    singup_fail = "Registration failed. Try another username or email"
    already_exists = "Already exists"
    unauthorized = "Unauthorized. Invalid token"