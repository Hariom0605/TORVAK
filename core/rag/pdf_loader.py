import os
import uuid
from datetime import datetime

import fitz

from core.rag.models import DocumentRecord


class PDFLoader:

    def load_document(self, pdf_path: str):

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"File not found: {pdf_path}")

        if not pdf_path.lower().endswith(".pdf"):
            raise ValueError("Only PDF files are supported.")

        pdf = fitz.open(pdf_path)

        pages = []

        for page in pdf:

            text = page.get_text("text").strip()

            if text:
                pages.append(
                    {
                        "page_number": page.number + 1,
                        "text": text
                    }
                )

        metadata = pdf.metadata

        document = DocumentRecord(
            document_id=str(uuid.uuid4()),
            title=metadata.get("title") or os.path.basename(pdf_path),
            source_path=os.path.abspath(pdf_path),
            file_type="pdf",
            total_pages=len(pdf),
            created_at=datetime.now().isoformat()
        )

        pdf.close()

        return document, pages