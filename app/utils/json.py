from typing import Any, Union
from datetime import datetime, date

import orjson
from flask.app import Flask
from flask.json import JSONEncoder


def orjson_dumps(
    obj: Any, *, default: Any = None, **kwargs: Any
) -> str:  # pylint: disable=unused-argument
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(obj, default=default).decode()  # pylint: disable=no-member


def orjson_loads(value: Union[str, bytes]) -> Any:
    return orjson.loads(value)


class JSONEncoderCustomDatetimeFormat(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, date):
            return o.isoformat()

        if isinstance(o, datetime):
            return o.isoformat(timespec="seconds")

        if isinstance(o, set):
            return list(o)

        return super().default(o)


def init_flask_json_encoder(app: Flask) -> None:
    app.json_encoder = JSONEncoderCustomDatetimeFormat
