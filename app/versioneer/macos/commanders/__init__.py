from app.versioneer.macos.commanders.docker import docker_command
from app.versioneer.macos.commanders.google import google_command

SOFT_REGISTRY = {
    'Mattermost': None,
    'Google Chrome': google_command,
    'PyCharm': None,
    'DBeaver': None,
    'Docker': docker_command,
    'OpenVPN Connect': None,
    'Sublime Text': None,
}

__all__ = [
    'SOFT_REGISTRY'
]
