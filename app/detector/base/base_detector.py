from abc import ABC, abstractmethod
from typing import Dict, Any, List

from app.models import Cve


class BaseDetector(ABC):
    @abstractmethod
    def detect(self, soft: str, params: Dict[str, Any]) -> List[Cve]:
        ...
