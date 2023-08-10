from enum import Enum
from typing import Optional

from app.detector.base import BaseDetector
from app.detector.base.detector import Detector
# from app.detector.base import BaseDetector
from app.externals.hooks import ClickHouseHook
from app.scanner.base import Scanner
from app.spider.macos import MacOsSpider
from app.versioneer.macos import MacOsVersioneer

HOOKS = {
    'Clickhouse': ClickHouseHook(),
}

SPIDERS = {
    'MacOs': MacOsSpider(),
}

VERSIONEERS = {
    'MacOs': MacOsVersioneer(),
}


def scanner_factory(
        os: str,
        hook: Optional[str] = None,
        spider: Optional[str] = None,
        versioneer: Optional[str] = None,
    ):
    hook = HOOKS.get(hook) if hook else HOOKS.get(os)
    spider = SPIDERS.get(spider) if spider else SPIDERS.get(os)
    versioneer = SPIDERS.get(versioneer) if versioneer else VERSIONEERS.get(os)
    detector = Detector(hook)
    return Scanner(spider=spider, versioneer=versioneer, detector=detector, hook=hook)
