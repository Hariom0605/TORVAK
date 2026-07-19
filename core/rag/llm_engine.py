import requests


class LLMEngine:

    def __init__(
        self,
        model: str = "llama3.1:8b",
        base_url: str = "http://localhost:11434"
    ):

        self.model = model
        self.base_url = base_url.rstrip("/")

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2,
        max_tokens: int = 1024
    ) -> str:

        url = f"{self.base_url}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens
            }
        }

        try:

            response = requests.post(
                url,
                json=payload,
                timeout=300
            )

            response.raise_for_status()

            data = response.json()

            return data.get("response", "").strip()

        except requests.exceptions.RequestException as e:

            raise RuntimeError(
                f"Unable to connect to Ollama: {e}"
            )

        except Exception as e:

            raise RuntimeError(
                f"LLM Generation Failed: {e}"
            )