from core.rag.embedding_engine import EmbeddingEngine
from core.rag.vector_store import VectorStore
from core.rag.models import SearchResult


class Retriever:

    def __init__(self):

        self.embedding_engine = EmbeddingEngine()

        self.vector_store = VectorStore()

        self.vector_store.load()

    def build_query_embedding(self, query: str):

        return self.embedding_engine.embed_text(query)

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        min_score: float = 0.30
    ) -> list[SearchResult]:

        query_embedding = self.build_query_embedding(query)

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        filtered_results = [

            result

            for result in results

            if result.score >= min_score

        ]

        return filtered_results

    def retrieve_by_document(
        self,
        query: str,
        document_id: str,
        top_k: int = 5
    ) -> list[SearchResult]:

        results = self.retrieve(
            query=query,
            top_k=top_k
        )

        return [

            result

            for result in results

            if result.chunk.document_id == document_id

        ]