from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List

from app.detector.base import BaseDetector
from app.detector.queries import QUERIES
from app.externals.hooks import BaseHook


class Detector(BaseDetector):
    def __init__(self, hook: BaseHook):
        self.hook = hook
        self.hook_name = hook.name

    def detect(self, soft: str, params: Dict[str, Any]) -> List[Any]:
        self.hook.connect()

        if not QUERIES.get(soft):
            return []

        cves = self.hook.execute(query=QUERIES[soft][self.hook_name], params=params)
        return cves

    @staticmethod
    def _adapt_query_result(self):
        pass
