"""
File        : scoring.py
Project     : AI Software Quality Assessment
Description :
Engine utama untuk menghitung skor ISO 25010 berdasarkan rules.
"""

from iso25010.rules import Rules


class ScoringEngine:

    # =====================================================
    # FUNCTIONAL SUITABILITY
    # =====================================================

    @staticmethod
    def functional_score(project, metrics):

        rules = Rules.FUNCTIONAL

        score = 0

        # -----------------------------
        # Entry Point
        # -----------------------------
        if project.entry_point != "Unknown":
            score += rules["entry_point"]

        # -----------------------------
        # README
        # -----------------------------
        if project.has_readme:
            score += rules["readme"]

        # -----------------------------
        # Requirements
        # -----------------------------
        if project.has_requirements:
            score += rules["requirements"]

        # -----------------------------
        # Python Files
        # -----------------------------
        py = metrics["python_files"]

        if py >= rules["python_files"]["excellent"][0]:
            score += rules["python_files"]["excellent"][1]

        elif py >= rules["python_files"]["good"][0]:
            score += rules["python_files"]["good"][1]

        elif py >= rules["python_files"]["minimum"][0]:
            score += rules["python_files"]["minimum"][1]

        # -----------------------------
        # Functions
        # -----------------------------
        fn = metrics["functions"]

        if fn >= rules["functions"]["excellent"][0]:
            score += rules["functions"]["excellent"][1]

        elif fn >= rules["functions"]["good"][0]:
            score += rules["functions"]["good"][1]

        elif fn >= rules["functions"]["minimum"][0]:
            score += rules["functions"]["minimum"][1]

        # -----------------------------
        # Classes
        # -----------------------------
        cl = metrics["classes"]

        if cl >= rules["classes"]["excellent"][0]:
            score += rules["classes"]["excellent"][1]

        elif cl >= rules["classes"]["good"][0]:
            score += rules["classes"]["good"][1]

        elif cl >= rules["classes"]["minimum"][0]:
            score += rules["classes"]["minimum"][1]

        # -----------------------------
        # LOC
        # -----------------------------
        loc = metrics["loc"]

        if loc >= rules["loc"]["excellent"][0]:
            score += rules["loc"]["excellent"][1]

        elif loc >= rules["loc"]["good"][0]:
            score += rules["loc"]["good"][1]

        elif loc >= rules["loc"]["minimum"][0]:
            score += rules["loc"]["minimum"][1]

        return min(score, 100)

    # =====================================================
    # SECURITY
    # =====================================================

    @staticmethod
    def security_score(bandit_result: dict):

        rules = Rules.SECURITY

        score = 100

        score += bandit_result.get("high", 0) * rules["high"]
        score += bandit_result.get("medium", 0) * rules["medium"]
        score += bandit_result.get("low", 0) * rules["low"]

        return max(min(score, 100), 0)

    # =====================================================
    # MAINTAINABILITY (sementara stub)
    # =====================================================

    @staticmethod
    def maintainability_score(mi_score: float, complexity: float):

        rules = Rules.MAINTAINABILITY

        score = 0

        # Maintainability Index
        if mi_score >= rules["mi"]["excellent"][0]:
            score += rules["mi"]["excellent"][1]

        elif mi_score >= rules["mi"]["good"][0]:
            score += rules["mi"]["good"][1]

        elif mi_score >= rules["mi"]["fair"][0]:
            score += rules["mi"]["fair"][1]

        else:
            score += rules["mi"]["poor"][1]

        # Complexity
        if complexity <= 5:
            score += rules["complexity"]["excellent"][1]

        elif complexity <= 10:
            score += rules["complexity"]["good"][1]

        else:
            score += rules["complexity"]["fair"][1]

        # Documentation bonus (sementara)
        score += rules["documentation"]

        return min(score, 100)

    # =====================================================
    # PERFORMANCE (stub awal)
    # =====================================================

    @staticmethod
    def performance_score(cpu, memory, runtime):

        rules = Rules.PERFORMANCE

        score = 0

        # CPU
        if cpu <= 20:
            score += rules["cpu"]["excellent"][1]

        elif cpu <= 40:
            score += rules["cpu"]["good"][1]

        else:
            score += rules["cpu"]["fair"][1]

        # Memory
        if memory <= 150:
            score += rules["memory"]["excellent"][1]

        elif memory <= 300:
            score += rules["memory"]["good"][1]

        else:
            score += rules["memory"]["fair"][1]

        # Runtime
        if runtime <= 1:
            score += rules["runtime"]["excellent"][1]

        elif runtime <= 3:
            score += rules["runtime"]["good"][1]

        else:
            score += rules["runtime"]["fair"][1]

        return min(score, 100)

    # =====================================================
    # USABILITY (stub awal - nanti AI vision)
    # =====================================================

    @staticmethod
    def usability_score(ui_scores: dict):

        rules = Rules.USABILITY

        total = 0

        for k in rules.keys():

            total += ui_scores.get(k, 0)

        return min(total, 100)