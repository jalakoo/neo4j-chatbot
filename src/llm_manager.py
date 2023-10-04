from llm_openai import LLMOpenAI
from llm_llama import LLMLama
from llm_type import LLMType

class LLMManager():

    def __init__(self, type:LLMType, model:str, key:str):
        if type == LLMType.LLAMA:
            self._llm = LLMLama(model, key)
        else:
             self._llm = LLMOpenAI(model, key)

    def chat_completion(self, prior_messages: list[any]):
        return self._llm.chat_completion(prior_messages)