import logging
from logging.handlers import RotatingFileHandler
import os

from settings import settings

logger = logging.getLogger()

LOG_LEVEL = logging.DEBUG


# 300 мб логов
max_rotate_file_bytes = 1024 * 1024 * 300


def init_file_logger():
    f_handler = RotatingFileHandler(
        os.path.join(settings.BASE_LOG_PATH, 'debug.log'),
        maxBytes=max_rotate_file_bytes, 
        backupCount=3
    )
    f_handler.setLevel(LOG_LEVEL)
    f_format = logging.Formatter(
        '%(name)s - %(levelname)s - %(asctime)s - %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)


def init_console_logger():
    c_handler = logging.StreamHandler()
    c_handler.setLevel(LOG_LEVEL)
    c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    logger.addHandler(c_handler)


def init_logger():
    if not os.path.exists(settings.BASE_LOG_PATH):
        logger.debug("Базовый пути логов не существует. Создадим.")
        os.makedirs(settings.BASE_LOG_PATH, exist_ok=True)
    else:
        # TODO ошибка логов
        logger.debug("Базовый пути логов не существует. Создадим.")
    logger.setLevel(LOG_LEVEL)
    init_console_logger()
    init_file_logger()
