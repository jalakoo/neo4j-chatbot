from llm_base import LLMBase
import openai

class LLMOpenAI(LLMBase):

    def __init__(self, model:str, key:str):
        self.model = model
        openai.api_key = key
    
    def chat_completion(self, prior_messages: list[any]):
       return openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in prior_messages
            ],
            stream=True,
        )
