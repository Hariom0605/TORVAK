from dataclasses import dataclass

from core.rag.context_builder import ContextBuilder
from core.rag.llm_engine import LLMEngine
from core.rag.prompt_builder import PromptBuilder
from core.rag.retriever import Retriever


@dataclass
class RAGResponse:
    answer: str
    sources: list[dict]
    retrieved_chunks: int


class AnswerGenerator:

    def __init__(self):

        self.retriever = Retriever()
        self.context_builder = ContextBuilder()
        self.prompt_builder = PromptBuilder()
        self.llm = LLMEngine()

    def generate(
        self,
        question: str,
        top_k: int = 5
    ) -> RAGResponse:

        results = self.retriever.retrieve(
            query=question,
            top_k=top_k
        )

        if not results:

            return RAGResponse(
                answer="I couldn't find the answer in the indexed documents.",
                sources=[],
                retrieved_chunks=0
            )

        context = self.context_builder.build_context(
            results
        )

        sources = self.context_builder.build_sources(
            results
        )

        prompt = self.prompt_builder.build_prompt(
            question=question,
            context=context
        )

        answer = self.llm.generate(
            prompt=prompt
        )

        return RAGResponse(
            answer=answer,
            sources=sources,
            retrieved_chunks=len(results)
        )