from ..domain.services.user_services import UserService
from ..domain.entities import UserEntity
from flask import Blueprint, request, jsonify, abort, current_app, g
from ..utils.utils import Errors
from ..utils.utils import jwt_required

user_bp = Blueprint('user_api', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    user_service: UserService = current_app.user_service

    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        abort(400, description="Missing: username, email or password.")
    try:     
        result, msg = user_service.register_user(data['username'], data['email'], data['password'])
        # current_app.logger.info(f"Usuario creado /register: {result.name if result else msg}")
        return (jsonify({"msg": msg}), 409) if not result else (jsonify(result.to_dict()), 200)
    except ValueError as e:
        abort(500, description=str(e))
    
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_service: UserService = current_app.user_service
    
    if not data or not data.get('email') or not data.get('password'):
        abort(400, description="Email and password required.")
    try:
        user, msg = user_service.get_by_email(email=data['email'])
        token, msg = user_service.login_user(data['email'], data['password'])
        if not token:
            return jsonify({"msg": msg}), 500
        return jsonify({"name": user.name, "email":user.email, "access_token": token}), 200
    except ValueError as e:
        abort(500, description=str(e))
        
@user_bp.route('/get_all_projects', methods=['GET'])
@jwt_required
def get_all():
    user_service: UserService = current_app.user_service
    try:
        projects, msg = user_service.get_all_projects(g.user_email)
        if projects is not None:
            return jsonify({"projects": [proj.to_dict() for proj in projects]}), 200
        else:
            return jsonify({"msg": msg}), 500
    except ValueError as e:
        abort(500, description=str(e))