import logging

from app.configuration import get_log_path_for


def get_logger(logger_name):
    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    logger = logging.getLogger(logger_name)

    handler = logging.FileHandler(get_log_path_for(logger_name))
    handler.setFormatter(formatter)

    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger
