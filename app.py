"""
File        : app.py
Project     : AI Software Quality Assessment
Description :
Streamlit UI untuk menjalankan AI ISO 25010 Analyzer.
"""

import streamlit as st
import tempfile
import zipfile
import os

from utils.zip_manager import ZipManager
from utils.file_detector import FileDetector

from agents.ai_agent import AIAgent

from report.report_generator import ReportGenerator


# =====================================================
# CONFIG UI
# =====================================================

st.set_page_config(

    page_title="ISO 25010 AI Software Analyzer",

    layout="wide"

)

st.title("📊 AI Software Quality Assessment (ISO/IEC 25010)")
st.write("Upload project ZIP untuk dianalisis secara otomatis.")

# =====================================================
# UPLOAD FILE
# =====================================================

uploaded_file = st.file_uploader("Upload Project ZIP", type=["zip"])

if uploaded_file is not None:

    with tempfile.TemporaryDirectory() as tmpdir:

        zip_path = os.path.join(tmpdir, "project.zip")

        # simpan file zip
        with open(zip_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # =================================================
        # EXTRACT ZIP
        # =================================================

        extract_path = os.path.join(tmpdir, "project")

        os.makedirs(extract_path, exist_ok=True)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        st.success("ZIP berhasil diekstrak")

        # =================================================
        # DETECT PROJECT
        # =================================================

        detector = FileDetector(extract_path)

        project = detector.detect()

        st.info(f"Project: {project.project_name}")
        st.info(f"Framework: {project.framework}")
        st.info(f"Entry Point: {project.entry_point}")

        # =================================================
        # RUN ANALYSIS
        # =================================================

        if st.button("🚀 Analyze Project"):

            with st.spinner("AI sedang menganalisis project..."):

                agent = AIAgent()

                result = agent.run(project)

            # =================================================
            # OUTPUT
            # =================================================

            st.success("Analisis selesai!")

            st.subheader("📌 Overall Result")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Overall Score", result["overall_score"])

            with col2:
                st.metric("Grade", result["grade"])

            # =================================================
            # SUMMARY AI
            # =================================================

            st.subheader("🧠 AI Summary")

            st.write(result["summary"])

            # =================================================
            # DETAIL SCORE
            # =================================================

            st.subheader("📊 Detail ISO 25010")

            for r in result["details"]:

                st.write(f"**{r.characteristic}** : {r.score}")

            # =================================================
            # EXPANDER DETAIL
            # =================================================

            with st.expander("📄 Detail Full Analysis"):

                for r in result["details"]:

                    st.markdown(f"### {r.characteristic}")

                    st.write("Score:", r.score)

                    st.write("Findings:")

                    for f in r.findings:
                        st.write("- ", f)

                    st.write("Recommendations:")

                    for rec in r.recommendations:
                        st.write("-", rec)

            reporter = ReportGenerator()

            pdf_path = os.path.join(tmpdir, "report.pdf")

            reporter.generate_pdf(result, pdf_path)

            with open(pdf_path, "rb") as f:

                st.download_button(

                    label="📥 Download Report PDF",

                    data=f,

                    file_name="iso25010_report.pdf",

                    mime="application/pdf"

                )