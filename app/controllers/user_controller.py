from ..domain.services.user_services import UserService
from ..domain.entities import UserEntity
from flask import Blueprint, request, jsonify, abort, current_app
from ..utils.utils import Errors

user_bp = Blueprint('user_api', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    # Servicio del usuario
    user_service: UserService = current_app.user_service

    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        abort(400, description="Faltan campos requeridos: username, email, password.")
    try:
        # 👀        
        result, code = user_service.register_user(data['username'], data['email'], data['password'])
        current_app.logger.info(f"Usuario creado /register: {result.name if result else code}")
        
        return jsonify(result.to_dict() if result else result), code
    except ValueError as e:
    #     abort(409, description=str(e)) # 409 Conflict
    # except Exception as e:
    #     # Log 'e'
    #     abort(500)
        return {"msg": "Error"}