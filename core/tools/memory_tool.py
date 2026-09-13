from core.tools.base_tool import BaseTool
from core.memory.manager import MemoryManager


class MemoryTool(BaseTool):

    def __init__(self):
        self.manager = MemoryManager()

    def can_handle(self, prompt: str) -> bool:
        memory_keywords = [
            "my name is", "i live in", "i am", "i like", "i prefer",
            "i am working on", "my goal is", "remember",
            "what is my name", "where do i live",
            "what are my projects", "what are my goals",
            "what do you know about me",
        ]
        text = prompt.strip().lower()
        return any(kw in text for kw in memory_keywords)

    def execute(self, prompt: str):
        self.log_execution(prompt, None)
        results = self.manager.remember(prompt)
        if results:
            names = [m.content for m in results]
            result = f"Got it. I'll remember: {', '.join(names)}."
            self.log_execution(prompt, result)
            return result

        # For query-style prompts, use retriever
        relevant = self.manager.get_relevant_memories(prompt, top_k=5)
        if relevant:
            lines = [f"{m.memory_type.value.upper()}: {m.content}" for m in relevant]
            result = "\n".join(lines) if lines else "I don't know."
            self.log_execution(prompt, result)
            return result

        self.log_execution(prompt, None, error="No memory results")
        return None