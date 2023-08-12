from abc import ABC, abstractmethod
from typing import Dict, Optional, List, Any


class BaseVersioneer(ABC):
    @abstractmethod
    def get_version_info(self, app_name: str) -> Dict[str, Any]:
        ...
