from core.tools.memory_tool import MemoryTool
from core.tools.command_tool import CommandTool
from core.tools.ai_tool import AITool


class ToolRegistry:

    def __init__(self):

        self.tools = [
            MemoryTool(),
            CommandTool(),
            AITool()
        ]

    def handle(self, prompt: str):

        for tool in self.tools:

            if tool.can_handle(prompt):
                return tool.execute(prompt)

        return "I couldn't process your request."