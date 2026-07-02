"""
File        : security_analyzer.py
Project     : AI Software Quality Assessment
Description :
Analyzer untuk ISO 25010 - Security menggunakan Bandit.
"""

from core.base_analyzer import BaseAnalyzer
from core.analysis_result import AnalysisResult

from iso25010.metrics import Metrics
from iso25010.scoring import ScoringEngine

from llm.reasoner import Reasoner

from bandit.core import config as bandit_config
from bandit.core import manager as bandit_manager


class SecurityAnalyzer(BaseAnalyzer):

    def analyze(self, project):

        # =====================================================
        # METRICS PROJECT
        # =====================================================
        metrics = Metrics(project.project_root).summary()

        # =====================================================
        # BANDIT CONFIG
        # =====================================================

        config = bandit_config.BanditConfig()
        b_manager = bandit_manager.BanditManager(
            config,
            agg_type="file"
        )

        # =====================================================
        # SCAN FILES
        # =====================================================

        python_files = Metrics(project.project_root).python_files()

        for file in python_files:

            try:
                b_manager.discover_files([str(file)])
                b_manager.run_tests()

            except Exception:
                continue

        # =====================================================
        # HASIL BANDIT
        # =====================================================

        results = b_manager.get_issue_list()

        high = 0
        medium = 0
        low = 0

        for issue in results:

            severity = issue.severity.lower()

            if severity == "high":
                high += 1

            elif severity == "medium":
                medium += 1

            elif severity == "low":
                low += 1

        # =====================================================
        # HITUNG SKOR
        # =====================================================

        score = ScoringEngine.security_score({

            "high": high,

            "medium": medium,

            "low": low

        })

        # =====================================================
        # FINDINGS
        # =====================================================

        findings = [

            f"High Issues : {high}",

            f"Medium Issues : {medium}",

            f"Low Issues : {low}",

            f"Total Files : {metrics['python_files']}"
        ]

        # =====================================================
        # AI RECOMMENDATION
        # =====================================================

        reasoner = Reasoner()

        recommendation = reasoner.generate_recommendation({

            "characteristic": "Security",

            "score": score,

            "high": high,

            "medium": medium,

            "low": low,

            "findings": findings

        })

        # =====================================================
        # RESULT
        # =====================================================

        return AnalysisResult(

            characteristic="Security",

            score=score,

            findings=findings,

            recommendations=[recommendation],

            evidence={

                "high": high,

                "medium": medium,

                "low": low,

                **metrics

            }

        )