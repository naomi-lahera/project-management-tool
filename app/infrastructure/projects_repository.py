from ..domain.models import ProjectModel

class ProjectRepository:
    def __init__(self):
        pass
    
    def create_project(self, user_email, name, description, archived):
        project = ProjectModel(
            name= name,
            description= description,
            archived= archived
            )