from typing import Dict, Any, List, Optional

from app.detector.base import BaseDetector
from app.detector.sql_components import SQL_COMPONENTS
from app.models import Cve
from app.externals.hooks import BaseHook
from app.externals.sql_components.sql_component import SqlDataComponent


class Detector(BaseDetector):
    def __init__(self, hook: BaseHook):
        self.hook = hook
        self.hook_name = hook.name

    def detect(self, soft: str, params: Optional[Dict[str, str]]) -> List[Cve]:
        self.hook.connect()

        if (
            SQL_COMPONENTS.get(soft)
            and SQL_COMPONENTS[soft].get(self.hook_name)
            and params
        ):
            sql_component: SqlDataComponent = SQL_COMPONENTS[soft][self.hook_name]()
            raw_rows = self.hook.execute(query=sql_component.get_sql(), params=params)
            cves = sql_component.adapt_sql_result(raw_rows, soft)
            return cves

        return []
