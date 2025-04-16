from ..extensions import db
from .entities import TaskStatus, TaskPriority

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    
class TaskModel(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False, index=True)
    status = db.Column(db.Enum(TaskStatus), default=TaskStatus.PENDING)
    priority = db.Column(db.Enum(TaskPriority), default=TaskPriority.HIGH)