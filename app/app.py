from flask import Flask
from .extensions import db, migrate
from .controllers.home_controller import home_bp
from .controllers.user_controller import user_bp
from .controllers.tasks_controller import task_bp
from .controllers.project_controller import project_bp
from .domain.models import *

from .infrastructure.users_repositories import UserRepository
from .infrastructure.tasks_repository import TaskRepository
from .infrastructure.projects_repository import ProjectRepository
from .infrastructure.user_project_repository import UserProjectRepository

from .domain.services.user_services import UserService
from .domain.services.task_services import TaskService
from .domain.services.project_service import ProjectService

import os
import logging
from logging import StreamHandler

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects-managment.db'
    app.config['SECRET_KEY'] = 'hgjnlkvfghjnkulukjlmfhgjhjkujiokolp'
    
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configuración básica de logging
    handler = StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    db.init_app(app) 
    migrate.init_app(app, db)
    
    #Inyeccion de dependencias
    user_repository = UserRepository()
    user_service = UserService(repository=user_repository)
    app.user_service = user_service
    
    project_repository = ProjectRepository(user_repository)
    project_service = ProjectService(reposotory=project_repository)
    app.project_service = project_service 
    
    task_repository = TaskRepository()
    user_project_repository = UserProjectRepository()
    task_service = TaskService(
        task_repository=task_repository,
        user_repository=user_repository,
        project_repository=project_repository,
        user_project_repository=user_project_repository
        )
    app.task_service = task_service
     
    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(task_bp, url_prefix= "/tasks")
    app.register_blueprint(project_bp, url_prefix= "/projects")

    return app

if __name__ == '__main__':
    app = create_app()
    app.logger.setLevel("INFO") 
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)