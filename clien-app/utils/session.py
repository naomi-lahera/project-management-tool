import streamlit as st

def init_session():
    st.session_state["BASE_URL"] = "http://127.0.0.1:5000"
    if not "user" in st.session_state:
        st.session_state["user"] = None
    if not "projects" in st.session_state:
        st.session_state["projects"] = None
    if not "tasks" in st.session_state:
        st.session_state["tasks"] = None
    
def login_user(user):
    st.session_state["user"] = user
    
def save_projects(projects):
    st.session_state["projects"] = projects