"""
File        : maintainability_analyzer.py
Project     : AI Software Quality Assessment
Description :
Analyzer untuk ISO 25010 - Maintainability.
"""

from core.base_analyzer import BaseAnalyzer
from core.analysis_result import AnalysisResult

from iso25010.metrics import Metrics
from iso25010.scoring import ScoringEngine

from radon.metrics import mi_visit
from radon.complexity import cc_visit

from llm.reasoner import Reasoner


class MaintainabilityAnalyzer(BaseAnalyzer):

    def analyze(self, project):

        # =====================================================
        # METRICS DASAR PROJECT
        # =====================================================
        metrics = Metrics(project.project_root).summary()

        # =====================================================
        # HITUNG COMPLEXITY (Radon)
        # =====================================================

        complexity_scores = []

        for file in Metrics(project.project_root).python_files():

            try:
                code = file.read_text(encoding="utf-8", errors="ignore")

                # Cyclomatic Complexity
                cc_blocks = cc_visit(code)

                for block in cc_blocks:
                    complexity_scores.append(block.complexity)

            except Exception:
                continue

        avg_complexity = (
            sum(complexity_scores) / len(complexity_scores)
            if complexity_scores else 0
        )

        # =====================================================
        # MAINTAINABILITY INDEX (MI)
        # =====================================================

        mi_scores = []

        for file in Metrics(project.project_root).python_files():

            try:
                code = file.read_text(encoding="utf-8", errors="ignore")

                mi = mi_visit(code, multi=True)

                mi_scores.append(mi)

            except Exception:
                continue

        avg_mi = (
            sum(mi_scores) / len(mi_scores)
            if mi_scores else 0
        )

        # =====================================================
        # HITUNG SKOR
        # =====================================================

        score = ScoringEngine.maintainability_score(
            mi_score=avg_mi,
            complexity=avg_complexity
        )

        # =====================================================
        # FINDINGS
        # =====================================================

        findings = [

            f"Average Maintainability Index : {round(avg_mi, 2)}",

            f"Average Cyclomatic Complexity : {round(avg_complexity, 2)}",

            f"Total Python Files : {metrics['python_files']}",

            f"Total Functions : {metrics['functions']}",

            f"Total Classes : {metrics['classes']}"
        ]

        # =====================================================
        # AI RECOMMENDATION
        # =====================================================

        reasoner = Reasoner()

        recommendation = reasoner.generate_recommendation({

            "characteristic": "Maintainability",

            "score": score,

            "mi": avg_mi,

            "complexity": avg_complexity,

            "metrics": metrics,

            "findings": findings

        })

        # =====================================================
        # RESULT
        # =====================================================

        return AnalysisResult(

            characteristic="Maintainability",

            score=score,

            findings=findings,

            recommendations=[recommendation],

            evidence={

                "mi": avg_mi,

                "complexity": avg_complexity,

                **metrics

            }

        )