import re
import subprocess
from typing import Dict

from app.versioneer.utils import subprocess_run

command = '/Applications/"Google Chrome.app"/Contents/MacOS/"Google Chrome" --version'
pattern = re.compile(r"Google Chrome\s(?P<version>(([0-9]+)\.?)+)").match


def google_command() -> Dict[str, str]:
    raw_version: str = subprocess_run(command)
    matched = pattern(raw_version)
    if not matched:
        return {"version": raw_version}

    return {"version": matched.group("version")}
