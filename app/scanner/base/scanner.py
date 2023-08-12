from app.detector.base.base_detector import BaseDetector
from app.models import Vulnerability
from app.externals.hooks import BaseHook
from app.scanner.base.base_scanner import BaseScanner
from app.spider.base import BaseSpider
from app.versioneer.base.base_versioneer import BaseVersioneer


class Scanner(BaseScanner):
    def __init__(
        self,
        spider: BaseSpider,
        versioneer: BaseVersioneer,
        detector: BaseDetector,
        hook: BaseHook,
    ) -> None:
        self.spider = spider
        self.versioneer = versioneer
        self.detector = detector
        self.hook = hook

    def scan(self) -> Vulnerability:
        vulnerabilities = []
        apps = self.spider.parse()
        for app in apps:
            version = self.versioneer.get_version_info(app)
            cves = self.detector.detect(soft=app, params=version)
            if cves:
                vulnerabilities.extend(cves)
        return Vulnerability(cve_list=vulnerabilities)
