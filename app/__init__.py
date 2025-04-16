from flask import Flask
from extensions import db
from controllers.home_controller import home_bp
from controllers.user_controller import user_bp
from domain import models

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects-managment.db'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app) 
     
    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp, url_prefix="/users")

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)