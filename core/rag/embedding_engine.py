import hashlib

import numpy as np

from core.rag.models import ChunkRecord

try:
    from sentence_transformers import SentenceTransformer
except ImportError:  # pragma: no cover - optional dependency at runtime
    SentenceTransformer = None


class EmbeddingEngine:

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.model = None

        if SentenceTransformer is not None:
            print("[RAG] Loading embedding model...")
            self.model = SentenceTransformer(model_name)
            print("[RAG] Embedding model loaded.")

    def _fallback_embedding(self, text: str, dimension: int = 32) -> np.ndarray:
        vector = np.zeros(dimension, dtype=np.float32)
        tokens = [token.lower() for token in text.replace("\n", " ").split() if token.strip()]
        if not tokens:
            return vector

        for index, token in enumerate(tokens[:dimension]):
            digest = int(hashlib.sha256(token.encode("utf-8")).hexdigest()[:8], 16)
            vector[index % dimension] += float(digest % 97) / 97.0

        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
        return vector

    def embed_text(self, text: str) -> np.ndarray:
        if self.model is None:
            return self._fallback_embedding(text)

        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embedding.astype(np.float32)

    def embed_chunks(self, chunks):
        if self.model is None:
            texts = [chunk.text if hasattr(chunk, 'text') else str(chunk) for chunk in chunks]
            return np.stack([self._fallback_embedding(t) for t in texts]).astype(np.float32)

        texts = [chunk.text if hasattr(chunk, 'text') else str(chunk) for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embeddings.astype(np.float32)