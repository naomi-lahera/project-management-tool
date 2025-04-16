from extensions import db
class CRUD:
    def __init__(self):
        pass
    
    def add(self, obj):
        db.session.add(obj)
        db.session.commit()
        return obj
    
    def update(self, obj_id, new_obj):
        pass
    
    def delete(self, obj_id):
        pass