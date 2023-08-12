from typing import Dict


from app.versioneer.macos.parsers import google_parser

SOFT_VERSION_PARSER: Dict[str, Dict] = {
    "Mattermost": {
        "command": '/Applications/"Mattermost.app"/Contents/MacOS/"Mattermost" --version',
        "parser": None,
    },
    "Google Chrome": {
        "command": '/Applications/"Google Chrome.app"/Contents/MacOS/"Google Chrome" --version',
        "parser": google_parser,
    },
    "PyCharm": {
        "command": '/Applications/"PyCharm.app"/Contents/MacOS/"PyCharm" --version',
        "parser": None,
    },
    "DBeaver": {
        "command": '/Applications/"DBeaver.app"/Contents/MacOS/"DBeaver" --version',
        "parser": None,
    },
    "Docker": {
        "command": "docker --version",
        "parser": None,
    },
    "OpenVPN Connect": {
        "command": '/Applications/"OpenVPN Connect.app"/Contents/MacOS/"OpenVPN Connect" --version',
        "parser": None,
    },
    "Sublime Text": {
        "command": '/Applications/"Sublime Text.app"/Contents/MacOS/"Sublime Text" --version',
        "parser": None,
    },
}
