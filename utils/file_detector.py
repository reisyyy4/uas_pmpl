"""
File        : file_detector.py
Project     : AI Software Quality Assessment
Description :
Mendeteksi informasi dasar project sebelum dilakukan analisis ISO/IEC 25010.
"""

from pathlib import Path

from core.project_info import ProjectInfo


class FileDetector:

    def __init__(self, project_path):

        self.project_path = Path(project_path)

    # =====================================================
    # Nama Project
    # =====================================================

    def get_project_name(self):

        return self.project_path.name

    # =====================================================
    # Total File
    # =====================================================

    def get_total_files(self):

        return len([
            f for f in self.project_path.rglob("*")
            if f.is_file()
        ])

    # =====================================================
    # Jumlah File Python
    # =====================================================

    def get_python_files(self):

        return len(list(
            self.project_path.rglob("*.py")
        ))

    # =====================================================
    # Jumlah Screenshot / Image
    # =====================================================

    def get_image_files(self):

        image_extensions = (
            ".png",
            ".jpg",
            ".jpeg",
            ".bmp",
            ".webp"
        )

        total = 0

        for file in self.project_path.rglob("*"):

            if file.suffix.lower() in image_extensions:
                total += 1

        return total

    # =====================================================
    # README
    # =====================================================

    def has_readme(self):

        return any(
            self.project_path.rglob("README.md")
        )

    # =====================================================
    # requirements.txt
    # =====================================================

    def has_requirements(self):

        return any(
            self.project_path.rglob("requirements.txt")
        )

    # =====================================================
    # Entry Point
    # =====================================================

    def detect_entry_point(self):

        candidates = [

            "app.py",

            "main.py",

            "run.py",

            "server.py",

            "manage.py"

        ]

        for candidate in candidates:

            for file in self.project_path.rglob(candidate):

                return str(file.relative_to(self.project_path))

        return "Unknown"

    # =====================================================
    # Framework
    # =====================================================

    def detect_framework(self):

        for file in self.project_path.rglob("*.py"):

            try:

                text = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

                if "import streamlit" in text:
                    return "Streamlit"

                if "from flask" in text or "import flask" in text:
                    return "Flask"

                if "import django" in text or "from django" in text:
                    return "Django"

                if "import tkinter" in text:
                    return "Tkinter"

                if "from PyQt5" in text or "import PyQt5" in text:
                    return "PyQt5"

            except Exception:
                continue

        return "Unknown"

    # =====================================================
    # Bahasa
    # =====================================================

    def detect_language(self):

        if self.get_python_files() > 0:
            return "Python"

        return "Unknown"

    # =====================================================
    # Validasi Project
    # =====================================================

    def is_valid_project(self):

        return self.get_python_files() > 0

    # =====================================================
    # Deteksi Keseluruhan
    # =====================================================

    def detect(self):

        return ProjectInfo(

            project_name=self.get_project_name(),

            project_root=str(self.project_path),

            language=self.detect_language(),

            framework=self.detect_framework(),

            entry_point=self.detect_entry_point(),

            total_files=self.get_total_files(),

            python_files=self.get_python_files(),

            image_files=self.get_image_files(),

            has_requirements=self.has_requirements(),

            has_readme=self.has_readme(),

            ready_for_analysis=self.is_valid_project()
        )