import click


from .swagger import run_swagger


@click.group(help="run cabinet services")
def cabinet() -> None:
    pass


cabinet.add_command(run_swagger)

__all__ = ["cabinet"]
