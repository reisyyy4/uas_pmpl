"""
File        : helper.py
Project     : AI Software Quality Assessment
Description :
Berisi fungsi-fungsi umum yang digunakan oleh seluruh aplikasi.
"""

from pathlib import Path
from datetime import datetime
import shutil
import uuid


def generate_session_id() -> str:
    """
    Membuat ID unik untuk setiap proses analisis.
    """
    return uuid.uuid4().hex


def get_current_datetime() -> str:
    """
    Mengembalikan waktu saat ini.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_folder(folder_path: str | Path):
    """
    Membuat folder jika belum ada.
    """
    Path(folder_path).mkdir(parents=True, exist_ok=True)


def delete_folder(folder_path: str | Path):
    """
    Menghapus folder beserta isinya.
    """
    folder = Path(folder_path)

    if folder.exists():
        shutil.rmtree(folder)


def get_file_extension(file_name: str) -> str:
    """
    Mengambil ekstensi file.
    """
    return Path(file_name).suffix.lower()


def format_score(score: float) -> float:
    """
    Membulatkan skor menjadi dua angka di belakang koma.
    """
    return round(score, 2)