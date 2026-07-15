
from config.settings import GEMINI_API_KEY
from core.context_memory import ContextMemory

import socket
import ollama
import google.generativeai as genai


SYSTEM_PROMPT = """
You are TORVAK AI OS.

You are a personal AI assistant running on the user's computer.

Never say you are Google, OpenAI, Microsoft or any company.

Your creator, owner and administrator are the local user.

Always prefer stored memory over model knowledge.

Keep replies concise unless detailed explanation is requested.

Behave like a personal AI Operating System.
"""


class AIEngine:

    def __init__(self):

        self.context = ContextMemory()

        try:

            genai.configure(api_key=GEMINI_API_KEY)

            self.online = genai.GenerativeModel(
                "gemini-2.5-flash"
            )

        except Exception:

            self.online = None

    def internet(self):

        try:

            socket.create_connection(("8.8.8.8", 53), 2)

            return True

        except:

            return False

    def online_chat(self, prompt):

        full_prompt = SYSTEM_PROMPT + "\n\nUser: " + prompt

        response = self.online.generate_content(
            full_prompt
        )

        return response.text

    def offline_chat(self, prompt):

        try:

            response = ollama.chat(

                model="phi4-mini:3.8b",

                messages=[

                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },

                    {
                        "role": "user",
                        "content": prompt
                    }

                ]

            )

            return response["message"]["content"]

        except Exception:

            return None

    def chat(self, prompt):

        self.context.add("user", prompt)

        if self.internet() and self.online:

            try:

                return self.online_chat(prompt)

            except Exception:

                pass

        reply = self.offline_chat(prompt)

        if reply:

            return reply

        return "Sorry! AI Brain is currently unavailable."
