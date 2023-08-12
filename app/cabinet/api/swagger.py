from spectree import SpecTree

from .consts import DOC_PATH
from ...common.api.protocols import request_validation_error_handler

swagger = SpecTree(
    "flask",
    title="Report data generation service",
    path=DOC_PATH,
    before=request_validation_error_handler,
    annotations=True,
)
