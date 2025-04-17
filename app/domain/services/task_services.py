from ..entities import TaskEntity
from ...domain.entities import TaskStatus, TaskPriority
from ...infrastructure.tasks_repository import TaskRepository
from ...infrastructure.projects_repository import ProjectRepository
from ...infrastructure.users_repositories import UserRepository
from ...infrastructure.user_project_repository import UserProjectRepository
from ...utils.utils import _generate_id_from_field, Errors

class TaskService:
    def __init__(
            self, 
            task_repository: TaskRepository, 
            user_project_repository: UserProjectRepository, 
            user_repository: UserRepository, 
            project_repository: ProjectRepository):
        
        self.task_repository: TaskRepository = task_repository
        self.project_repository: ProjectRepository = project_repository
        self.user_repository: UserRepository = user_repository
        self.user_project_repository: UserProjectRepository = user_project_repository
        
    def create_task(self, name, status, priority, project_manager_email, project_name, asigned_user_email):
        project_manager = self.user_repository.get_by_email(project_manager_email)
        asigned_user = self.user_repository.get_by_email(asigned_user_email)
        project = self.project_repository.find_by_name(project_name)
        
        if not self.user_project_repository.is_owner(project_manager, project):
            return None, Errors.conflict.value
        
        if not project or not asigned_user:
            return None, Errors.doesnt_exist.value
         
        if not self.user_project_repository.exist_by_id(user_id=project_manager.id, project_id=project.id):
            return None, Errors.doesnt_exist.value
        
        if not status: status = TaskStatus.PENDING 
        else: TaskStatus(status)
        if not priority: priority = TaskPriority.HIGH
        else: TaskPriority(priority)
        
        task = self.task_repository.create_task(
            task_id=_generate_id_from_field(name), 
            user_id=asigned_user.id, 
            project_id=project.id, 
            task_name=name, 
            status=status, 
            priority=priority)
        
        return task, 'OK'
    
    def update_task(self, task: TaskEntity) -> TaskEntity:
        pass
    
    def delete_task(self, task_id: str) -> TaskEntity:
        pass