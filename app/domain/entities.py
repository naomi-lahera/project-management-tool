from enum import Enum

class Entity:
    def __init__(self, id):
        self.id = id

class UserEntity(Entity):
    def __init__(self, id, name, email, pwd):
        super().__init__(id)
        self.name = name
        self.email = email
        self.pwd = pwd
        
    def to_dict(self):
        return {
            "username": self.name,
            "email": self.email
        }
        
class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class TaskPriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TaskEntity(Entity):
    def __init__(self, id, name, status, priority):
        super().__init__(id)
        self.name = name
        self.status = status
        self.priority = priority
        
    def to_dict(self):
        return {
            "name": self.name,
            "status": self.status,
            "priority": self.priority
        }
        
