from enum import Enum
import hashlib

class Errors(Enum):
    already_exists = 0
    
def _generate_id_from_email(self, email) -> str:
    return hashlib.sha256(email.encode()).hexdigest()