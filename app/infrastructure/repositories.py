from infrastructure.CRUD_db import CRUD
from domain.models import UserModel

class UserRepository(CRUD):
    def addUser(self):
        pass
    
    def exists(username, email) -> bool:
        user = UserModel.query.filter((UserModel.username == username) | (UserModel.email == email)).first()
        return user is None