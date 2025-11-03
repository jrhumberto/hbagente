from langchain core. language models import LLM
from typing import Optional, List
import requests
from dotenv import load_dotenv
import os

load_dotenv()

class CustomNvidiaLLM(LLM):
    """Minimal LangChain LLM wrapper for NVIDIA NIM."""
    model: str = "nvidia/llama-3.3-nemotron-super-49b-v1"
    temperature: float = 0.2
    max_tokens: int = 4096
    top_p: int = 0.95
    frequency_penalty: int = 0
    presence_penalty: int = 0
    stream: bool =True

    #model: str = "meta/llama3-70b-instruct"
    #temperature: float = 0.7
    #max_tokens: int = 1024

    api_key: str = os.getenv("NVIDIA_API_KEY")
    base_url: str = "https://integrate.api.nvidia.com/v1"

    @property
    def _llm_type(self) -> str:
        return "nvidia-nim"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        pay load = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "top_p": self.top_p,
            "frequency_penalty": self.frequency_penalty,
            "presence_penalty": self.presence_penalty,
            "stream": self.stream
        }
        url = f"{self.base_url}/chat/completions"
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            raise RuntimeError(f"NVIDIA NIM API error: {response.status_code} {response.text}")
        return response. json() ["choices"] [0] ["message"] ["content"]


def get_nvidia_llm():
    return CustomNvidiaLLM()


      
