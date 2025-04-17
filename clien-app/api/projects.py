import streamlit as st
from models.models import User, Project
import requests

BASE_URL = st.session_state["BASE_URL"]

def get_all():
    user: User = st.session_state["user"]
    
    return [Project("Project 1", "Descripcion del primer proyecto", False)]

def create(name, description):
    return True

def delete_project(project_id, token):
    url = f"{BASE_URL}/projects/{project_id}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.delete(url, headers=headers)
    return response.status_code == 204
