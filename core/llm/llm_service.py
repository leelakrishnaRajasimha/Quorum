from core.llm.provider_factory import ProviderFactory


class LLMService:

    def __init__(self, provider="gemini"):

        self.provider = ProviderFactory.get_provider(provider)

    def generate(self, prompt):

        return self.provider.generate_text(prompt)