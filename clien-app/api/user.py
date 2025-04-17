import streamlit as st
from models.models import User
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