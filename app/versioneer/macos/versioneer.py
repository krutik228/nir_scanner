import os
import subprocess
from typing import Dict, Optional, Any, Callable

from app.versioneer.base.base_versioneer import BaseVersioneer
from app.versioneer.macos.commander import SOFT_VERSION_PARSER
from app.versioneer.macos.consts import COMMAND_TEMPLATE, SOFT_LIST


class MacOsVersioneer(BaseVersioneer):
    def get_version(self, app_name) -> Dict[str, Any]:
        if app_name not in SOFT_VERSION_PARSER:
            return {app_name: None}

        raw_version = subprocess.run(
                SOFT_VERSION_PARSER[app_name]['command'], shell=True, check=True, capture_output=True
        ).stdout.decode()
        parse_function: Callable = SOFT_VERSION_PARSER[app_name]['parser']
        version = parse_function(raw_version) if parse_function else raw_version

        return version

    @staticmethod
    def _normalize_app_name(app_name: str):
        if app_name.endswith('.app'):
            return app_name.replace('.app', '')
