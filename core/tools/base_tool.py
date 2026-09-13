from abc import ABC, abstractmethod
from typing import Optional, Dict, Any


class BaseTool(ABC):

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None):
        self.name = name or self.__class__.__name__
        self.description = description or ""
        self.permissions = {"enabled": True, "requires_confirmation": False}
        self.execution_history: list[Dict[str, Any]] = []

    @abstractmethod
    def can_handle(self, prompt: str) -> bool:
        pass

    @abstractmethod
    def execute(self, prompt: str) -> Any:
        pass

    def log_execution(self, prompt: str, result: Any, error: Optional[str] = None):
        self.execution_history.append({
            "prompt": prompt,
            "result": str(result)[:200],
            "error": error,
            "timestamp": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
        })

    def reset(self):
        self.execution_history.clear()
