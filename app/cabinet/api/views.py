from spectree import Response
from flask import Response as FlaskResponse

from app.cabinet.api.consts import SCANNER_TAG
from app.cabinet.api.dto import ScanQuery
from app.cabinet.api.swagger import swagger
from app.common.api.protocols import (
    ErrorResponseProtocol,
    OkResponseProtocol,
    make_ok_response,
)
from app.models import Vulnerability
from app.utils.scanner_factory import scanner_factory


@swagger.validate(
    query=ScanQuery,
    resp=Response(
        HTTP_200=OkResponseProtocol[Vulnerability],
        HTTP_404=ErrorResponseProtocol,
        HTTP_400=ErrorResponseProtocol,
        HTTP_422=ErrorResponseProtocol,
    ),
    tags=[SCANNER_TAG],
)
def scan_system(query: ScanQuery) -> FlaskResponse:
    scanner = scanner_factory(os=query.os, hook=query.database)
    data = scanner.scan()

    return make_ok_response(data_model=data, status_code=200)
