"""
File        : rules.py
Project     : AI Software Quality Assessment
Description :
Berisi seluruh aturan penilaian ISO/IEC 25010.
"""


class Rules:

    # =====================================================
    # Functional Suitability
    # =====================================================

    FUNCTIONAL = {

        "entry_point": 20,

        "readme": 10,

        "requirements": 10,

        "python_files": {

            "excellent": (10, 15),

            "good": (5, 10),

            "minimum": (1, 5)

        },

        "functions": {

            "excellent": (20, 15),

            "good": (10, 10),

            "minimum": (5, 5)

        },

        "classes": {

            "excellent": (5, 15),

            "good": (2, 10),

            "minimum": (1, 5)

        },

        "loc": {

            "excellent": (1000, 15),

            "good": (500, 10),

            "minimum": (100, 5)

        }

    }

    # =====================================================
    # Maintainability
    # =====================================================

    MAINTAINABILITY = {

        "mi": {

            "excellent": (85, 40),

            "good": (70, 30),

            "fair": (50, 20),

            "poor": (0, 10)

        },

        "complexity": {

            "excellent": (5, 30),

            "good": (10, 20),

            "fair": (15, 10)

        },

        "documentation": 30

    }

    # =====================================================
    # Security
    # =====================================================

    SECURITY = {

        "high": -20,

        "medium": -10,

        "low": -5,

        "max_score": 100

    }

    # =====================================================
    # Performance
    # =====================================================

    PERFORMANCE = {

        "cpu": {

            "excellent": (20, 40),

            "good": (40, 30),

            "fair": (70, 20)

        },

        "memory": {

            "excellent": (150, 30),

            "good": (300, 20),

            "fair": (500, 10)

        },

        "runtime": {

            "excellent": (1, 30),

            "good": (3, 20),

            "fair": (5, 10)

        }

    }

    # =====================================================
    # Usability
    # =====================================================

    USABILITY = {

        "layout": 20,

        "navigation": 20,

        "consistency": 20,

        "typography": 20,

        "accessibility": 20

    }