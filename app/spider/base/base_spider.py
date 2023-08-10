from abc import ABC, abstractmethod
from typing import List


class BaseSpider(ABC):
    def __init__(self):
        self._soft_set = set()

    @abstractmethod
    def parse(self) -> List[str]:
        ...

    def get_all_soft(self) -> List[str]:
        return list(self._soft_set)
