from ..domain.models import UserProjectModel
from ..domain.entities import UserEntity, ProjectEntity
from ..extensions import db
from flask import current_app

class UserProjectRepository:
    def __init__(self):
        pass
    
    def is_owner(self, user: UserEntity, project: ProjectEntity) -> bool:
        current_app.logger.info(f"REPOSITORY User-Project 1 Crear tarea: {user.id}")
        
        project_model = UserProjectModel.query.filter(UserProjectModel.user_id == user.id, UserProjectModel.project_id == project.id, UserProjectModel.boss == True).first()
        
        current_app.logger.info(f"REPOSITORY User-Project 2 Crear tarea: {user.id}")
        
        return project_model is not None
        
        # return True
    
    def exist_by_id(self, user_id, project_id):
        current_app.logger.info(f"REPOSITOY User-Project 1 Crear tarea: {user_id}")
        
        user_project = UserProjectModel.query.filter_by(user_id=user_id, project_id=project_id).first()
        
        current_app.logger.info(f"REPOSITOY User-Project 2 Crear tarea: {user_project.boss}")
        
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