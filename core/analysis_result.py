"""
File        : analysis_result.py
Project     : AI Software Quality Assessment
Description :
Model hasil analisis setiap karakteristik ISO 25010.
"""

from dataclasses import dataclass, field


@dataclass
class AnalysisResult:

    characteristic: str

    score: float

    findings: list = field(default_factory=list)

    recommendations: list = field(default_factory=list)

    evidence: dict = field(default_factory=dict)

    status: str = "Success"