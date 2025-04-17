from ...infrastructure.projects_repository import ProjectRepository
from ...domain.entities import ProjectEntity
from ...utils.utils import Errors
from ...utils.utils import _generate_id_from_field
from flask import current_app

class ProjectService:
    def __init__(self, reposotory):
        self.repository: ProjectRepository = reposotory
       
    def create_project(self, user_email, name, description, archived):
        current_app.logger.info(f"SERVICE Usuario creando proycto: {user_email}")
        
        project = self.repository.find_by_name(name)
        
        current_app.logger.info(f"SERVICE 1 Usuario creando proycto: {project.name if project else None}")
        
        if project:
            return None, Errors.already_exists.value
        
        project = self.repository.create_project(user_email, ProjectEntity(_generate_id_from_field(name), name, description, archived))
        current_app.logger.info(f"SERVICE 2 Usuario creado proycto: {project.name if project else None}")
        
        return project, 'OK'