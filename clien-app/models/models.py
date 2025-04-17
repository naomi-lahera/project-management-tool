class User:
    def __init__(self, username: str, email: str, token: str):
        self.username = username
        self.email = email
        self.token = token
        
class Project:
    def __init__(self, name, descriptio, archivated):
        self.name = name
        self.description = descriptio
        self.archivated = archivated