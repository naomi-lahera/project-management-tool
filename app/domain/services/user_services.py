from ...infrastructure.users_repositories import UserRepository
from ...utils.utils import Errors, _generate_id_from_field
from ..entities import UserEntity
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
from datetime import datetime, timedelta, timezone
import jwt

class UserService():
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    def register_user(self, username, email, password):
        user: UserEntity = self.repository.get_by_email(email)
        
        if user:
            return None, Errors.already_exists.value
        
        user = UserEntity(_generate_id_from_field(email), username, email, generate_password_hash(password))
       
        user = self.repository.add_user(user)
        
        print(user.name)
        current_app.logger.info(f"{user.name}")
        
        return user, 'OK'
    
    def login_user(self, email, pwd_str):
        user: UserEntity = self.repository.get_by_email(email)
        
        if not user:
            return None, Errors.doesnt_exist.value
        
        current_app.logger.info(f"Check password hash: {check_password_hash(user.pwd, pwd_str)}")
        current_app.logger.info(f"Check password hash: {user.pwd}")
        current_app.logger.info(f"Check password hash: {pwd_str}")
        
        if not check_password_hash(user.pwd, pwd_str):
            return None, Errors.conflict.value
        
        payload = {
            "user_id": user.id,
            "user_email": user.email,
            "exp": datetime.now(timezone.utc) + timedelta(hours=1)
        }
        token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm="HS256")
        
        return token, 'OK'
    
    def get_by_email(self, email):
        return self.repository.get_by_email(email)