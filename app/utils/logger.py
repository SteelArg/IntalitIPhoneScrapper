import logging

from app.configuration import get_log_path_for


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    handler = logging.FileHandler(get_log_path_for(logger_name))

    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger
