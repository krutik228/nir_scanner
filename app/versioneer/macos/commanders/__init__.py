from typing import Callable, Dict, Type

from app.versioneer.macos.commanders.docker import docker_command
from app.versioneer.macos.commanders.google import google_command
from app.versioneer.macos.commanders.openvpn_connect import openvpn_connect_command
from app.versioneer.macos.commanders.pycharm import pycharm_command

GET_VERSION_COMMAND = Callable[[str], Dict[str, str]]

SOFT_REGISTRY: Dict[str, GET_VERSION_COMMAND] = {
    'Mattermost': None,
    'Google Chrome': google_command,
    'PyCharm': pycharm_command,
    'DBeaver': None,
    'Docker': docker_command,
    'OpenVPN Connect': openvpn_connect_command,
    'Sublime Text': None,
}

__all__ = [
    'SOFT_REGISTRY'
]
