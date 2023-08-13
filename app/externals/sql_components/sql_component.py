from abc import abstractmethod, ABC
from typing import List

from app.models import Cve


class SqlDataComponent(ABC):
    @abstractmethod
    def get_sql(self) -> str:
        ...

    @abstractmethod
    def adapt_sql_result(self, raw_rows, soft) -> List[Cve]:
        ...
