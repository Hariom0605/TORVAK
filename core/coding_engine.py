from core.ai_engine import AIEngine


class CodingEngine:

    def __init__(self):

        self.ai = AIEngine()

    def chat(self, prompt):

        coding_prompt = f"""
You are TORVAK Coding Assistant.

Rules:
- Generate professional code.
- Explain code if needed.
- Fix bugs.
- Give best practices.
- Return clean code.

User Request:
{prompt}
"""

        return self.ai.chat(coding_prompt)