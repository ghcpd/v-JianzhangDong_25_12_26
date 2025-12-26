import logging

_LOGGER = None

def get_logger(name: str = "app") -> logging.Logger:
    global _LOGGER
    if _LOGGER is None:
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        _LOGGER = logger

    return _LOGGER
