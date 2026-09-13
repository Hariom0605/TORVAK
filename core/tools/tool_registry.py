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

    def find_by_capability(self, capability: str):
        """Find a tool by capability hint."""
        capability_map = {
            "memory": MemoryTool,
            "command": CommandTool,
            "ai": AITool,
            "chat": AITool,
            "coding": AITool,
        }
        tool_class = capability_map.get(capability.lower())
        if tool_class:
            for tool in self.tools:
                if isinstance(tool, tool_class):
                    return tool
        return None