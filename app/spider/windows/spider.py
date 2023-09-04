import os
from glob import glob
from typing import List

from app.spider.base import BaseSpider
from app.spider.windows.consts import APPLICATIONS_PATH


class WindowsSpider(BaseSpider):
    def parse(self) -> List[str]:
        soft_list = []
        os.chdir(APPLICATIONS_PATH)
        for application in glob('**/*.exe', recursive=True):
            application = application.replace('.exe', '')
            self._soft_set.add(application)
            soft_list.append(application)

        return soft_list
