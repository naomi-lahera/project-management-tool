from ..domain.models import ProjectModel, UserModel, UserProjectModel
from ..domain.entities import ProjectEntity, UserEntity
from ..infrastructure.users_repositories import UserRepository
from ..extensions import db
from flask import current_app

class ProjectRepository:
    def __init__(self, user_repository):
        self.user_repository: UserRepository = user_repository
    
    def create_project(self, user_email, project: ProjectEntity):
        # current_app.logger.info(f"REPOSITORY 1 Usuario creando proyecto: {user_email}")
        
        project_model = ProjectModel(
            id= project.id,
            name= project.name,
            description= project.description,
            archivated= project.archivated
            )
        
        # current_app.logger.info(f"REPOSITORY 2 Usuario creando proyecto: {user_email}")
        
        project_manager: UserEntity = self.user_repository.get_by_email(user_email)
        
        # current_app.logger.info(f"REPOSITORY 3 Usuario creando proyecto: {project_manager.name if project_manager else 'No encuentra al usuario'}")
        
        project_manager_model = UserModel(
            id=project_manager.id, 
            username = project_manager.name,
            email = project_manager.email,
            password_hash=project_manager.pwd
            )
        
        current_app.logger.info(f"REPOSITORY 4 Usuario creando proyecto: {project_manager_model.username}")
        
        link = UserProjectModel(
            user_id = project_manager_model.id,
            project_id = project_model.id,
            archivated = False,
            boss = True
            )
        
        current_app.logger.info(f"REPOSITORY 5 Usuario creando proyecto: {link.boss}")

        db.session.add(project_model)
        db.session.add(link)
        db.session.commit()
        
        return ProjectEntity(project_model.id, project_model.name, project_model.description, project_model.archivated)
    
    def find_by_name(self, name):
        # current_app.logger.info(f"Nombre del proyecto que se esta buscando: {name}")
        
        project_model = ProjectModel.query.filter(ProjectModel.name == name).first()
        # current_app.logger.info(f"Get project by name: {project_model.name if project_model else 'No encuentra al usuario'}")
        return ProjectEntity(project_model.id, project_model.name, project_model.description, project_model.archivated) if project_model else None