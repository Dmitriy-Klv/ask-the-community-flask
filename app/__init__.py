from flask import Flask
from app.routers.questions import questions_bp
from app.routers.response import response_bp
from config import DevelopmentConfig
from app.extensions import db, migrate
from app import models



def create_app():
    """
    Application factory for initializing the Flask app.
    Registers blueprints and applies configurations.
    """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(questions_bp, url_prefix='/questions')
    app.register_blueprint(response_bp, url_prefix='/responses')

    db.init_app(app)
    migrate.init_app(app, db)

    return app