from core.tools.base_tool import BaseTool
from core.ai_engine import AIEngine
from core.router import AIRouter


class AITool(BaseTool):

    def __init__(self):

        self.ai = AIEngine()
        self.router = AIRouter(self.ai)

    def can_handle(self, prompt: str) -> bool:
        return True

    def execute(self, prompt: str):

        return self.router.route(prompt)