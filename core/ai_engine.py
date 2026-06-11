from config import GEMINI_API_KEY
import requests
import ollama
import google.generativeai as genai


class AIEngine:

    def __init__(self):

        genai.configure(api_key=GEMINI_API_KEY)

        self.online = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def internet(self):

        try:
            requests.get(
                "https://google.com",
                timeout=3
            )
            return True

        except:
            return False

    def online_chat(self, prompt):

        response = self.online.generate_content(prompt)

        return response.text

    def offline_chat(self, prompt):

        response = ollama.chat(
            model="qwen2.5:7b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    def chat(self, prompt):

        if self.internet():
            return self.online_chat(prompt)

        return self.offline_chat(prompt)