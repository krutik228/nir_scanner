from abc import ABC, abstractmethod
from typing import Any, List


class BaseScanner(ABC):
    @abstractmethod
    def scan(self) -> List[Any]:
        ...
