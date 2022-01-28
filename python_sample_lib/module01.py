from io import TextIOWrapper
from json import load
from logging import Logger, config, getLogger


def get_logger(name: str) -> Logger:
    __configure_log_env()
    logger: Logger = getLogger(name)
    return logger


def __configure_log_env() -> None:
    log_config_file: TextIOWrapper = open("./config/log_config.json", "r", encoding="utf-8")
    config.dictConfig(load(log_config_file))
    return None
