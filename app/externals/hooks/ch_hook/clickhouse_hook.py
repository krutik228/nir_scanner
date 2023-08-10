from typing import Any, Dict, Optional

from clickhouse_driver import Client

from app.externals.hooks.base.base_hook import BaseHook
from app.utils.get_ch_client import get_ch_client


class ClickHouseHook(BaseHook):

    name = 'Clickhouse'

    def __init__(self):
        self.ch_client: Optional[Client] = None

    def connect(self) -> Any:
        self.ch_client = get_ch_client()

    def execute(self, query: str, params: Dict[str, Any]) -> Any:
        if self.ch_client:
            return self.ch_client.execute(query=query, params=params)
