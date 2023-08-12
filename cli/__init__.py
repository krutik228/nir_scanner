import click

from cli.cabinet import cabinet


@click.group()
def entrypoint() -> None:
    pass


entrypoint.add_command(cabinet)
