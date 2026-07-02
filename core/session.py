"""
File        : session.py
Project     : AI Software Quality Assessment
Description :
Menyimpan informasi satu sesi analisis.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Session:

    session_id: str

    created_at: datetime

    project_name: str

    results: list = field(default_factory=list)

    overall_score: float = 0

    grade: str = "-"