import re
from typing import Dict

from app.utils.exceptions import VersionNotFound
from app.versioneer.utils import subprocess_run

command = '/Applications/"Pycharm.app"/Contents/MacOS/"Pycharm" --version'
pattern = re.compile(
    r"PyCharm (?P<version>[0-9\.]+) \((Professional Edition|Community Edition)\)\sBuild #PY-(?P<build>[0-9\.-]+)"
).search


def pycharm_command(soft: str) -> Dict[str, str]:
    raw_version: str = subprocess_run(command)
    matched = pattern(raw_version)
    if matched:
        return {"version": matched.group("version"), "build": matched.group("build")}

    raise VersionNotFound(f"Version not found in {soft}")
