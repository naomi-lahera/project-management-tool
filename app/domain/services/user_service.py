from ...infrastructure.repositories import UserRepository
from ...utils.utils import Errors, _generate_id_from_email
from ...domain.entities import UserEntity
from werkzeug.security import generate_password_hash, check_password_hash

class UserService():
    def register_user(self, username, email, password):
        if UserRepository.exists(username, email):
            return None, Errors.already_exists.value
        
        user = UserEntity(generate_password_hash(email), username, email, _generate_id_from_email(password))
        user, code = UserRepository.add(user)
        
        return  user, code 