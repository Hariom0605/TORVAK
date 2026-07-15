from core.ai_engine import AIEngine
from core.router import AIRouter
from core.command_router import CommandRouter
from core.memory_manager import process_memory


class Assistant:

    def __init__(self):

        self.ai = AIEngine()
        self.router = AIRouter(self.ai)
        self.command = CommandRouter()

    def process(self, prompt):

        text = prompt.lower()

        # ---------------- MEMORY ---------------- #

        memory_response = process_memory(prompt)

        if memory_response is not None:
            return memory_response

        # ---------------- COMMANDS ---------------- #

        result = self.command.execute(text)

        if result != "Command Not Found":
            return result

        # ---------------- AI ---------------- #

        return self.router.route(prompt)