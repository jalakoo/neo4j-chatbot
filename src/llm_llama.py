from llm_base import LLMBase

class LLMLama(LLMBase):

    def __init__(self, model:str, key:str):
        self.model = model
        self.key = key

    def chat_completion(self):
        raise Exception("Unimplemented")