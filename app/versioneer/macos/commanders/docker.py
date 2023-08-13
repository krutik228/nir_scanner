import re
from typing import Dict

from app.utils.exceptions import VersionNotFound
from app.versioneer.utils import subprocess_run

command = "docker --version"
pattern = re.compile(
    r"Docker version (?P<version>[0-9\.]+)(, build (?P<build>[a-z0-9]+))?"
).match


def docker_command(soft: str) -> Dict[str, str]:
    raw_version = subprocess_run(command)
    matched = pattern(raw_version)
    if matched:
        return {"version": matched.group("version"), "build": matched.group("build")}

    raise VersionNotFound(f"Version not found for {soft}")
