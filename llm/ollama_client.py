"""
File        : ollama_client.py
Project     : AI Software Quality Assessment
Description :
Client untuk berkomunikasi dengan Ollama API.
"""

import requests

from config import MODEL_NAME
from config import OLLAMA_URL


class OllamaClient:

    def __init__(self):

        self.url = f"{OLLAMA_URL}/api/generate"

        self.model = MODEL_NAME

    # ============================================
    # Generate Text
    # ============================================

    def generate(self, prompt):

        payload = {

            "model": self.model,

            "prompt": prompt,

            "stream": False

        }

        response = requests.post(

            self.url,

            json=payload,

            timeout=300

        )

        response.raise_for_status()

        return response.json()["response"]

    # ============================================
    # Check Connection
    # ============================================

    def is_connected(self):

        try:

            requests.get(

                OLLAMA_URL,

                timeout=5

            )

            return True

        except Exception:

            return False