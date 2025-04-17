from flask import current_app, Blueprint, request, jsonify, abort, g
from ..utils.utils import jwt_required

project_bp = Blueprint('project_api',  __name__)

@project_bp.route('/create', methods=['POST'])
@jwt_required
def create_project():
    project_service = current_app.project_service
    data = request.get_data()
    
    if not data or not data.get('name') or not data.get('description'):
        abort(400, description="Missing: name or description.")
    try:
        user_email = g.user_email
        result, msg =  project_service.create_project(user_email, data["name"], data["description"], False)
        
        if not result:
            return jsonify({"msg": msg}), 409
        
        return jsonify(result.to_dict()), 200
    except:
        return jsonify({"mdg": "Error"}), 500