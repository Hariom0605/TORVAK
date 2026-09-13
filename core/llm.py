import os
from abc import ABC, abstractmethod
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


class BaseLLM(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class GeminiLLM(BaseLLM):
    def __init__(
        self,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
    ):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found.")

        try:
            from google import genai
        except ImportError as exc:
            raise RuntimeError("google-genai is required for the Gemini provider.") from exc

        self.client = genai.Client(api_key=api_key)
        model_name = model or os.getenv("LLM_MODEL", "gemini-2.5-flash")
        self.model_name = model_name

        temp_value = temperature
        if temp_value is None:
            raw_temp = os.getenv("LLM_TEMPERATURE", "0.2")
            try:
                temp_value = float(raw_temp)
            except ValueError:
                temp_value = 0.2
        self.temperature = temp_value

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                temperature=self.temperature,
            ),
        )
        text = getattr(response, "text", "")
        if not text:
            return ""
        return text.strip()


class LLM:
    def __init__(
        self,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
    ):
        provider_name = (provider or os.getenv("LLM_PROVIDER", "gemini")).lower()
        self.provider = provider_name

        if provider_name == "gemini":
            self.client = GeminiLLM(model=model, temperature=temperature)
        else:
            raise ValueError(f"Unsupported LLM Provider: {provider_name}")

    def generate(self, prompt: str) -> str:
        return self.client.generate(prompt)
