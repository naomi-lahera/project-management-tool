from ..extensions import db
from .CRUD_db import CRUD
from ..domain.models import UserModel
from ..domain.entities import UserEntity
from sqlalchemy import or_

#class UserRepository(CRUD):
class UserRepository():
    def __init__(self):
        super().__init__()
    
    def add_user(self, user: UserEntity) -> UserEntity:
        user_model = UserModel(
            id=user.id, 
            username=user.name,
            email=user.email,
            password_hash=user.pwd
        )
        
        db.session.add(user_model)
        db.session.commit()
        
        # new_user = UserModel.query.filter(UserModel.username == user_model.email).first()
        # return UserEntity(new_user.id , new_user.username, new_user.email, new_user.password) if new_user is not None else None
        
        return user

        
    def exists(self, username, email) -> bool:
        user = UserModel.query.filter(or_(UserModel.username == username, UserModel.email == email)).first()
        
        return user is not None
        