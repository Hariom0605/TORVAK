import re

from core.tools.base_tool import BaseTool
from core.memory_manager import process_memory


class MemoryTool(BaseTool):

    MEMORY_PATTERNS = [
        r"\bmy name is\b",
        r"\bi live in\b",
        r"\bi am \d+ years old\b",
        r"\bi like\b",
        r"\bi prefer\b",
        r"\bi am working on\b",
        r"\bmy goal is\b",
        r"\bremember( to)?\b",
        r"\bwhat is my name\b",
        r"\bwhere do i live\b",
        r"\bwhat are my projects\b",
        r"\bwhat are my goals\b",
        r"\bwhat do you know about me\b",
    ]

    def can_handle(self, prompt: str) -> bool:
        text = prompt.strip().lower()
        return any(re.search(pattern, text) for pattern in self.MEMORY_PATTERNS)

    def execute(self, prompt: str):
        return process_memory(prompt)