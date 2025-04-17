from enum import Enum
import hashlib

class Errors(Enum):
    already_exists = "A user with that email already exists." # Conflict
    doesnt_exist = "No user with that email exists." # Conflict
    conflict = "Conflict"
    incorrect_pwd = "The password is incorrect."
    
def _generate_id_from_field(email) -> str:
    return hashlib.sha256(email.encode()).hexdigest()