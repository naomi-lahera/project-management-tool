from ..domain.models import UserProjectModel
from ..domain.entities import UserEntity, ProjectEntity

class UserProjectRepository:
    def __init__(self):
        pass
    
    def is_owner(self, user: UserEntity, project: ProjectEntity) -> bool:
        project = UserProjectModel.query.filter(UserProjectModel.user_id == user.id, UserProjectModel.project_id == project.id, UserProjectModel.boss).first()
        
        return project is not None