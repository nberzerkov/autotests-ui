import logging

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)  # инициализация логгера с указанным именем

    logger.setLevel(logging.DEBUG)  # устанавливаем уровень логирования на уровень DEBUG для логгера

    handler = logging.StreamHandler()  # создание обработчика, который выводит логи в консоль

    handler.setLevel(logging.DEBUG)  # устанавливаем уровень логирования на уровень DEBUG для обработчика

    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)  # применяем форматтер к обработчику

    logger.addHandler(handler)  # добавляем обработчик к логгеру

    return logger
