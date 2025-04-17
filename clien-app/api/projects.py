import streamlit as st
from models.models import User, Project
import requests
from utils.session import Errors

BASE_URL = f'{st.session_state["BASE_URL"]}/projects'

def get_all():
    user: User = st.session_state["user"]
    
    return [Project("Project 1", "Descripcion del primer proyecto", False)]

def create(name, description):
    url = f"{BASE_URL}/create"
    token = st.session_state["user"].token
    headers = {"Authorization": f"Bearer {token}"}
    
    payload= {
        "name": name,
        "description": description
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return True, "OK"
        elif response.status_code == 409:
            return False, Errors.already_exists.value
    except:
        return False, Errors.server_error.value

def delete_project(project_id, token):
    url = f"{BASE_URL}/projects/{project_id}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.delete(url, headers=headers)
    return response.status_code == 204
