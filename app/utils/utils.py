from enum import Enum
import hashlib

class Errors(Enum):
    already_exists = 409 # Conflict
    doesnt_exist = 409 # Conflict
    conflict = 409
    
def _generate_id_from_field(email) -> str:
    return hashlib.sha256(email.encode()).hexdigest()