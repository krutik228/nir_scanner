from enum import Enum

from pydantic import BaseModel


class OsEnum(str, Enum):
    macos = "MacOs"


class DatabaseEnum(str, Enum):
    clickhouse = "Clickhouse"


class ScanQuery(BaseModel):
    os: OsEnum
    database: DatabaseEnum

    class Config:
        use_enum_values = True
