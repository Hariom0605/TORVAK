from pathlib import Path

from core.rag.answer_generator import AnswerGenerator
from core.rag.document_manager import DocumentManager
from core.rag.embedding_engine import EmbeddingEngine
from core.rag.models import DocumentRecord
from core.rag.pdf_loader import PDFLoader
from core.rag.recursive_chunker import TextChunker
from core.rag.vector_store import VectorStore


class RAGEngine:

    def __init__(self):

        self.loader = PDFLoader()

        self.chunker = TextChunker()

        self.embedding_engine = EmbeddingEngine()

        self.vector_store = VectorStore()

        self.document_manager = DocumentManager()

        self.answer_generator = AnswerGenerator()

        self.vector_store.load()

    def index_document(
        self,
        pdf_path: str
    ) -> DocumentRecord:

        document, pages = self.loader.load_document(
            pdf_path
        )

        if self.document_manager.document_exists(
            document.document_id
        ):

            raise ValueError(
                "Document already indexed."
            )

        chunks = self.chunker.chunk_document(
            document,
            pages
        )

        embeddings = self.embedding_engine.embed_chunks(
            chunks
        )

        self.vector_store.add_chunks(
            chunks,
            embeddings
        )

        self.vector_store.save()

        self.document_manager.add_document(
            document
        )

        return document

    def ask(
        self,
        question: str,
        top_k: int = 5
    ):

        return self.answer_generator.generate(
            question=question,
            top_k=top_k
        )

    def remove_document(
        self,
        document_id: str
    ):

        self.vector_store.delete_document(
            document_id
        )

        self.document_manager.remove_document(
            document_id
        )

    def list_documents(self):

        return self.document_manager.list_documents()

    def clear_database(self):

        self.vector_store.clear()

        self.document_manager.clear()

    def stats(self):

        return {

            "documents":
                len(
                    self.document_manager.list_documents()
                ),

            "chunks":
                self.vector_store.total_chunks,

            "vectors":
                self.vector_store.total_vectors

        }

    def rebuild_index(self):

        documents = self.document_manager.list_documents()

        self.vector_store.clear()

        for document in documents:

            if not Path(
                document.source_path
            ).exists():

                continue

            _, pages = self.loader.load_document(
                document.source_path
            )

            chunks = self.chunker.chunk_document(
                document,
                pages
            )

            embeddings = self.embedding_engine.embed_chunks(
                chunks
            )

            self.vector_store.add_chunks(
                chunks,
                embeddings
            )

        self.vector_store.save()