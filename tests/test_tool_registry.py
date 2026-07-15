import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def test_registry_prefers_memory_tool_without_double_execution(monkeypatch):
    import core.tools.tool_registry as tool_registry_module

    calls = []

    class FakeMemoryTool:
        def __init__(self):
            self.name = "memory"

        def can_handle(self, prompt):
            calls.append(("memory", prompt))
            return True

        def execute(self, prompt):
            calls.append(("memory-exec", prompt))
            return "memory-result"

    class FakeCommandTool:
        def __init__(self):
            self.name = "command"

        def can_handle(self, prompt):
            calls.append(("command", prompt))
            return False

        def execute(self, prompt):
            calls.append(("command-exec", prompt))
            return "command-result"

    class FakeAITool:
        def __init__(self):
            self.name = "ai"

        def can_handle(self, prompt):
            calls.append(("ai", prompt))
            return False

        def execute(self, prompt):
            calls.append(("ai-exec", prompt))
            return "ai-result"

    monkeypatch.setattr(tool_registry_module, "MemoryTool", FakeMemoryTool)
    monkeypatch.setattr(tool_registry_module, "CommandTool", FakeCommandTool)
    monkeypatch.setattr(tool_registry_module, "AITool", FakeAITool)

    registry = tool_registry_module.ToolRegistry()

    result = registry.handle("my name is Alice")

    assert result == "memory-result"
    assert calls.count(("memory", "my name is Alice")) == 1
    assert calls.count(("memory-exec", "my name is Alice")) == 1
