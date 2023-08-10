from app.detector.base.base_detector import BaseDetector
from app.externals.hooks import BaseHook
from app.scanner.base.base_scanner import BaseScanner
from app.spider.base import BaseSpider
from app.versioneer.base.base_versioneer import BaseVersioneer


class Scanner(BaseScanner):
    def __init__(self, spider: BaseSpider, versioneer: BaseVersioneer, detector: BaseDetector, hook: BaseHook) -> None:
        self.spider = spider
        self.versioneer = versioneer
        self.detector = detector
        self.hook = hook

    def scan(self):
        vulnerabilities = {}
        apps = self.spider.parse()
        for app in apps:
            version = self.versioneer.get_version(app)
            cves = self.detector.detect(soft=app, params=version)
            vulnerabilities.update({app: cves})
        return vulnerabilities
