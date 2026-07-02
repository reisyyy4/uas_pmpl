"""
File        : base_analyzer.py
Project     : AI Software Quality Assessment
Description :
Abstract class untuk seluruh analyzer.
"""

from abc import ABC, abstractmethod

from core.analysis_result import AnalysisResult
from core.project_info import ProjectInfo


class BaseAnalyzer(ABC):

    @abstractmethod
    def analyze(self, project: ProjectInfo) -> AnalysisResult:
        """
        Melakukan analisis terhadap project.
        """
        pass