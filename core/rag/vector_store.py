import os
import pickle

import faiss
import numpy as np

from core.rag.models import ChunkRecord, SearchResult


class VectorStore:

    def __init__(
        self,
        dimension=384,
        index_path="memory/vector_store/faiss.index",
        metadata_path="memory/vector_store/chunks.pkl"
    ):

        self.dimension = dimension

        self.index_path = index_path
        self.metadata_path = metadata_path

        os.makedirs(
            os.path.dirname(index_path),
            exist_ok=True
        )

        self.index = faiss.IndexFlatIP(self.dimension)

        self.chunks: list[ChunkRecord] = []

    def add_chunks(
        self,
        chunks: list[ChunkRecord],
        embeddings: np.ndarray
    ):

        if len(chunks) != len(embeddings):
            raise ValueError(
                "Chunks and embeddings count mismatch."
            )

        embeddings = embeddings.astype(np.float32)

        self.index.add(embeddings)

        self.chunks.extend(chunks)

        print(f"[RAG] Indexed {len(chunks)} chunks.")

    def search(
        self,
        query_embedding: np.ndarray,
        top_k=5
    ) -> list[SearchResult]:

        if self.index.ntotal == 0:
            return []

        query_embedding = np.array(
            [query_embedding],
            dtype=np.float32
        )

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, idx in zip(scores[0], indices[0]):

            if idx == -1:
                continue

            results.append(

                SearchResult(
                    chunk=self.chunks[idx],
                    score=float(score)
                )

            )

        return results

    def save(self):

        faiss.write_index(
            self.index,
            self.index_path
        )

        with open(
            self.metadata_path,
            "wb"
        ) as file:

            pickle.dump(
                self.chunks,
                file
            )

        print("[RAG] Vector Store Saved.")

    def load(self):

        if not os.path.exists(self.index_path):
            return

        self.index = faiss.read_index(
            self.index_path
        )

        with open(
            self.metadata_path,
            "rb"
        ) as file:

            self.chunks = pickle.load(file)

        print("[RAG] Vector Store Loaded.")

    def delete_document(
        self,
        document_id: str
    ):

        remaining_chunks = [

            chunk

            for chunk in self.chunks

            if chunk.document_id != document_id

        ]

        self.rebuild(remaining_chunks)

    def rebuild(
        self,
        chunks: list[ChunkRecord]
    ):

        self.index = faiss.IndexFlatIP(
            self.dimension
        )

        self.chunks = []

        if not chunks:
            self.save()
            return

        from core.rag.embedding_engine import (
            EmbeddingEngine
        )

        engine = EmbeddingEngine()

        embeddings = engine.embed_chunks(
            chunks
        )

        self.add_chunks(
            chunks,
            embeddings
        )

        self.save()

    def clear(self):

        self.index = faiss.IndexFlatIP(
            self.dimension
        )

        self.chunks = []

        self.save()

    @property
    def total_chunks(self):

        return len(self.chunks)

    @property
    def total_vectors(self):

        return self.index.ntotal