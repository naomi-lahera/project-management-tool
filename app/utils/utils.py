from enum import Enum
import hashlib
from flask import current_app
import jwt
from functools import wraps
from flask import request, abort, g
from datetime import datetime

class Errors(Enum):
    already_exists = "Already exists." # Conflict
    doesnt_exist = "Not found." # Conflict
    conflict = "Conflict"
    incorrect_pwd = "The password is incorrect."
    
def _generate_id_from_field(email) -> str:
    return hashlib.sha256(email.encode()).hexdigest()

def jwt_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            abort(401, description="Missing or invalid autorization token.")
        
        token = auth_header.split(" ")[1]
        
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            exp = payload.get("exp")
            if exp and datetime.now().timestamp() > exp:
                abort(401, description="Expired Token.")
            
            g.user_email = payload.get("user_email")
            if g.user_email is None:
                abort(401, description="Invalid Token.")
        except jwt.ExpiredSignatureError:
            abort(401, description="Expired Token.")
        except jwt.InvalidTokenError:
            abort(401, description="Invalid Token.")
        
        return f(*args, **kwargs)
    return decorated_function


