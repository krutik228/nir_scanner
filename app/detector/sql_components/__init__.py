from app.detector.sql_components.docker import DockerClickhouseDataSqlComponent
from app.detector.sql_components.google import GoogleClickhouseDataSqlComponent

SQL_COMPONENTS = {
    "Google Chrome": {
        "Clickhouse": GoogleClickhouseDataSqlComponent,
    },
    "Docker": {
        "Clickhouse": DockerClickhouseDataSqlComponent,
    },

}

__all__ = [
    'SQL_COMPONENTS',
]
