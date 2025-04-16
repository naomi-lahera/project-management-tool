from ..domain.entities import TaskEntity
from .CRUD_db import CRUD

class TaskRepository(CRUD):
    def __init__(self):
        pass
    
    def add_task(self, task: TaskEntity) -> TaskEntity:
        self.add(task)