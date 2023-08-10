import subprocess
import sys
import os
from glob import glob
from pathlib import Path

from app.spider.macos import MacOsSpider
from app.spider.macos.consts import APPLICATIONS_PATH
from app.utils.scanner_factory import scanner_factory
from app.versioneer.macos.versioneer import MacOsVersioneer


def main():
    scanner = scanner_factory(os='MacOs', hook='Clickhouse')
    sf = scanner.scan()
    for key, value in sf.items():
        print(f'{key}: {value}')
    # spider = MacOsSpider()
    # versioneer = MacOsVersioneer()
    # apps = spider.parse()
    # for app in apps:
    #     version = versioneer.get_versions(app)
    #     print(version)
    # subprocess.run('')
    # print(apps)


if __name__ == '__main__':
    main()
