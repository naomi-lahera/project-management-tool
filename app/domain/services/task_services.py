from ..entities import TaskEntity

class TaskService:
    def __init__(self, repository):
        self.repository = repository
        
    def add_task(self, task: TaskEntity) -> TaskEntity:
        pass
    
    def update_task(self, task: TaskEntity) -> TaskEntity:
        pass
    
    def delete_task(self, task_id: str) -> TaskEntity:
        pass