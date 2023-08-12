from typing import List

from pydantic import BaseModel


class Cve(BaseModel):
    cve_id: str
    soft: str
    description: str


class Vulnerability(BaseModel):
    cve_list: List[Cve]


class Exx(BaseModel):
    cve_id: str
