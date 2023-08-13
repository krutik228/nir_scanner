import re
from typing import Dict

from app.utils.exceptions import VersionNotFound
from app.versioneer.utils import subprocess_run

command = '/Applications/"OpenVPN Connect.app"/Contents/MacOS/"OpenVPN Connect" --version'
pattern = re.compile(r'"build-number": "(?P<build>[0-9]+)",\s+"version": "(?P<version>[0-9\.]+)"').search


def openvpn_connect_command(soft: str) -> Dict[str, str]:
    raw_version: str = subprocess_run(command)
    matched = pattern(raw_version)
    if matched:
        return {'version': matched.group('version'), 'build': matched.group('build')}

    raise VersionNotFound(f'Version not found for {soft}')
