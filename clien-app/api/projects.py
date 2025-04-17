import streamlit as st
from models.models import User, Project

BASE_URL = st.session_state["BASE_URL"]

def get_all():
    user: User = st.session_state["user"]
    
    return [Project("Project 1", "Descripcion del primer proyecto", False)]

def create(name, description):
    return True