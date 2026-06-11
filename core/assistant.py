from core.command_router import CommandRouter
from core.ai_engine import AIEngine


class Assistant:

    def __init__(self):

        self.router = CommandRouter()
        self.ai = AIEngine()

    def process(self, text):

        result = self.router.execute(text)

        if result != "Command Not Found":
            return result

        return self.ai.chat(text)