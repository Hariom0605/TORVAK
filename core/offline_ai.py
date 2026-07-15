import ollama

class OfflineAI:

    def chat(self, prompt):

        try:
            response = ollama.chat(
                model="qwen3:4b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"]

        except Exception:
            return None