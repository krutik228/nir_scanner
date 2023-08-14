

import re
from typing import Dict

from app.utils.exceptions import VersionNotFound
from app.versioneer.utils import subprocess_run

command = (
    '/Applications/"DBeaver.app"/Contents/MacOS/"DBeaver" --version'
)
pattern = re.compile(r'DBeaver (?P<version>[0-9\.]+)').search


def dbeaver_command(soft: str) -> Dict[str, str]:
    raw_version: str = subprocess_run(command)
    matched = pattern(raw_version)
    if matched:
        return {"version": matched.group("version")}

    raise VersionNotFound(f"Version not found for {soft}")
