"""
File        : ai_agent.py
Project     : AI Software Quality Assessment
Description :
AI Agent utama untuk menjalankan seluruh pipeline ISO 25010.
"""

from analyzers.functional_analyzer import FunctionalAnalyzer
from analyzers.maintainability_analyzer import MaintainabilityAnalyzer
from analyzers.security_analyzer import SecurityAnalyzer
from analyzers.performance_analyzer import PerformanceAnalyzer
from analyzers.usability_analyzer import UsabilityAnalyzer

from iso25010.grading import GradeEngine
from llm.reasoner import Reasoner

from core.session import Session
from datetime import datetime


class AIAgent:

    def __init__(self):

        self.functional = FunctionalAnalyzer()
        self.maintainability = MaintainabilityAnalyzer()
        self.security = SecurityAnalyzer()
        self.performance = PerformanceAnalyzer()
        self.usability = UsabilityAnalyzer()

        self.reasoner = Reasoner()

    # =====================================================
    # MAIN PIPELINE
    # =====================================================

    def run(self, project):

        session = Session(

            session_id=str(datetime.now().timestamp()),

            created_at=datetime.now(),

            project_name=project.project_name,

            results=[]
        )

        # =====================================================
        # RUN ALL ANALYZERS
        # =====================================================

        functional = self.functional.analyze(project)
        maintainability = self.maintainability.analyze(project)
        security = self.security.analyze(project)
        performance = self.performance.analyze(project)
        usability = self.usability.analyze(project)

        results = [
            functional,
            maintainability,
            security,
            performance,
            usability
        ]

        session.results = results

        # =====================================================
        # OVERALL SCORE
        # =====================================================

        total_score = (
            functional.score +
            maintainability.score +
            security.score +
            performance.score +
            usability.score
        ) / 5

        session.overall_score = total_score

        # =====================================================
        # GRADE
        # =====================================================

        grade_info = GradeEngine.get_grade(total_score)

        session.grade = grade_info["grade"]

        # =====================================================
        # AI SUMMARY
        # =====================================================

        summary = self.reasoner.generate_summary({

            "project": project.project_name,

            "overall_score": total_score,

            "grade": session.grade,

            "results": [

                {

                    "characteristic": r.characteristic,

                    "score": r.score

                }

                for r in results

            ]

        })

        # =====================================================
        # FINAL REPORT
        # =====================================================

        return {

            "session_id": session.session_id,

            "project": project.project_name,

            "overall_score": round(total_score, 2),

            "grade": session.grade,

            "summary": summary,

            "details": results

        }