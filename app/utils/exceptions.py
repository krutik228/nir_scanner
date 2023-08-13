class ScannerFactoryError(Exception):
    pass


class DetectError(Exception):
    pass


class VersionNotFound(DetectError):
    pass
