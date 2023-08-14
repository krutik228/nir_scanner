from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from app.models import Cve


class BaseDetector(ABC):
    @abstractmethod
    def detect(self, soft: str, params: Optional[Dict[str, str]]) -> List[Cve]:
        ...
