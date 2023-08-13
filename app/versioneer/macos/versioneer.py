from typing import Dict, Callable

from app.versioneer.base.base_versioneer import BaseVersioneer

from app.versioneer.macos.commanders import SOFT_REGISTRY


class MacOsVersioneer(BaseVersioneer):
    def get_version_info(self, app_name) -> Dict[str, str]:
        if app_name in SOFT_REGISTRY and SOFT_REGISTRY.get(app_name):
            command: Callable = SOFT_REGISTRY.get(app_name)
            version_info = command(app_name)
            return version_info
