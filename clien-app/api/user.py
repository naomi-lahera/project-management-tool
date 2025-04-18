import streamlit as st
from models.models import User, Project
import requests
from utils.session import Errors

BASE_URL = f'{st.session_state["BASE_URL"]}/users'

def register_api(username, email, password):
    url = f"{BASE_URL}/register"
    payload = {
        "username": username,
        "email": email,
        "password": password
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            # data = response.json()
            return True, "OK"
        else:
            return False, Errors.singup_fail.value
    except:
        return False, Errors.server_error.value

def login_api(email, password):
    url = f"{BASE_URL}/login"
    payload = {
        "email": email,
        "password": password
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            return User(username=data["name"], email=data["email"], token=data["access_token"]), "OK"
        else:
            return None, Errors.login_fail.value
    except:
        return None, Errors.server_error.value
    
def get_all_projects():
    url = f"{BASE_URL}/get_all_projects"
    token = st.session_state["user"].token
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(url, headers=headers)        
        data = response.json()
        projects = data.get("projects", [])
        
        if response.status_code == 200:
            return [Project(proj["name"], proj["description"], proj["archivated"]) for proj in projects] , 'OK'
        elif response.status_code == 401:
            return [] , Errors.unauthorized.value
        else:
            return [], Errors.server_error.value
    except:
        return [] , Errors.server_error.value