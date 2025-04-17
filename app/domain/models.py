from ..extensions import db
from .entities import TaskStatus, TaskPriority

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    
    user_projects = db.relationship("UserProjectModel", back_populates="user")
    
class TaskModel(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(200), nullable=False, index=True)
    status = db.Column(db.Enum(TaskStatus), default=TaskStatus.PENDING)
    priority = db.Column(db.Enum(TaskPriority), default=TaskPriority.MEDIUM)
    
    # project_id = db.Column(db.String, db.ForeignKey('projects.id'), nullable=False)
    # user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)

    # project = db.relationship("ProjectModel", backref="tasks")
    # user = db.relationship("UserModel", backref="tasks")
    
class ProjectModel(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False, index=True)
    description = db.Column(db.String(200), nullable=False, index=True)
    archivated = db.Column(db.Boolean, default=False)
    
    user_projects = db.relationship("UserProjectModel", back_populates="project")
    
class UserProjectModel(db.Model):
    __tablename__ = 'user_project'
    user_id = db.Column(db.String, db.ForeignKey('users.id'), primary_key=True)
    project_id = db.Column(db.String, db.ForeignKey('projects.id'), primary_key=True)
    archivated = db.Column(db.Boolean, default=False) #TODO Quitar este campo
    boss = db.Column(db.Boolean, default=False)

    user = db.relationship("UserModel", back_populates="user_projects")
    project = db.relationship("ProjectModel", back_populates="user_projects")
    