from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional


class PlanStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


class IntentType(Enum):
    QUESTION = "question"
    COMMAND = "command"
    MEMORY = "memory"
    CODING = "coding"
    RESEARCH = "research"
    PLAN = "plan"


@dataclass
class PlanStep:
    step_id: str
    description: str
    tool_hint: Optional[str] = None
    expected_output: Optional[str] = None
    completed: bool = False


@dataclass
class Plan:
    plan_id: str
    intent: IntentType
    query: str
    steps: List[PlanStep] = field(default_factory=list)
    status: PlanStatus = PlanStatus.PENDING
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: Optional[datetime] = None
    context_memories: List[str] = field(default_factory=list)
    rag_results: List[str] = field(default_factory=list)
    error_message: Optional[str] = None

    def complete(self):
        self.status = PlanStatus.COMPLETED
        self.completed_at = datetime.now(timezone.utc)

    def fail(self, message: str):
        self.status = PlanStatus.FAILED
        self.error_message = message
