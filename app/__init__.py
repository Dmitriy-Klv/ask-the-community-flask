from flask import Flask

from app import models
from app.extensions import db, migrate
from app.routers.questions import questions_bp
from app.routers.response import response_bp
from config import DevelopmentConfig
from app.routers.category import category_bp


def create_app():
    """
    Application factory for initializing the Flask app.
    Registers blueprints and applies configurations.
    """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(questions_bp, url_prefix="/questions")
    app.register_blueprint(response_bp, url_prefix="/responses")
    app.register_blueprint(category_bp, url_prefix="/categories")


    db.init_app(app)
    migrate.init_app(app, db)

    return app
