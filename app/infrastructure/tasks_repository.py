from ..domain.entities import TaskEntity
from .CRUD_db import CRUD
from ..domain.models import TaskModel, UserProjectModel
from ..extensions import db

class TaskRepository():
    def __init__(self):
        pass
    
    def create_task(self, task_id, user_id, project_id, task_name, status, priority):
        new_task = TaskModel(
            id=task_id,
            name=task_name,
            status=status,
            priority=priority,
            user_id=user_id,
            project_id=project_id
        )

        db.session.add(new_task)
        db.session.commit()
        return new_task
        
    # def exists(self, name):
    #     # task = TaskModel.query.filter(TaskModel.name.lower().replace(' ', '') == name.lower().replace(' ', '')).first()
        
    #     # return task is not None
        
    #     return False