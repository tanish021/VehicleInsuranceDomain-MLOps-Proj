import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from from_root import from_root
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024
BACKUP_COUNT = 3

log_dir_path = ROOT_DIR / "logs"
log_dir_path.mkdir(parents=True, exist_ok=True)
os.makedirs(log_dir_path, exist_ok=True)

log_file_path = log_dir_path / LOG_FILE


def configure_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"
    )

    file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=MAX_LOG_SIZE,
        backupCount=BACKUP_COUNT
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

configure_logger()
logging.info(f"Logging started. Log file: {log_file_path}")