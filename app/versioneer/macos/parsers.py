import re
from typing import Tuple, Dict, Any


def google_parser(raw_version: str) -> Dict[str, Dict[str, Any]]:
    pattern = re.compile(r'Google Chrome\s(?P<version>(([0-9]+)\.?)+)').match
    return {'version': pattern(raw_version).group('version')}
