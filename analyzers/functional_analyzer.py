"""
File        : functional_analyzer.py
Project     : AI Software Quality Assessment
Description :
Analyzer untuk Functional Suitability (ISO/IEC 25010).
"""

from core.base_analyzer import BaseAnalyzer
from core.analysis_result import AnalysisResult

from iso25010.metrics import Metrics
from iso25010.scoring import ScoringEngine

from llm.reasoner import Reasoner


class FunctionalAnalyzer(BaseAnalyzer):

    def analyze(self, project):

        # ==========================================
        # Ambil metrik project
        # ==========================================

        metrics = Metrics(project.project_root).summary()

        # ==========================================
        # Hitung skor
        # ==========================================

        score = ScoringEngine.functional_score(
            project,
            metrics
        )

        # ==========================================
        # Temuan
        # ==========================================

        findings = [

            f"Framework : {project.framework}",

            f"Entry Point : {project.entry_point}",

            f"Python Files : {metrics['python_files']}",

            f"Functions : {metrics['functions']}",

            f"Classes : {metrics['classes']}",

            f"Lines of Code : {metrics['loc']}",

            f"README : {'Ya' if project.has_readme else 'Tidak'}",

            f"Requirements : {'Ya' if project.has_requirements else 'Tidak'}"

        ]

        # ==========================================
        # AI Recommendation
        # ==========================================

        reasoner = Reasoner()

        recommendation = reasoner.generate_recommendation(
            {
                "characteristic": "Functional Suitability",
                "score": score,
                "metrics": metrics,
                "findings": findings
            }
        )

        # ==========================================
        # Hasil
        # ==========================================

        return AnalysisResult(

            characteristic="Functional Suitability",

            score=score,

            findings=findings,

            recommendations=[recommendation],

            evidence=metrics
        )