from abc import ABC, abstractmethod


class BaseTool(ABC):

    @abstractmethod
    def can_handle(self, prompt: str) -> bool:
        pass

    @abstractmethod
    def execute(self, prompt: str):
        pass