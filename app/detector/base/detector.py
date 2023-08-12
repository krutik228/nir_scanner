from typing import Dict, Any, List

from app.detector.base import BaseDetector
from app.detector.queries import QUERIES
from app.models import Cve
from app.externals.hooks import BaseHook
from app.externals.sql_components.sql_component import SqlDataComponent


class Detector(BaseDetector):
    def __init__(self, hook: BaseHook):
        self.hook = hook
        self.hook_name = hook.name

    def detect(self, soft: str, params: Dict[str, Any]) -> List[Cve]:
        self.hook.connect()

        if QUERIES.get(soft) and QUERIES[soft].get(self.hook_name):
            sql_component: SqlDataComponent = QUERIES[soft][self.hook_name]()
            raw_rows = self.hook.execute(query=sql_component.get_sql(), params=params)
            cves = sql_component.adapt_sql_result(raw_rows)
            return cves

        return []
