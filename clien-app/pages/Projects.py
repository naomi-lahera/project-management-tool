import streamlit as st
from api.projects import create, archive_project
from api.user import get_all
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
                if success: 
                    st.success(f"Project '{project_name}' created successfully.")
                    projects, _ = get_all()
                    save_projects(projects)
                else: st.error(msg)
            else:
                st.warning("Project name and description are required.")
    
    if not projects:
        projects, msg = get_all()
        save_projects(projects)

    if not projects:
        st.warning(f"Loading projects failed: {msg}")
    else:
        for project in projects:
            with st.expander(f"📁 {project.name}"):
                st.write(f"**Descripción:** {project.description}")
                # st.write(f"**Archivado:** {'Sí' if project.archivated else 'No'}")
    
                # col1, col2, col3, col4 = st.columns(4)
                # with col1:
                #     if st.button(f"✏️ Edit", key=f"edit_{project.name}", disabled=project.archivated):
                #         st.session_state["edit_project"] = project
                #         st.switch_page("pages/editar_proyecto.py")
                # with col2:
                #     if st.button(f"📝 Add task", key=f"add_task_{project.name}", disabled=project.archivated):
                #         st.session_state["add_task_project"] = project
                #         st.switch_page("pages/Add_task.py")
                # with col3:
                #     if st.button(f"➕ Add User", key=f"add_user_{project.name}", disabled=project.archivated):
                #         st.session_state["add_user_project"] = project
                #         st.switch_page("pages/Link.py")
                # with col4:
                #     if not project.archivated:
                #         if st.button("📦 Archive", key=f"archive_{project.name}"):
                #             archive_project(project.name)
                #             st.success(f"Project '{project.name}' archived successfully.")
                #             st.rerun()
                #     else:
                #         st.info("This project is archived.")