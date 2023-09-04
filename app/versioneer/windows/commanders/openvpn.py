import re
from typing import Dict

from app.utils.exceptions import VersionNotFound
from app.versioneer.utils import powershell_subprocess_run

command = (
    r'$OpenVPN = Get-ChildItem -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",'
    r'"HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall" '
    r'| Get-ItemProperty | Where-Object {$_.DisplayName -match "OpenVPN" } '
    r'| Select-Object -Property DisplayName, DisplayVersion, PSChildName; $OpenVPN.DisplayVersion'
)
pattern = re.compile(r'(?P<version>[0-9\.]+)').match


def openvpn_command(soft: str) -> Dict[str, str]:
    raw_version: str = powershell_subprocess_run(command)
    matched = pattern(raw_version)
    if matched:
        return {"version": matched.group("version")}

    raise VersionNotFound(f"Version not found for {soft}")
