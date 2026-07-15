import google.generativeai as genai

class OnlineAI:

    def __init__(self):

        genai.configure(api_key="YOUR_API_KEY")

        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def chat(self, prompt):

        response = self.model.generate_content(prompt)

        return response.text
    