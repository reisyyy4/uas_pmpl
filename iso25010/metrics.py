"""
File        : metrics.py
Project     : AI Software Quality Assessment
Description :
Mengumpulkan metrik dasar project Python.
"""

from pathlib import Path
import ast


class Metrics:

    def __init__(self, project_path):

        self.project_path = Path(project_path)

    # ============================================
    # Semua file Python
    # ============================================

    def python_files(self):

        return list(

            self.project_path.rglob("*.py")

        )

    # ============================================
    # Jumlah file Python
    # ============================================

    def total_python_files(self):

        return len(self.python_files())

    # ============================================
    # Lines of Code
    # ============================================

    def total_loc(self):

        total = 0

        for file in self.python_files():

            try:

                with open(file, "r", encoding="utf-8") as f:

                    total += len(f.readlines())

            except Exception:

                continue

        return total

    # ============================================
    # Empty Lines
    # ============================================

    def total_empty_lines(self):

        total = 0

        for file in self.python_files():

            try:

                with open(file, "r", encoding="utf-8") as f:

                    for line in f:

                        if line.strip() == "":

                            total += 1

            except Exception:

                continue

        return total

    # ============================================
    # Comment Lines
    # ============================================

    def total_comment_lines(self):

        total = 0

        for file in self.python_files():

            try:

                with open(file, "r", encoding="utf-8") as f:

                    for line in f:

                        if line.strip().startswith("#"):

                            total += 1

            except Exception:

                continue

        return total

    # ============================================
    # Function
    # ============================================

    def total_functions(self):

        total = 0

        for file in self.python_files():

            try:

                tree = ast.parse(

                    file.read_text(

                        encoding="utf-8",

                        errors="ignore"

                    )

                )

                total += len(

                    [

                        node

                        for node in ast.walk(tree)

                        if isinstance(node, ast.FunctionDef)

                    ]

                )

            except Exception:

                continue

        return total

    # ============================================
    # Class
    # ============================================

    def total_classes(self):

        total = 0

        for file in self.python_files():

            try:

                tree = ast.parse(

                    file.read_text(

                        encoding="utf-8",

                        errors="ignore"

                    )

                )

                total += len(

                    [

                        node

                        for node in ast.walk(tree)

                        if isinstance(node, ast.ClassDef)

                    ]

                )

            except Exception:

                continue

        return total

    # ============================================
    # Import
    # ============================================

    def total_imports(self):

        total = 0

        for file in self.python_files():

            try:

                tree = ast.parse(

                    file.read_text(

                        encoding="utf-8",

                        errors="ignore"

                    )

                )

                total += len(

                    [

                        node

                        for node in ast.walk(tree)

                        if isinstance(node, (ast.Import, ast.ImportFrom))

                    ]

                )

            except Exception:

                continue

        return total

    # ============================================
    # Ringkasan
    # ============================================

    def summary(self):

        return {

            "python_files": self.total_python_files(),

            "loc": self.total_loc(),

            "empty_lines": self.total_empty_lines(),

            "comment_lines": self.total_comment_lines(),

            "functions": self.total_functions(),

            "classes": self.total_classes(),

            "imports": self.total_imports()

        }