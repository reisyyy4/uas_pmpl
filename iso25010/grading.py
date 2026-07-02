"""
File        : grading.py
Project     : AI Software Quality Assessment
Description :
Mengubah skor menjadi grade dan kategori kualitas.
"""


class GradeEngine:

    @staticmethod
    def get_grade(score: float):

        if score >= 85:

            return {

                "grade": "A",

                "category": "Excellent"

            }

        elif score >= 70:

            return {

                "grade": "B",

                "category": "Good"

            }

        elif score >= 55:

            return {

                "grade": "C",

                "category": "Fair"

            }

        elif score >= 40:

            return {

                "grade": "D",

                "category": "Poor"

            }

        else:

            return {

                "grade": "E",

                "category": "Very Poor"

            }