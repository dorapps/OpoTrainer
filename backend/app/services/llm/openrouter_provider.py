from openai import OpenAI
from app.core.config import settings
from .base import LLMProvider

class OpenRouterProvider(LLMProvider):

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )

    def generate(self, system_prompt: str, user_prompt: str) -> str:

        response = self.client.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content