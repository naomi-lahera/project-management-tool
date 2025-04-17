from ..entities import TaskEntity
from ...domain.entities import TaskStatus, TaskPriority
from ...infrastructure.tasks_repository import TaskRepository
from ...utils.utils import _generate_id_from_field, Errors

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository: TaskRepository = repository
        
    def create_task(self, name, status, priority):
        # if self.repository.exists(name):
        #     return None, Errors.already_exists.value
        
        # if not status: status = TaskStatus.PENDING
        # if not priority: priority = TaskPriority.HIGH
        
        task = TaskEntity(_generate_id_from_field(name), name, status, priority)
        # self.repository.add_task(task)
        
        # return task, 201
        
        return None, 'OK'
    
    def update_task(self, task: TaskEntity) -> TaskEntity:
        pass
    
    def delete_task(self, task_id: str) -> TaskEntity:
        pass