from flask import current_app, Blueprint, request, abort, jsonify
from ..domain.services.task_services import TaskService

task_bp = Blueprint('task_api', __name__)

@task_bp.route('/create', methods=['POST'])
def create_task():
    tasks_service: TaskService = current_app.task_service
    data = request.get_json()
    
    if not data.get('name'):
        abort(400, description="Faltan campos requeridos: name.")
                
    try:
        name = data["name"]
        status = data.get('status', None)
        priority = data.get('priority', None)
        current_app.logger.info(f"Tarea creada /create: {name}, {status}, {priority}")
        
        result, code = tasks_service.create_task(name, status, priority)
        current_app.logger.info(f"Tarea creada /create: {result.name if result else code}")
        
        # return jsonify(result.to_dict() if result else None), code
        
        return jsonify({"msg": "OK"}), 201
    except:
        return {"msg": "Error"}