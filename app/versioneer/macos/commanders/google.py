import re
from typing import Dict

from app.utils.exceptions import VersionNotFound
from app.versioneer.utils import subprocess_run

command = '/Applications/"Google Chrome.app"/Contents/MacOS/"Google Chrome" --version'
pattern = re.compile(r"Google Chrome\s(?P<version>(([0-9]+)\.?)+)").match


def google_command(soft: str) -> Dict[str, str]:
    raw_version: str = subprocess_run(command)
    matched = pattern(raw_version)
    if matched:
        return {"version": matched.group("version")}

    raise VersionNotFound(f'Version not found for {soft}')
