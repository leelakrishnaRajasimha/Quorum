from core.llm.gemini_provider import GeminiProvider
from core.llm.nvidia_provider import NvidiaProvider


class ProviderFactory:

    @staticmethod
    def get_provider(provider):

        providers = {
            "gemini": GeminiProvider,
            # "openai": OpenAIProvider,
            # "claude": ClaudeProvider,
            # "grok": GrokProvider,
            "nvidia": NvidiaProvider,
            # "openrouter": OpenRouterProvider,
        }

        if provider.lower() not in providers:
            raise ValueError(f"Provider '{provider}' is not supported.")

        return providers[provider.lower()]()