from typing import Dict, Type

from app.detector.sql_components.dbeaver import DBeaverClickhouseDataSqlComponent
from app.detector.sql_components.docker import DockerClickhouseDataSqlComponent
from app.detector.sql_components.google import GoogleClickhouseDataSqlComponent
from app.detector.sql_components.openvpn_connect import (
    OpenVPNConnectClickhouseDataSqlComponent,
)
from app.detector.sql_components.pycharm import PycharmClickhouseDataSqlComponent
from app.externals.sql_components.sql_component import SqlDataComponent

SQL_COMPONENTS: Dict[str, Dict[str, Type[SqlDataComponent]]] = {
    "Google Chrome": {
        "Clickhouse": GoogleClickhouseDataSqlComponent,
    },
    "Docker": {
        "Clickhouse": DockerClickhouseDataSqlComponent,
    },
    "OpenVPN Connect": {
        "Clickhouse": OpenVPNConnectClickhouseDataSqlComponent,
    },
    "PyCharm": {
        "Clickhouse": PycharmClickhouseDataSqlComponent,
    },
    "DBeaver": {
        "Clickhouse": DBeaverClickhouseDataSqlComponent,
    },
}

__all__ = [
    "SQL_COMPONENTS",
]
