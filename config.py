"""
Konfigurasi utama aplikasi
AI Software Quality Assessment
ISO/IEC 25010
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load file .env
load_dotenv()

# =====================================================
# BASE DIRECTORY
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

# =====================================================
# FOLDER
# =====================================================

UPLOAD_SOURCE = BASE_DIR / "uploads" / "source"
UPLOAD_SCREENSHOT = BASE_DIR / "uploads" / "screenshots"
REPORT_FOLDER = BASE_DIR / "reports"
TEMP_FOLDER = BASE_DIR / "temp"

# =====================================================
# AI CONFIGURATION
# =====================================================

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434"
)

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "llama3.2-vision"
)

# =====================================================
# FILE LIMIT
# =====================================================

MAX_FILE_SIZE_MB = 100

# =====================================================
# ISO CHARACTERISTICS
# =====================================================

ISO_CHARACTERISTICS = [
    "Functional Suitability",
    "Performance Efficiency",
    "Security",
    "Maintainability",
    "Usability"
]

# =====================================================
# SCORE RANGE
# =====================================================

MAX_SCORE = 100
MIN_SCORE = 0

# =====================================================
# CREATE FOLDER IF NOT EXISTS
# =====================================================

UPLOAD_SOURCE.mkdir(parents=True, exist_ok=True)
UPLOAD_SCREENSHOT.mkdir(parents=True, exist_ok=True)
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)
TEMP_FOLDER.mkdir(parents=True, exist_ok=True)