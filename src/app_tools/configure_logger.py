import logging


def configure_logger(
        logger: object,
        info_file: str='',
        debug_file: str='',
        error_file: str='',
        screen_logging: bool=False,
        date_format: str='%Y-%m-%d %H:%M:%S',
        message_format: str='%(asctime)s [%(name)s] %(levelname)s %(message)s',
        start_msg: str='',
        max_bytes: int=10485760,
        backup_counts: int=5,
        ) -> None:


    """
    Стандартная конфигурация логгера.

    logger - Объект логгера
    screen_logging (False) - включить хендлер экрана
    info_file, debug_file, error_file- имена файлов для
    файловых хендлеров (если пустая строка - файловые хендлеры не создаются).
    start_msg - строка, записываемая в лог при старте
    """
    if not isinstance(logger, logging.Logger):
        raise TypeError('logger must be a logging.Logger')

    # set level
    logger.setLevel(logging.DEBUG)

    # create and configure formatters
    # standard formats
    file_formatter = logging.Formatter(fmt=message_format,
                                       datefmt=date_format,
                                       )
    if screen_logging:
        screen_formatter = logging.Formatter(fmt='%(message)s')
        screen_handler = logging.StreamHandler()
        screen_handler.setLevel(logging.INFO)
        screen_handler.setFormatter(screen_formatter)
        logger.addHandler(screen_handler)

    if info_file:
        file_info_handler = logging.handlers.RotatingFileHandler(
            filename=info_file, maxBytes=max_bytes, backupCount=max_bytes)
        file_info_handler.setLevel(logging.INFO)
        file_info_handler.setFormatter(file_formatter)
        logger.addHandler(file_info_handler)

    if debug_file:
        file_debug_handler = logging.handlers.RotatingFileHandler(
                filename=debug_file, maxBytes=max_bytes, backupCount=max_bytes)
        file_debug_handler.setLevel(logging.DEBUG)
        file_debug_handler.setFormatter(file_formatter)
        logger.addHandler(file_debug_handler)

    if error_file:
        file_error_handler = logging.handlers.RotatingFileHandler(
                filename=error_file, maxBytes=max_bytes, backupCount=max_bytes)
        file_error_handler.setLevel(logging.ERROR)
        file_error_handler.setFormatter(file_formatter)
        logger.addHandler(file_error_handler)

    if start_msg:
        logger.debug(start_msg)

