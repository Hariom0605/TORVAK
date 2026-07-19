import json
import os
from dataclasses import asdict
from datetime import datetime
from typing import Dict, List
from core.rag.models import DocumentRecord


class DocumentManager:

    def __init__(self, manifest_path="memory/documents.json"):
        self.manifest_path = manifest_path
        os.makedirs(os.path.dirname(self.manifest_path), exist_ok=True)
        self.documents: Dict[str, DocumentRecord] = {}
        self.load_manifest()

    def load_manifest(self):
        if not os.path.exists(self.manifest_path):
            return
        with open(self.manifest_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        self.documents = {
            doc["document_id"]: DocumentRecord(**doc)
            for doc in data
        }

    def save_manifest(self):
        data = [
            asdict(document)
            for document in self.documents.values()
        ]
        with open(self.manifest_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def add_document(self, document: DocumentRecord):
        self.documents[document.document_id] = document
        self.save_manifest()

    def remove_document(self, document_id: str):
        if document_id in self.documents:
            del self.documents[document_id]
            self.save_manifest()

    def get_document(self, document_id: str):
        return self.documents.get(document_id)
    
    def list_documents(self) -> List[DocumentRecord]:
        return list(self.documents.values())

    def document_exists(self, source_path: str) -> bool:
        return any(
            document.source_path == source_path
            for document in self.documents.values()
        )
    
    def clear(self):

        self.documents.clear()

        self.save_manifest()