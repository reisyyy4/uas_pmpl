"""
File        : report_generator.py
Project     : AI Software Quality Assessment
Description :
Generate PDF report hasil analisis ISO 25010.
"""

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

from datetime import datetime


class ReportGenerator:

    def generate_pdf(self, result: dict, output_path: str):

        doc = SimpleDocTemplate(output_path, pagesize=A4)

        styles = getSampleStyleSheet()

        content = []

        # =====================================================
        # TITLE
        # =====================================================

        title = Paragraph(
            "AI Software Quality Assessment - ISO/IEC 25010 Report",
            styles["Title"]
        )

        content.append(title)
        content.append(Spacer(1, 12))

        # =====================================================
        # PROJECT INFO
        # =====================================================

        content.append(Paragraph(f"<b>Project:</b> {result['project']}", styles["Normal"]))

        content.append(Paragraph(f"<b>Date:</b> {datetime.now()}", styles["Normal"]))

        content.append(Spacer(1, 12))

        # =====================================================
        # OVERALL SCORE
        # =====================================================

        content.append(
            Paragraph(
                f"<b>Overall Score:</b> {result['overall_score']}",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Grade:</b> {result['grade']}",
                styles["Heading2"]
            )
        )

        content.append(Spacer(1, 12))

        # =====================================================
        # DETAIL ISO 25010
        # =====================================================

        content.append(Paragraph("<b>ISO 25010 Details:</b>", styles["Heading2"]))

        for r in result["details"]:

            content.append(
                Paragraph(
                    f"{r.characteristic} : {r.score}",
                    styles["Normal"]
                )
            )

        content.append(Spacer(1, 12))

        # =====================================================
        # AI SUMMARY
        # =====================================================

        content.append(Paragraph("<b>AI Summary:</b>", styles["Heading2"]))

        content.append(
            Paragraph(result["summary"], styles["Normal"])
        )

        content.append(Spacer(1, 12))

        # =====================================================
        # FINDINGS DETAIL
        # =====================================================

        content.append(Paragraph("<b>Detailed Findings:</b>", styles["Heading2"]))

        for r in result["details"]:

            content.append(
                Paragraph(f"<b>{r.characteristic}</b>", styles["Heading3"])
            )

            for f in r.findings:

                content.append(Paragraph(f"- {f}", styles["Normal"]))

            content.append(Spacer(1, 6))

        # =====================================================
        # RECOMMENDATIONS
        # =====================================================

        content.append(Paragraph("<b>AI Recommendations:</b>", styles["Heading2"]))

        for r in result["details"]:

            for rec in r.recommendations:

                content.append(Paragraph(f"- {rec}", styles["Normal"]))

        # =====================================================
        # BUILD PDF
        # =====================================================

        doc.build(content)

        return output_path