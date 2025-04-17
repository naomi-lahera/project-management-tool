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
    
    if not data.get('name') or not data.get('project_name'):
        abort(400, description="Faltan campos requeridos: name or project_name")
                
    try:
        name = data["name"]
        project_name = data["project_name"]
        status = data.get('status', None)
        priority = data.get('priority', None)
        
        current_app.logger.info(f"Tarea creada /create: {name}, {status}, {priority}, {project_name}")
        
        # result, msg = tasks_service.create_task(name, status, priority, g.user_email, project_name)
        # current_app.logger.info(f"Tarea creada /create: {result.name if result else msg}")
        
        # return jsonify(result.to_dict() if result else None), code
        
        return jsonify({"msg": "OK"}), 201
    except:
        return {"msg": "Error"}