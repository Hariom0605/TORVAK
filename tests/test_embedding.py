from core.rag.embedding_engine import EmbeddingEngine

engine = EmbeddingEngine()

chunks = [
    "Machine learning is a subset of Artificial Intelligence.",
    "Deep learning uses neural networks.",
    "Python is a popular programming language."
]

embeddings = engine.embed_chunks(chunks)

print("\nShape :", embeddings.shape)
print("\nFirst 10 values of first embedding:\n")
print(embeddings[0][:10])