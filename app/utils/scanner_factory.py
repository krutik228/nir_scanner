from typing import Optional

from app.detector.base.detector import Detector

from app.externals.hooks import ClickHouseHook, BaseHook
from app.scanner.base import Scanner
from app.spider.base import BaseSpider
from app.spider.macos import MacOsSpider
from app.utils.exceptions import ScannerFactoryError
from app.versioneer.base import BaseVersioneer
from app.versioneer.macos import MacOsVersioneer

HOOKS = {
    "Clickhouse": ClickHouseHook(),
}

SPIDERS = {
    "MacOs": MacOsSpider(),
}

VERSIONEERS = {
    "MacOs": MacOsVersioneer(),
}


def scanner_factory(os: str, hook: str):
    _hook: Optional[BaseHook] = HOOKS.get(hook)
    _spider: Optional[BaseSpider] = SPIDERS.get(os)
    _versioneer: Optional[BaseVersioneer] = VERSIONEERS.get(os)

    if not all([_hook, _spider, _versioneer]):
        raise ScannerFactoryError("Hook, spider or versioneer are not defined")

    detector = Detector(_hook)
    return Scanner(
        spider=_spider, versioneer=_versioneer, detector=detector, hook=_hook
    )
