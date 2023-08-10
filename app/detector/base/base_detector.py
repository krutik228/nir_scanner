from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List


class BaseDetector(ABC):
    @abstractmethod
    def detect(self, soft: str, params: Dict[str, Any]) -> List[Any]:
        ...
