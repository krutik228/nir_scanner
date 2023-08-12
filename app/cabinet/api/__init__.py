from typing import Type

from flask import Flask

from .base_bp import bp as base_bp
from .routes import register_route
from ...config import Config
from ...utils.json import init_flask_json_encoder

register_route(base_bp)


def create_app(config: Type[Config]) -> Flask:
    app = Flask(__name__, static_folder=None)
    app.config.from_object(config)

    add_blueprints(app)
    init_flask_json_encoder(app)
    return app


def add_blueprints(app: Flask) -> None:
    app.register_blueprint(base_bp)
