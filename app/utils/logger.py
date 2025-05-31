import logging

from app.configuration import get_log_path_for


def get_logger(logger_name, log_to_console=False):
    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    logger = logging.getLogger(logger_name)

    file_handler = logging.FileHandler(get_log_path_for(logger_name))
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    if log_to_console:
        logger.addHandler(console_handler)

    return logger
