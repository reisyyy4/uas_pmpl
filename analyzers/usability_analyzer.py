"""
File        : usability_analyzer.py
Project     : AI Software Quality Assessment
Description :
Analyzer untuk ISO 25010 - Usability.
"""

from core.base_analyzer import BaseAnalyzer
from core.analysis_result import AnalysisResult

from iso25010.metrics import Metrics
from iso25010.scoring import ScoringEngine

from llm.reasoner import Reasoner


class UsabilityAnalyzer(BaseAnalyzer):

    def analyze(self, project):

        # =====================================================
        # METRICS
        # =====================================================
        metrics = Metrics(project.project_root).summary()

        # =====================================================
        # HEURISTIC UI SCORE
        # =====================================================

        ui_scores = {
            "layout": 0,
            "navigation": 0,
            "consistency": 0,
            "typography": 0,
            "accessibility": 0
        }

        # -----------------------------------------------------
        # Framework indicator
        # -----------------------------------------------------

        if project.framework == "Streamlit":
            ui_scores["layout"] += 20
            ui_scores["navigation"] += 20
            ui_scores["consistency"] += 15

        elif project.framework == "Flask":
            ui_scores["navigation"] += 15
            ui_scores["consistency"] += 15

        elif project.framework == "Tkinter":
            ui_scores["layout"] += 15
            ui_scores["typography"] += 10

        # -----------------------------------------------------
        # README indicator
        # -----------------------------------------------------

        if project.has_readme:
            ui_scores["accessibility"] += 20

        # -----------------------------------------------------
        # Entry point indicator
        # -----------------------------------------------------

        if project.entry_point != "Unknown":
            ui_scores["navigation"] += 20

        # -----------------------------------------------------
        # Project structure indicator
        # -----------------------------------------------------

        if metrics["python_files"] > 10:
            ui_scores["consistency"] += 10

        if metrics["functions"] > 20:
            ui_scores["layout"] += 10

        # =====================================================
        # HITUNG TOTAL SCORE
        # =====================================================

        score = ScoringEngine.usability_score(ui_scores)

        # =====================================================
        # FINDINGS
        # =====================================================

        findings = [

            f"Framework : {project.framework}",

            f"Python Files : {metrics['python_files']}",

            f"Functions : {metrics['functions']}",

            f"Classes : {metrics['classes']}",

            f"README : {'Ada' if project.has_readme else 'Tidak'}",

            f"Entry Point : {project.entry_point}"

        ]

        # =====================================================
        # AI RECOMMENDATION
        # =====================================================

        reasoner = Reasoner()

        recommendation = reasoner.generate_recommendation({

            "characteristic": "Usability",

            "score": score,

            "ui_scores": ui_scores,

            "framework": project.framework,

            "metrics": metrics,

            "findings": findings

        })

        # =====================================================
        # RESULT
        # =====================================================

        return AnalysisResult(

            characteristic="Usability",

            score=score,

            findings=findings,

            recommendations=[recommendation],

            evidence={

                "ui_scores": ui_scores,

                **metrics

            }

        )