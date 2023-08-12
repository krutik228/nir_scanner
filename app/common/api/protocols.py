import logging
from typing import Any, Generic, Optional, TypeVar, Literal

from flask import Response, jsonify
from pydantic import BaseModel, Field, ValidationError
from pydantic.generics import GenericModel
from werkzeug.exceptions import UnprocessableEntity

from logging import getLogger

logger = getLogger(__name__)


ProtocolDataT = TypeVar("ProtocolDataT", bound=BaseModel)


class OkResponseProtocol(GenericModel, Generic[ProtocolDataT]):
    status: str = Field("OK", const=True)
    message: Optional[str] = None
    data: Optional[ProtocolDataT] = None


class ErrorResponseProtocol(BaseModel):
    status: str = Field("error", const=True)
    message: str
    data: Optional[Any] = None


def make_error_response(status_code: int, message: str) -> Response:
    error_model = ErrorResponseProtocol(message=message)
    response = jsonify(error_model.dict())
    response.status_code = status_code
    return response


def make_ok_response(
    data_model: Optional[ProtocolDataT] = None,
    message: Optional[str] = None,
    status_code: int = 200,
) -> Response:
    ok_response_model = OkResponseProtocol(
        message=message, data=data_model
    )  # type: OkResponseProtocol[ProtocolDataT]
    response = jsonify(ok_response_model.dict())
    response.status_code = status_code
    return response


def request_validation_error_handler(
    req: Any, resp: Any, req_validation_error: ValidationError, instance: Any
) -> None:
    """see spectree.utils.default_before_handler for more information"""

    if req_validation_error:
        logging.info(
            "Request ValidationError",
            extra={
                "request_data": req.json,
                "validation_error": req_validation_error.json(),
            },
        )

        raise UnprocessableEntity
