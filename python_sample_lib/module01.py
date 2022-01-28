from io import TextIOWrapper
from json import load
from logging import Logger, config, getLogger


def configure_log() -> None:
    log_config_file: TextIOWrapper = open("./config/log_config.json", "r", encoding="utf-8")
    config.dictConfig(load(log_config_file))
    return None


def get_logger(name: str) -> Logger:
    logger: Logger = getLogger(name)
    return logger
