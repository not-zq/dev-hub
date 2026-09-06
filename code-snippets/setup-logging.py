
import logging
from pathlib import Path

def get_logger(
    name: str,
    stream_handler_level: str | None = "INFO",
    file_handler_level:   str | None = None,
    log_file_path: Path | None = None,
) -> logging.Logger:

    if file_handler_level and not log_file_path:
        raise TypeError("File handler level was set but no file path for logging was provided")

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        fmt     = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
    )

    if stream_handler_level:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(getattr(logging, stream_handler_level))
        logger.addHandler(stream_handler)
        logger.debug(f"Stream handler initialized set to {stream_handler_level}")

    if file_handler_level:
        file_handler = logging.FileHandler(log_file_path, encoding = "utf-8")
        file_handler.setFormatter(formatter)
        file_handler.setLevel(getattr(logging, file_handler_level))
        logger.addHandler(file_handler)
        logger.debug(f"File handler initizalized set to {file_handler_level}")

    return logger

if __name__ == "__main__":

    logger = get_logger(name = "Logger")
    logger.info("Logger initialized")
