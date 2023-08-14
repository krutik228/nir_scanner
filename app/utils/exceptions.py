from clickhouse_driver.errors import ServerException


class ScannerFactoryError(Exception):
    pass


class DetectError(Exception):
    pass


class VersionNotFound(DetectError):
    pass


class DataBaseError(ServerException):
    pass
