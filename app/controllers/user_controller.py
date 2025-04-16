from flask import Blueprint, request, jsonify, abort
from domain.services.user_service import UserService

user_bp = Blueprint('auth_api', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        abort(400, description="Faltan campos requeridos: username, email, password.")
        
    try:
        result, code = UserService.register_user(data['username'], data['email'], data['password'])
        # return jsonify(result), 201
        return jsonify(result), code
    except ValueError as e:
        abort(409, description=str(e)) # 409 Conflict
    except Exception as e:
        # Log 'e'
        abort(500)