from core.rag.embedding_engine import EmbeddingEngine
from core.rag.vector_store import VectorStore
from core.rag.models import ChunkRecord

engine = EmbeddingEngine()

chunks = [
    ChunkRecord(chunk_id="1", document_id="doc1", page_number=1, text="Machine Learning is a subset of Artificial Intelligence."),
    ChunkRecord(chunk_id="2", document_id="doc1", page_number=1, text="Python is a programming language."),
    ChunkRecord(chunk_id="3", document_id="doc1", page_number=1, text="Operating System manages computer resources."),
    ChunkRecord(chunk_id="4", document_id="doc1", page_number=1, text="DBMS stores structured data."),
    ChunkRecord(chunk_id="5", document_id="doc1", page_number=1, text="Computer Networks connect devices.")
]

embeddings = engine.embed_chunks(chunks)

store = VectorStore()

store.add_chunks(chunks, embeddings)

query = "What is machine learning?"

query_embedding = engine.embed_text(query)

results = store.search(query_embedding, top_k=5)

print("\nTop Results\n")

for i, result in enumerate(results, 1):
    print(f"Rank {i}: {result.chunk.text[:50]}... (score: {result.score:.4f})")