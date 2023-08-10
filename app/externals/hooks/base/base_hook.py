from abc import ABC, abstractmethod
from typing import List, Any, Dict


class BaseHook(ABC):

    name: str

    @abstractmethod
    def execute(self, query: str, params: Dict[str, Any]) -> Any:
        ...

    @abstractmethod
    def connect(self) -> Any:
        ...
