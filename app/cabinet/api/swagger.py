from spectree import SpecTree

from .consts import DOC_PATH
from app.common.api.protocols import request_validation_error_handler

swagger = SpecTree(
    "flask",
    title="Vulnerability Scanner",
    path=DOC_PATH,
    before=request_validation_error_handler,
    annotations=True,
)
