from core.tools.base_tool import BaseTool
from core.command_router import CommandRouter


class CommandTool(BaseTool):

    def __init__(self):
        self.command = CommandRouter()

    def can_handle(self, prompt: str) -> bool:
        text = prompt.lower().strip()

        if not text:
            return False

        known_commands = [
            "open chrome",
            "open calculator",
            "open notepad",
            "open vscode",
            "open downloads",
            "open documents",
            "open desktop",
            "open youtube",
            "open google",
            "search google",
            "search youtube",
            "take screenshot",
            "exit",
        ]

        return any(keyword in text for keyword in known_commands)

    def execute(self, prompt: str):
        return self.command.execute(prompt.lower())