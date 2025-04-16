from flask import Flask
from .extensions import db, migrate
from .controllers.home_controller import home_bp
from .controllers.user_controller import user_bp
from .controllers.tasks_controller import task_bp
from .domain import models

from .infrastructure.users_repositories import UserRepository
from .infrastructure.tasks_repository import TaskRepository

from .domain.services.user_services import UserService
from .domain.services.task_services import TaskService

import os
import logging
from logging import StreamHandler

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects-managment.db'
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
    
    task_repository = TaskRepository()
    task_service = TaskService(TaskRepository)
    app.task_service = task_repository
     
    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(task_bp, url_prefix= "/tasks")

    return app

if __name__ == '__main__':
    app = create_app()
    app.logger.setLevel("INFO") 
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)