from abc import ABC, abstractmethod
from typing import Dict, Optional


class BaseVersioneer(ABC):
    @abstractmethod
    def get_version_info(self, app_name: str) -> Optional[Dict[str, str]]:
        ...
