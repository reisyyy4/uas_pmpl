"""
File        : zip_manager.py
Project     : AI Software Quality Assessment
Description :
Mengelola file ZIP yang diunggah pengguna.
"""

from pathlib import Path
import zipfile
import shutil

from utils.helper import create_folder


class ZipManager:

    def __init__(self, zip_path, extract_path):

        self.zip_path = Path(zip_path)
        self.extract_path = Path(extract_path)

    def is_valid_zip(self):

        return zipfile.is_zipfile(self.zip_path)

    def extract(self):

        if not self.is_valid_zip():
            raise ValueError("File bukan ZIP yang valid.")

        create_folder(self.extract_path)

        with zipfile.ZipFile(self.zip_path, "r") as zip_ref:
            zip_ref.extractall(self.extract_path)

        return self.extract_path

    def clean(self):

        if self.extract_path.exists():
            shutil.rmtree(self.extract_path)