import re

from app.versioneer.utils import subprocess_run

command = 'docker --version'
pattern = re.compile(r'Docker version (?P<version>[0-9\.]+)(, build (?P<build>[a-z0-9]+))?').match


def docker_command():
    raw_version = subprocess_run(command)
    matched = pattern(raw_version)
    if not matched:
        return {}

    return {'version': matched.group('version'), 'build': matched.group('build')}
