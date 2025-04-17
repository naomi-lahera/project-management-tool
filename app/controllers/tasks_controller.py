from flask import current_app, Blueprint, request, abort, jsonify, g
from ..domain.services.task_services import TaskService
from flask import current_app
from ..utils.utils import jwt_required

task_bp = Blueprint('task_api', __name__)

@task_bp.route('/create', methods=['POST'])
@jwt_required
def create_task():
    tasks_service: TaskService = current_app.task_service
    data = request.get_json()
    
    if not data.get('name', None) or not data.get('project_name', None) or not data.get('asigned_user_email', None):
        abort(400, description="Faltan campos requeridos: name or project_name")
                
    try:
        asigned_user_email = data["asigned_user_email"]
        project_name = data["project_name"]
        name = data["name"]
        status = data.get('status', None)
        priority = data.get('priority', None)
        
        current_app.logger.info(f"Tarea creada /create: {name}, {status}, {priority}, {project_name}")
        
        result, msg = tasks_service.create_task(
            name=name,
            status=status,
            priority=priority,
            project_manager_email=g.user_email,
            project_name=project_name,
            asigned_user_email=asigned_user_email
        )
        
        current_app.logger.info(f"Tarea creada /create: {result.name if result else msg}")
        if result:
            return jsonify(result.to_dict() if result else None), 200
        return jsonify({"msg": msg}), 500
    
    except:
        return {"msg": "Error"}, 500