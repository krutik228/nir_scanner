from typing import Dict, Callable, Optional

from app.versioneer.base.base_versioneer import BaseVersioneer

from app.versioneer.macos.commanders import SOFT_REGISTRY


class MacOsVersioneer(BaseVersioneer):
    def get_version_info(self, app_name) -> Optional[Dict[str, str]]:
        if SOFT_REGISTRY.get(app_name):
            command: Callable = SOFT_REGISTRY[app_name]
            params: Dict[str, str] = command(app_name)
            self._adapt_params(params)
            return params

    @staticmethod
    def _adapt_params(params: Dict[str, str]) -> Dict[str, str]:
        params['os'] = 'MacOs'
        version = params.get('version')
        if version:
            params['version'] = version.replace('-', '.')
        return params

