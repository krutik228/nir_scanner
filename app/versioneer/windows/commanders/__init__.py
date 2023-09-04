from typing import Callable, Dict, Optional

from .openvpn import openvpn_command


GET_VERSION_COMMAND = Optional[Callable[[str], Dict[str, str]]]

SOFT_REGISTRY: Dict[str, GET_VERSION_COMMAND] = {
    "OpenVPN": openvpn_command,
}

__all__ = ['SOFT_REGISTRY']
