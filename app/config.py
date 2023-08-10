from os import getenv


class Config:
    CH_CALCULATOR_HOST = getenv('CH_CALCULATOR_SERVER', 'localhost')
    CH_CALCULATOR_PORT = int(getenv('CH_CALCULATOR_PORT', '9000'))
    CH_CALCULATOR_USERNAME = getenv('CH_CALCULATOR_USER', 'default')
    CH_CALCULATOR_PASSWORD = getenv('CH_CALCULATOR_PASSWORD', '')
    CH_CALCULATOR_DATABASE = getenv('CH_CALCULATOR_DATABASE', 'db_scanner')
