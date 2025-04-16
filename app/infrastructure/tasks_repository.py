from ..domain.entities import TaskEntity
from .CRUD_db import CRUD
from ..domain.models import TaskModel
from ..extensions import db

class TaskRepository(CRUD):
    def __init__(self):
        pass
    
    def add_task(self, task: TaskEntity) -> TaskEntity:
        task_model = TaskModel(
            id= task.id,
            status= task.status,
            priority= task.priority
        )
        
        db.session.add(task_model)
        db.session.commit()
        return task
        
    def exists(self, name):
        # task = TaskModel.query.filter(TaskModel.name.lower().replace(' ', '') == name.lower().replace(' ', '')).first()
        
        # return task is not None
        
        return False