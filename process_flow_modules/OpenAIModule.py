import os
import openai


class OpenAIModule(object):
    _is_initialized = False

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(OpenAIModule, cls).__new__(cls)
        return cls.instance

    def __init__(self, api_type, api_base, api_version, engine, organization, api_key):
        self.api_type = api_type
        self.api_base = api_base
        self.api_version = api_version
        self.engine = engine
        self.organization = organization
        self.api_key = api_key
        self._is_initialized = True

    def create_gpt_model(self, messages, temperature=0.3, max_tokens=3000):
        openai.api_type = self.api_type
        openai.api_base = self.api_base
        openai.api_version = self.api_version
        openai.api_key = self.api_key
        openai.organization = self.organization

        response = openai.ChatCompletion.create(
            engine=self.engine,
            temperature=temperature,
            max_tokens=max_tokens,
            messages=messages,

        )
        return response.choices[0].message.content