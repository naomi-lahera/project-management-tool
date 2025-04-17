import streamlit as st
from api.projects import get_all, create
from utils.session import save_projects

st.set_page_config(page_title="Projects", page_icon="📁")
st.title("Projects")

user = st.session_state["user"]
projects = st.session_state["projects"]

if not user:
    st.warning("You need to log in first")
    st.page_link("pages/Login.py")
else:
    st.write("Here you can view your projects...")
    with st.sidebar:
        st.header("Create Project")
        project_name = st.text_input("Project Name", key="sidebar_name", placeholder="Enter project name")
        project_description = st.text_input("Description", key="sidebar_description", placeholder="Enter description")

        if st.button("Create", key="sidebar_create"):
            if project_name.strip() and project_description.strip():
                success, msg = create(project_name, project_description)
                if success: st.success(f"Project '{project_name}' created successfully.")
                else: st.error(msg)
            else:
                st.warning("Project name and description are required.")
    
