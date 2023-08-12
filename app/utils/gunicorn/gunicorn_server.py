from typing import Any, Callable, Optional

from flask import Flask
from gunicorn.app.base import BaseApplication

FlaskFactory = Callable[[], Flask]


class GunicornServer(BaseApplication):
    """
    Start gunicorn server from python

    GunicornServer(my_app, my_options).run()
    """

    def __init__(
        self,
        app: Flask,
        options: Optional[dict[str, Any]] = None,
        worker_class: Optional[str] = None,
    ) -> None:
        self.app = app  # type: Flask

        self.worker_class = worker_class

        if options is None:
            options = {}
        self.options = options

        super().__init__()

    def load_config(self) -> None:
        if self.worker_class:
            self.cfg.settings["worker_class"].value = self.worker_class

        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self) -> Flask:
        return self.get_flask_app()

    def get_flask_app(self) -> Flask:
        return self.app

    def init(self, parser: Any, opts: Any, args: Any) -> Any:
        raise NotImplementedError
