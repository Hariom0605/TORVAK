from sentence_transformers import SentenceTransformer
import numpy as np

from core.rag.models import ChunkRecord


class EmbeddingEngine:

    def __init__(self, model_name="all-MiniLM-L6-v2"):

        print("[RAG] Loading embedding model...")

        self.model = SentenceTransformer(model_name)

        print("[RAG] Embedding model loaded.")

    def embed_text(self, text: str) -> np.ndarray:

        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embedding.astype(np.float32)

    def embed_chunks(self, chunks: list[ChunkRecord]):

        texts = [chunk.text for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embeddings.astype(np.float32)