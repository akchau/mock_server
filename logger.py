import logging

logger = logging.getLogger()

LOG_LEVEL = logging.DEBUG


def init_logger():
    logger.setLevel(LOG_LEVEL)
    c_handler = logging.StreamHandler()
    c_handler.setLevel(LOG_LEVEL)
    c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    logger.addHandler(c_handler)
