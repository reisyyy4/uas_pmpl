"""
File        : logger.py
Project     : AI Software Quality Assessment
Standard    : ISO/IEC 25010
Description :
Menyediakan logger untuk mencatat aktivitas aplikasi.
"""

import logging
from pathlib import Path

# Folder log
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "application.log"


def setup_logger(name: str = "ISO25010_AI") -> logging.Logger:
    """
    Membuat dan mengembalikan objek logger.
    """

    logger = logging.getLogger(name)

    # Hindari handler ganda jika fungsi dipanggil berkali-kali
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # Simpan ke file
    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Tampilkan juga di terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger