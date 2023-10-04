from llms.llm_base import LLMBase

class LLMLama(LLMBase):

    def __init__(self, model:str, key:str):
        self.model = model
        self.key = key

    def chat_completion(self,
                        prior_messages: list[any],
                        neo4j_uri: str,
                        neo4j_user: str,
                        neo4j_password: str):
        raise Exception("Unimplemented")