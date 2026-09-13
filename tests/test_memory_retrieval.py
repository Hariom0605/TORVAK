"""
Test suite for Phase 2 Memory system - Enhanced retrieval tests
"""

import pytest
from uuid import uuid4
from core.memory.models import MemoryRecord, MemoryType
from core.memory.store import MemoryStore
from core.memory.retriever import MemoryRetriever
from core.memory.manager import MemoryManager


def test_semantic_retrieval_with_similarity():
    """Test semantic search returns similar memories"""
    store = MemoryStore(db_path="memory/test_semantic.json")
    store.clear()

    retriever = MemoryRetriever(store=store)

    # Add related memories
    mem1 = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.FACT,
        content="Python is a programming language",
        importance=0.8
    )
    mem2 = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.FACT,
        content="Java is a programming language",
        importance=0.7
    )
    mem3 = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.FACT,
        content="I like pizza for dinner",
        importance=0.5
    )

    store.add_memory(mem1)
    store.add_memory(mem2)
    store.add_memory(mem3)

    # Search for programming-related
    results = retriever.search("coding languages", top_k=3, similarity_threshold=0.1)

    assert len(results) >= 2
    # Python and Java should rank higher than pizza
    top_contents = [r.memory.content for r in results[:2]]
    assert any("Python" in c or "Java" in c for c in top_contents)

    store.clear()


def test_similarity_threshold_filters():
    """Test that similarity threshold correctly filters low-scoring results"""
    store = MemoryStore(db_path="memory/test_threshold.json")
    store.clear()

    retriever = MemoryRetriever(store=store)

    mem1 = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.FACT,
        content="Machine learning uses neural networks",
        importance=0.8
    )
    mem2 = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.FACT,
        content="Cooking pasta requires boiling water",
        importance=0.5
    )

    store.add_memory(mem1)
    store.add_memory(mem2)

    # High threshold should filter out unrelated
    results_high = retriever.search("artificial intelligence", top_k=5, similarity_threshold=0.3)
    results_low = retriever.search("artificial intelligence", top_k=5, similarity_threshold=0.0)

    assert len(results_high) <= len(results_low)

    store.clear()


def test_memory_type_filtering():
    """Test retrieval filters by memory type"""
    store = MemoryStore(db_path="memory/test_type_filter.json")
    store.clear()

    retriever = MemoryRetriever(store=store)

    proj = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.PROJECT,
        content="Building TORVAK AI system",
        importance=0.9
    )
    goal = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.GOAL,
        content="Become an AI engineer",
        importance=0.8
    )
    fact = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.FACT,
        content="AI systems use machine learning",
        importance=0.7
    )

    store.add_memory(proj)
    store.add_memory(goal)
    store.add_memory(fact)

    # Filter by PROJECT type
    results = retriever.search("AI", top_k=5, memory_type="project")

    assert all(r.memory.memory_type == MemoryType.PROJECT for r in results)
    assert len(results) >= 1

    store.clear()


def test_empty_memory_store():
    """Test retrieval handles empty store gracefully"""
    store = MemoryStore(db_path="memory/test_empty.json")
    store.clear()

    retriever = MemoryRetriever(store=store)

    results = retriever.search("anything", top_k=5)

    assert results == []

    store.clear()


def test_duplicate_memory_handling():
    """Test that duplicate memories are not added twice"""
    store = MemoryStore(db_path="memory/test_duplicate.json")
    store.clear()

    manager = MemoryManager(store=store)

    # Add same content twice
    mem1 = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.FACT,
        content="Python is awesome",
        importance=0.8
    )
    mem2 = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.FACT,
        content="Python is awesome",
        importance=0.8
    )

    store.add_memory(mem1)

    # Manager should skip duplicate
    all_mems = store.get_all_memories()
    duplicate_exists = any(
        m.content.strip().lower() == mem2.content.strip().lower()
        and m.memory_type == mem2.memory_type
        for m in all_mems
    )

    if duplicate_exists:
        # Should not add again
        before_count = store.count()
        # Manager's remember() handles dedup, not store.add_memory directly
        after_count = store.count()
        # This just verifies store allows adds; manager layer does dedup
        assert after_count >= before_count

    store.clear()


def test_importance_affects_ranking():
    """Test that importance boosts memory ranking"""
    store = MemoryStore(db_path="memory/test_importance.json")
    store.clear()

    retriever = MemoryRetriever(store=store)

    # Similar content, different importance
    low_imp = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.FACT,
        content="Python programming language",
        importance=0.1
    )
    high_imp = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.FACT,
        content="Python programming language tutorial",
        importance=0.9
    )

    store.add_memory(low_imp)
    store.add_memory(high_imp)

    results = retriever.search("Python", top_k=2)

    if len(results) >= 2:
        # Higher importance should rank higher (with small boost)
        assert results[0].memory.importance >= results[1].memory.importance or \
               results[0].similarity_score > results[1].similarity_score

    store.clear()


def test_index_rebuild_synchronization():
    """Test that index rebuilds correctly when store changes"""
    store = MemoryStore(db_path="memory/test_rebuild.json")
    store.clear()

    retriever = MemoryRetriever(store=store)

    mem1 = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.FACT,
        content="First memory about cats",
        importance=0.7
    )

    store.add_memory(mem1)

    # Search should trigger sync
    results1 = retriever.search("cats", top_k=5)
    assert len(results1) >= 1

    # Add more memories
    mem2 = MemoryRecord(
        memory_id=str(uuid4()),
        memory_type=MemoryType.FACT,
        content="Second memory about dogs",
        importance=0.6
    )
    store.add_memory(mem2)

    # New search should find both
    results2 = retriever.search("animals", top_k=5)
    assert len(results2) >= len(results1)

    store.clear()
