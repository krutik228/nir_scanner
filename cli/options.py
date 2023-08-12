import click

num_workers = click.option(
    "--num_workers", "-w", help="number of workers", default=1, show_default=True
)


app_port = click.option(
    "--app_port",
    type=int,
    show_default=True,
    default=8080,
    help="Specify port on which gunicorn server will be started",
)

timeout = click.option(
    "--timeout", help="maximum request time in seconds", default=30, show_default=True
)
