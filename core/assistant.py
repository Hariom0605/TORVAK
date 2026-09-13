from core.ai_engine import AIEngine
from core.router import AIRouter
from core.command_router import CommandRouter
from core.memory.manager import MemoryManager
from core.planner.planner import Planner


class Assistant:

    def __init__(self):

        self.ai = AIEngine()
        self.router = AIRouter(self.ai)
        self.command = CommandRouter()
        self.memory = MemoryManager()
        self.planner = Planner(memory=self.memory)

    def process(self, prompt):

        text = prompt.lower()

        # ---------------- MEMORY ---------------- #

        memory_results = self.memory.remember(prompt)

        if memory_results:
            names = [m.content for m in memory_results]
            return f"Got it. I'll remember: {', '.join(names)}."

        # Check for memory queries using new retriever
        if any(phrase in text for phrase in ["what is my name", "where do i live", "what are my projects", "what are my goals", "what do you know about me"]):
            relevant = self.memory.get_relevant_memories(prompt, top_k=5)
            if relevant:
                lines = [f"{m.memory_type.value.upper()}: {m.content}" for m in relevant]
                return "\n".join(lines) if lines else "I don't know."

        # ---------------- PLANNER ---------------- #
        plan = self.planner.build_plan(prompt)
        if plan.intent.value != "command" and (plan.steps or plan.context_memories):
            steps_str = " | ".join([f"{s.step_id}: {s.description}" for s in plan.steps])
            return f"Plan ({plan.intent.value}): {steps_str}"

        # ---------------- COMMANDS ---------------- #

        result = self.command.execute(text)

        if result != "Command Not Found":
            return result

        # ---------------- AI ---------------- #

        return self.router.route(prompt)