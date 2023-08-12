from flask import Blueprint

from app.cabinet.api.views import scan_system


def register_route(bp: Blueprint) -> None:
    bp.add_url_rule(
        rule=f"/scanner",
        view_func=scan_system,
        methods=["GET"],
    )
