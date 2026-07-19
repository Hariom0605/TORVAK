from core.rag.embedding_engine import EmbeddingEngine
from core.rag.vector_store import VectorStore

engine = EmbeddingEngine()

chunks = [
    "Machine Learning is a subset of Artificial Intelligence.",
    "Python is a programming language.",
    "Operating System manages computer resources.",
    "DBMS stores structured data.",
    "Computer Networks connect devices."
]

embeddings = engine.embed_chunks(chunks)

store = VectorStore()

store.add_embeddings(embeddings, chunks)

query = "What is machine learning?"

query_embedding = engine.embed_text(query)

results = store.search(query_embedding)

print("\nTop Results\n")

for i, result in enumerate(results, 1):

    print("=" * 60)

    print(f"Rank : {i}")

    print(f"Distance : {result['distance']:.4f}")

    print(result["chunk"])