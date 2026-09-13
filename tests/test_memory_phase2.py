from datetime import datetime

import pytest

from core.memory.manager import MemoryManager
from core.memory.models import MemoryRecord, MemorySearchResult, MemoryType
from core.memory.store import MemoryStore
from core.memory.extractor import MemoryExtractor


def test_memory_record_round_trip():
    original = MemoryRecord(
        memory_id="m-1",
        memory_type=MemoryType.PREFERENCE,
        content="User prefers Python",
        importance=0.9,
        metadata={"source": "user"},
    )

    serialized = original.to_dict()
    restored = MemoryRecord.from_dict(serialized)

    assert restored.memory_id == original.memory_id
    assert restored.memory_type == MemoryType.PREFERENCE
    assert restored.content == original.content
    assert restored.importance == pytest.approx(0.9)
    assert restored.metadata == {"source": "user"}


def test_memory_store_crud_and_backup_restore(tmp_path):
    db_path = tmp_path / "memory.json"
    backup_path = tmp_path / "backup.json"
    store = MemoryStore(str(db_path), str(backup_path))

    record = MemoryRecord(
        memory_id="m-1",
        memory_type=MemoryType.PROFILE,
        content="User name is Alice",
        importance=1.0,
        metadata={"source": "user"},
    )

    store.add_memory(record)
    assert store.count() == 1
    assert store.get_memory("m-1").content == "User name is Alice"

    updated = MemoryRecord(
        memory_id="m-1",
        memory_type=MemoryType.PROFILE,
        content="User name is Alice Smith",
        importance=1.0,
        metadata={"source": "user"},
    )
    assert store.update_memory(updated) is True

    assert store.get_memory("m-1").content == "User name is Alice Smith"
    assert store.delete_memory("m-1") is True
    assert store.count() == 0

    store.add_memory(record)
    store.backup()
    store.clear()
    assert store.count() == 0
    store.restore()
    assert store.count() == 1


def test_memory_extractor_parses_valid_json_and_rejects_invalid(monkeypatch):
    class FakeLLM:
        def generate(self, prompt):
            return '[{"memory_type":"preference","content":"User prefers Python","importance":0.8,"metadata":{"source":"user"}}]'

    extractor = MemoryExtractor(llm=FakeLLM())
    events = extractor.extract("I prefer Python over Java.")

    assert len(events) == 1
    assert events[0].memory_type == MemoryType.PREFERENCE
    assert events[0].content == "User prefers Python"
    assert events[0].importance == pytest.approx(0.8)

    class BadLLM:
        def generate(self, prompt):
            return "not json"

    bad_extractor = MemoryExtractor(llm=BadLLM())
    assert bad_extractor.extract("hello") == []


def test_memory_manager_remembers_unique_records_and_searches(monkeypatch, tmp_path):
    class FakeLLM:
        def generate(self, prompt):
            return '[{"memory_type":"project","content":"User is building TORVAK","importance":0.9,"metadata":{"source":"user"}}]'

    store = MemoryStore(str(tmp_path / "memory.json"), str(tmp_path / "backup.json"))
    manager = MemoryManager(store=store, llm=FakeLLM())

    first = manager.remember("I am building TORVAK")
    second = manager.remember("I am building TORVAK")

    assert len(first) == 1
    assert len(second) == 0
    assert manager.get_stats().project_count == 1

    results = manager.search("TORVAK project plan")
    assert results
    assert results[0].memory.content == "User is building TORVAK"


def test_memory_type_validation_rejects_invalid_values():
    with pytest.raises(ValueError):
        MemoryType.validate("unknown")
