from abc import ABC, abstractmethod
from typing import Any, List

from app.models import Vulnerability


class BaseScanner(ABC):
    @abstractmethod
    def scan(self) -> Vulnerability:
        ...
