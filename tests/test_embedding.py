from core.rag.embedding_engine import EmbeddingEngine
from core.rag.models import ChunkRecord

engine = EmbeddingEngine()

chunks = [
    ChunkRecord(chunk_id="1", document_id="doc1", page_number=1, text="Machine learning is a subset of Artificial Intelligence."),
    ChunkRecord(chunk_id="2", document_id="doc1", page_number=1, text="Deep learning uses neural networks."),
    ChunkRecord(chunk_id="3", document_id="doc1", page_number=1, text="Python is a popular programming language.")
]

embeddings = engine.embed_chunks(chunks)

print("\nShape :", embeddings.shape)
print("\nFirst 10 values of first embedding:\n")
print(embeddings[0][:10])