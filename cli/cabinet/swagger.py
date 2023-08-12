import click

from app.cabinet.api import create_app, add_blueprints
from app.cabinet.api.consts import DOC_PREFIX
from app.config import Config
from app.utils.gunicorn import GunicornServer
from app.cabinet.api.swagger import swagger

SWAGGER_PROBES_URL_PREFIX = DOC_PREFIX
API_METRICS_URL_PREFIX = DOC_PREFIX


@click.command("swagger", help=f"start swagger for cabinet on {DOC_PREFIX} endpoint")
def run_swagger() -> None:
    app = create_app(Config)

    swagger.register(app)
    server = GunicornServer(app)
    server.run()
