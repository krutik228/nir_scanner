from app.detector.sql_components.docker import DockerClickhouseDataSqlComponent
from app.detector.sql_components.google import GoogleClickhouseDataSqlComponent
from app.detector.sql_components.openvpn_connect import OpenVPNConnectClickhouseDataSqlComponent
from app.detector.sql_components.pycharm import PycharmClickhouseDataSqlComponent

SQL_COMPONENTS = {
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

}

__all__ = [
    'SQL_COMPONENTS',
]
