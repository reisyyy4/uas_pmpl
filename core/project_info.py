"""
File        : project_info.py
Project     : AI Software Quality Assessment
Description :
Menyimpan informasi project yang akan dianalisis.
"""

from dataclasses import dataclass


@dataclass
class ProjectInfo:

    project_name: str
    project_root: str

    language: str
    framework: str
    entry_point: str

    total_files: int
    python_files: int
    image_files: int

    has_requirements: bool
    has_readme: bool

    ready_for_analysis: bool