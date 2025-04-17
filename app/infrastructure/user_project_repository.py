from ..domain.models import UserProjectModel
from ..domain.entities import UserEntity, ProjectEntity
from ..extensions import db

class UserProjectRepository:
    def __init__(self):
        pass
    
    def is_owner(self, user: UserEntity, project: ProjectEntity) -> bool:
        project = UserProjectModel.query.filter(UserProjectModel.user_id == user.id, UserProjectModel.project_id == project.id, UserProjectModel.boss).first()
        
        return project is not None
    
    def exist_by_id(self, user_id, project_id):
        user_project = UserProjectModel.query.filter_by(user_id=user_id, project_id=project_id).first()
        
        return user_project is not None
    
    def link(self, user, project):
        user_project = UserProjectModel(
            user_id=user.id,
            project_id=project.id,
            archivated =False,
            boss=False
        )
        
        db.session.add(user_project)
        db.session.commit()