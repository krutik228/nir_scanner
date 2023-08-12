from typing import Any, ContextManager

from gunicorn.workers.sync import SyncWorker


class SyncWorkerWithContextManager(SyncWorker):
    def __init__(
        self, *args: Any, context_manager: ContextManager[None], **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs)
        self.context_manager = context_manager

    def run(self) -> None:
        with self.context_manager:
            super().run()
