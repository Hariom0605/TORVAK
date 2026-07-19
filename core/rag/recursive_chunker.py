import uuid

from langchain_text_splitters import RecursiveCharacterTextSplitter

from core.rag.models import ChunkRecord


class TextChunker:

    def __init__(
        self,
        chunk_size=800,
        chunk_overlap=150
    ):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def chunk_document(self, document, pages):

        chunks = []

        for page in pages:

            page_chunks = self.splitter.split_text(
                page["text"]
            )

            for text in page_chunks:

                chunk = ChunkRecord(
                    chunk_id=str(uuid.uuid4()),
                    document_id=document.document_id,
                    page_number=page["page_number"],
                    text=text
                )

                chunks.append(chunk)

        return chunks