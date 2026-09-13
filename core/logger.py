import logging
import os


def configure_logging(level: str | None = None) -> logging.Logger:
    logger_level_name = (level or os.getenv("LOG_LEVEL", "INFO")).upper()
    logger_level = getattr(logging, logger_level_name, logging.INFO)

    root_logger = logging.getLogger()
    if not root_logger.handlers:
        logging.basicConfig(level=logger_level, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    else:
        root_logger.setLevel(logger_level)

    return root_logger


def get_logger(name: str) -> logging.Logger:
    configure_logging()
    return logging.getLogger(name)


configure_logging()
