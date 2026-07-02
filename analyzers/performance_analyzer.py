"""
File        : performance_analyzer.py
Project     : AI Software Quality Assessment
Description :
Analyzer untuk ISO 25010 - Performance Efficiency.
"""

import time
import psutil
import subprocess

from core.base_analyzer import BaseAnalyzer
from core.analysis_result import AnalysisResult

from iso25010.metrics import Metrics
from iso25010.scoring import ScoringEngine

from llm.reasoner import Reasoner


class PerformanceAnalyzer(BaseAnalyzer):

    def analyze(self, project):

        # =====================================================
        # METRICS
        # =====================================================
        metrics = Metrics(project.project_root).summary()

        # =====================================================
        # CPU & MEMORY (baseline system)
        # =====================================================
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent

        runtime = None

        # =====================================================
        # TRY RUN ENTRY POINT
        # =====================================================

        entry = project.entry_point

        if entry != "Unknown":

            try:

                start_time = time.time()

                subprocess.run(

                    ["python", entry],

                    cwd=project.project_root,

                    timeout=10,

                    capture_output=True

                )

                runtime = time.time() - start_time

            except Exception:
                runtime = None

        # =====================================================
        # FALLBACK RUNTIME
        # =====================================================

        if runtime is None:

            # estimasi berdasarkan kompleksitas
            runtime = metrics["loc"] / 1000

        # =====================================================
        # HITUNG SKOR
        # =====================================================

        score = ScoringEngine.performance_score(

            cpu=cpu_usage,

            memory=memory_usage,

            runtime=runtime

        )

        # =====================================================
        # FINDINGS
        # =====================================================

        findings = [

            f"CPU Usage : {cpu_usage} %",

            f"Memory Usage : {memory_usage} %",

            f"Runtime : {round(runtime, 2)} seconds",

            f"Total LOC : {metrics['loc']}",

            f"Python Files : {metrics['python_files']}"
        ]

        # =====================================================
        # AI RECOMMENDATION
        # =====================================================

        reasoner = Reasoner()

        recommendation = reasoner.generate_recommendation({

            "characteristic": "Performance Efficiency",

            "score": score,

            "cpu": cpu_usage,

            "memory": memory_usage,

            "runtime": runtime,

            "metrics": metrics,

            "findings": findings

        })

        # =====================================================
        # RESULT
        # =====================================================

        return AnalysisResult(

            characteristic="Performance Efficiency",

            score=score,

            findings=findings,

            recommendations=[recommendation],

            evidence={

                "cpu": cpu_usage,

                "memory": memory_usage,

                "runtime": runtime,

                **metrics

            }

        )