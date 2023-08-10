from clickhouse_driver import Client
from app.config import Config


def get_ch_client() -> Client:
    return Client(
        host=Config.CH_CALCULATOR_HOST,
        port=Config.CH_CALCULATOR_PORT,
        user=Config.CH_CALCULATOR_USERNAME,
        password=Config.CH_CALCULATOR_PASSWORD,
        database=Config.CH_CALCULATOR_DATABASE,
        secure=False,
        verify=False,
        compression=False,
    )
