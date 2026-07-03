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

        print("OLLAMA_URL =", OLLAMA_URL)
        print("URL =", self.url)
        print("MODEL =", self.model)

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

        print("====================================")
        print("URL      :", self.url)
        print("MODEL    :", self.model)
        print("STATUS   :", response.status_code)
        print("RESPONSE :", response.text)
        print("====================================")

        if response.status_code != 200:
            raise Exception(
            f"Ollama Error\n"
            f"Status : {response.status_code}\n"
            f"Body   : {response.text}"
        )

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