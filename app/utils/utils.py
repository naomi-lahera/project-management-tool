from enum import Enum
import hashlib

class Errors(Enum):
    already_exists = 409 # Conflict
    
def _generate_id_from_email(email) -> str:
    return hashlib.sha256(email.encode()).hexdigest()