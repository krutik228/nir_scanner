from abc import ABC, abstractmethod

from app.models import Vulnerability


class BaseScanner(ABC):
    @abstractmethod
    def scan(self) -> Vulnerability:
        ...
