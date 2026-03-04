from app.core.config import settings
from .openai_provider import OpenAIProvider
from .openrouter_provider import OpenRouterProvider

def get_llm_provider():

    if settings.LLM_PROVIDER == "openrouter":
        return OpenRouterProvider()

    return OpenAIProvider()