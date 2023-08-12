from typing import List, Optional

from pydantic import BaseModel


class Cve(BaseModel):
    cve_id: str
    soft: str
    description: Optional[str]
    severity: float


class Vulnerability(BaseModel):
    cve_list: List[Cve]


class Exx(BaseModel):
    cve_id: str
