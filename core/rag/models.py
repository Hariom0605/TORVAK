from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DocumentRecord:
    document_id: str
    title: str
    source_path: str
    file_type: str
    total_pages: int
    created_at: str


@dataclass
class ChunkRecord:
    chunk_id: str
    document_id: str
    page_number: int
    text: str


@dataclass
class SearchResult:
    chunk: ChunkRecord
    score: float