from flask import Flask
from extensions import db
# from flask_sqlalchemy import SQLAlchemy
from controllers.user_controller import user_bp

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects-managment.db'
# db = SQLAlchemy(app)
# app.register_blueprint(user_bp)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects-managment.db'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # inicializas aquí, no antes

    app.register_blueprint(user_bp, url_prefix="/users")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)