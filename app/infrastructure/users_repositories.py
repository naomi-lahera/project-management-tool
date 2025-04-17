from ..extensions import db
from ..domain.models import UserModel
from ..domain.entities import UserEntity
from flask import current_app

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
        current_app.logger.info(f"User password hash: {user_model.password_hash}")
        
        db.session.add(user_model)
        db.session.commit()
        
        # new_user = UserModel.query.filter(UserModel.username == user_model.email).first()
        # return UserEntity(new_user.id , new_user.username, new_user.email, new_user.password) if new_user is not None else None
        return user

    # def exists(self, username, email) -> bool:
    #     user = UserModel.query.filter(or_(UserModel.username == username, UserModel.email == email)).first()
        
    #     return user is not None
    
    def get_by_email(self, email):
        user = UserModel.query.filter(UserModel.email == email).first()
        # current_app.logger.info(f"Get User by email: {user.username if user else 'No encuentra al usuario'}")
        
        return None if not user else UserEntity(user.id, user.username, user.email, user.password_hash)