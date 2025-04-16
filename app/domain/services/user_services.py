from ...infrastructure.users_repositories import UserRepository
from ...utils.utils import Errors, _generate_id_from_email
from ..entities import UserEntity
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

class UserService():
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    def register_user(self, username, email, password):
        if self.repository.exists(username, email):
            return None, Errors.already_exists.value
        
        user = UserEntity(generate_password_hash(email), username, email, _generate_id_from_email(password))
       
        user = self.repository.add_user(user)
        
        print(user.name)
        current_app.logger.info(f"{user.name}")
        
        return user, 201