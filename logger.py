import logging
from logging.handlers import RotatingFileHandler
import os

from settings import settings

logger = logging.getLogger()

LOG_LEVEL = logging.DEBUG


# 300 мб логов
max_rotate_file_bytes = 1024 * 1024 * 300


# Если запускаем из под докера то все норм
# TODO может можно проверить тип запуска

def init_file_logger():
    if isinstance(settings.BASE_LOG_PATH, str):
        logger.info("Подключение логгирования в файл")
        
        host_log_file_path = os.path.join(settings.BASE_LOG_PATH, 'debug.log')
        
        # Внутренний путь для логов
        container_path = "/var/log/mock_server"
        
        # TODO а может ли не существовать, если забиндился
        # Создадим если не существует
        if not os.path.exists(container_path):
            os.makedirs(container_path, exist_ok=True)

        file_path = os.path.join(container_path, 'debug.log')

        f_handler = RotatingFileHandler(
            file_path,
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
        logger.info(f"Логгирование в файл {host_log_file_path} настроено.")
    else:
        logger.info("Логгирование в файл отключено.")


def init_console_logger():
    c_handler = logging.StreamHandler()
    c_handler.setLevel(LOG_LEVEL)
    c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    logger.addHandler(c_handler)


def init_logger():
    logger.setLevel(LOG_LEVEL)
    # Сначала инициализируем консольный логгер
    init_console_logger()
    # Только потом файловый, чтобы логгировать
    init_file_logger()
