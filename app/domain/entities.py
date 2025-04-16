from werkzeug.security import generate_password_hash, check_password_hash

class Entity:
    def __init__(self, id):
        self.id = id

class UserEntity(Entity):
    def __init__(self, id, name, email, pwd):
        super().__init__(id)
        self.name = name
        self.email = email
        self.pwd = pwd
        
