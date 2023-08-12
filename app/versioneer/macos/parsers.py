import re
from typing import Dict


def google_parser(raw_version: str) -> Dict[str, str]:
    pattern = re.compile(r"Google Chrome\s(?P<version>(([0-9]+)\.?)+)").match
    matched = pattern(raw_version)
    if not matched:
        return {"version": raw_version}

    return {"version": matched.group("version")}
