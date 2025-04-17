from ..entities import TaskEntity
from ...domain.entities import TaskStatus, TaskPriority
from ...infrastructure.tasks_repository import TaskRepository
from ...infrastructure.projects_repository import ProjectRepository
from ...infrastructure.users_repositories import UserRepository
from ...infrastructure.project_user_repository import UserProjectRepository
from ...utils.utils import _generate_id_from_field, Errors

class TaskService:
    def __init__(self, task_repository: TaskRepository): # , user_repository, project_repository, user_project_repository
        self.task_repository: TaskRepository = task_repository
        # self.project_repository: ProjectRepository = project_repository
        # self.user_repository: UserRepository = user_repository
        # self.user_project_repository: UserProjectRepository = user_project_repository
        
    def create_task(self, name, status, priority, project_manager_email, project_name):
        # user = self.user_repository.get_by_email(project_manager_email)
        # project = self.project_repository.find_by_name(project_name)
        
        # if not user or not project:
        #     return None, Errors.doesnt_exist.value
        
        # if not self.user_project_repository.is_owner(user, project):
        #     return None, Errors.conflict.value
        
        
        # if not status: status = TaskStatus.PENDING
        # if not priority: priority = TaskPriority.HIGH
        
        # task = TaskEntity(_generate_id_from_field(name), name, status, priority)
        # self.repository.add_task(task)
        
        # return task, 201
        
        return None, 'OK'
    
    def update_task(self, task: TaskEntity) -> TaskEntity:
        pass
    
    def delete_task(self, task_id: str) -> TaskEntity:
        pass