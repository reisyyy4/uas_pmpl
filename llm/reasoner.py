"""
File        : reasoner.py
Project     : AI Software Quality Assessment
Description :
Mengubah hasil analyzer menjadi prompt untuk LLM.
"""

from llm.prompts import (
    SYSTEM_PROMPT,
    SUMMARY_PROMPT,
    RECOMMENDATION_PROMPT
)

from llm.ollama_client import OllamaClient


class Reasoner:

    def __init__(self):

        self.client = OllamaClient()

    # ============================================

    def generate_summary(self, results):

        prompt = f"""

{SYSTEM_PROMPT}

{SUMMARY_PROMPT}

{results}

"""

        return self.client.generate(prompt)

    # ============================================

    def generate_recommendation(self, results):

        prompt = f"""

{SYSTEM_PROMPT}

{RECOMMENDATION_PROMPT}

{results}

"""

        return self.client.generate(prompt)