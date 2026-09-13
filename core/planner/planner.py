from __future__ import annotations

import logging
from typing import Optional, List

from core.planner.models import Plan, PlanStep, IntentType, PlanStatus
from core.memory.manager import MemoryManager
from core.rag.retriever import Retriever
from core.tools.tool_registry import ToolRegistry

logger = logging.getLogger(__name__)


class Planner:
    def __init__(
        self,
        memory: Optional[MemoryManager] = None,
        retriever: Optional[Retriever] = None,
        registry: Optional[ToolRegistry] = None,
    ):
        self.memory = memory or MemoryManager()
        self.retriever = retriever or Retriever()
        self.registry = registry or ToolRegistry()

    def classify_intent(self, prompt: str) -> IntentType:
        text = prompt.lower()
        if any(w in text for w in ["what", "who", "why", "how", "explain", "tell me"]):
            return IntentType.QUESTION
        if any(w in text for w in ["write", "create", "build", "generate", "fix", "debug", "code", "program"]):
            return IntentType.CODING
        if any(w in text for w in ["remember", "memory", "my name", "my goal", "project", "what do you know"]):
            return IntentType.MEMORY
        if any(w in text for w in ["research", "search", "find info", "look up", "web"]):
            return IntentType.RESEARCH
        if any(w in text for w in ["plan", "step by step", "how to do", "break down"]):
            return IntentType.PLAN
        return IntentType.COMMAND

    def build_plan(self, prompt: str) -> Plan:
        from uuid import uuid4
        plan_id = str(uuid4())
        intent = self.classify_intent(prompt)
        plan = Plan(plan_id=plan_id, intent=intent, query=prompt)

        # Memory retrieval
        relevant = self.memory.get_relevant_memories(prompt, top_k=3)
        plan.context_memories = [m.memory_id for m in relevant]

        # RAG retrieval (if document-related)
        try:
            rag = self.retriever.retrieve(prompt, top_k=3)
            plan.rag_results = [r.chunk.text[:100] for r in rag] if rag else []
        except Exception as exc:
            logger.debug("RAG retrieval failed: %s", exc)

        # Structured steps based on intent
        if intent == IntentType.CODING:
            plan.steps = [
                PlanStep(step_id="s1", description="Analyze requirements from prompt"),
                PlanStep(step_id="s2", description="Retrieve code context and memories"),
                PlanStep(step_id="s3", description="Generate solution / fix"),
                PlanStep(step_id="s4", description="Present result and store learnings"),
            ]
        elif intent == IntentType.RESEARCH:
            plan.steps = [
                PlanStep(step_id="s1", description="Clarify research scope"),
                PlanStep(step_id="s2", description="Search web / RAG sources"),
                PlanStep(step_id="s3", description="Synthesize findings"),
                PlanStep(step_id="s4", description="Deliver structured answer"),
            ]
        elif intent == IntentType.MEMORY:
            plan.steps = [
                PlanStep(step_id="s1", description="Extract relevant memories"),
                PlanStep(step_id="s2", description="Update or confirm memory"),
            ]
        else:
            plan.steps = [
                PlanStep(step_id="s1", description="Understand user intent"),
                PlanStep(step_id="s2", description="Retrieve context (memory + RAG)"),
                PlanStep(step_id="s3", description="Generate response using LLM"),
            ]

        return plan

    def execute_step(self, plan: Plan, step_index: int) -> str:
        if step_index >= len(plan.steps):
            plan.complete()
            return "Plan complete."
        step = plan.steps[step_index]
        # In a full implementation, this would invoke tools, LLM, etc.
        # Here we mark progress and return a status.
        step.completed = True
        return f"Step {step.step_id}: {step.description} — completed."

    def select_tools(self, plan: Plan) -> List[str]:
        hints = []
        for step in plan.steps:
            if step.tool_hint:
                hints.append(step.tool_hint)
        # Deduplicate and pick from registry by capability
        selected = []
        for hint in set(hints):
            tool = self.registry.find_by_capability(hint)
            if tool and tool.__class__.__name__ not in [t.__class__.__name__ for t in selected]:
                selected.append(tool)
        return [t.__class__.__name__ for t in selected]
