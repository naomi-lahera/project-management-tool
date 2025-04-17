from ...infrastructure.projects_repository import ProjectRepository
from ...utils.utils import Errors

class ProjectService:
    def __init__(self, reposotory):
        self.repository: ProjectRepository = reposotory
       
    def create_project(self, user_email, name, description, archived):
        project = self.repository.find_by_name(name)
        if project:
            return None, Errors.already_exists.value
        
        project = self.repository.create_project(user_email, name, description, archived)
        
        return project