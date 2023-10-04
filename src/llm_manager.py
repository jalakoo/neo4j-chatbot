from llms.llm_openai import LLMOpenAI
from llms.llm_llama import LLMLama
from llms.llm_cypher_rag import LLMCypherRAG
from llms.llm_type import LLMType

class LLMManager():
    # Spins up actual LLM object based on type selection

    def __init__(self, type:LLMType, model:str, key:str):
        if type == LLMType.LLAMA:
            self._llm = LLMLama(model, key)
        elif type == LLMType.CYPHER_RAG:
            self._llm = LLMCypherRAG(model, key)
        else:
             self._llm = LLMOpenAI(model, key)

    # Langchain vector search takes neo4j creds directly,
    # so we'll confirm all the options to this style
    def chat_completion(self, 
                        prior_messages: list[any],
                        neo4j_uri: str,
                        neo4j_user: str,
                        neo4j_password: str):
        
        return self._llm.chat_completion(prior_messages,
                                         neo4j_uri,
                                         neo4j_user,
                                         neo4j_password)