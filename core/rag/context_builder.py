from core.rag.models import SearchResult


class ContextBuilder:

    def __init__(self, max_context_length: int = 4000):

        self.max_context_length = max_context_length

    def build_context(
        self,
        results: list[SearchResult]
    ):

        if not results:
            return ""

        context = []
        used_chunks = set()
        current_length = 0

        for result in results:

            chunk = result.chunk

            if chunk.chunk_id in used_chunks:
                continue

            text = chunk.text.strip()

            if not text:
                continue

            source = (
                f"[Source: {chunk.document_id} | "
                f"Page: {chunk.page_number}]"
            )

            block = f"{source}\n{text}\n"

            if current_length + len(block) > self.max_context_length:
                break

            context.append(block)

            used_chunks.add(chunk.chunk_id)

            current_length += len(block)

        return "\n".join(context)

    def build_sources(
        self,
        results: list[SearchResult]
    ):

        sources = []

        seen = set()

        for result in results:

            chunk = result.chunk

            key = (
                chunk.document_id,
                chunk.page_number
            )

            if key in seen:
                continue

            seen.add(key)

            sources.append(
                {
                    "document_id": chunk.document_id,
                    "page_number": chunk.page_number
                }
            )

        return sources