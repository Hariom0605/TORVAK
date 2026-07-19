class PromptBuilder:

    def __init__(self):

        self.system_prompt = """
You are TORVAK, an intelligent AI assistant.

Answer the user's question ONLY using the provided context.

Rules:

1. Never use outside knowledge.
2. If the answer is not available in the context, reply:
   "I couldn't find the answer in the indexed documents."
3. Keep answers accurate and concise.
4. If possible, explain in simple language.
5. Preserve technical terms exactly as they appear.
6. Never hallucinate.
"""

    def build_prompt(
        self,
        question: str,
        context: str
    ) -> str:

        prompt = f"""
{self.system_prompt}

==========================
CONTEXT
==========================

{context}

==========================
QUESTION
==========================

{question}

==========================
ANSWER
==========================
"""

        return prompt