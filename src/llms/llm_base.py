import abc
from dataclasses import dataclass

@dataclass
class LLMBase(abc.ABC):

    # @staticmethod
    # @abc.abstractmethod
    # def empty():
    #     pass

    @abc.abstractclassmethod
    def chat_completion(self,
                        prior_messages: list[any],
                        neo4j_uri: str,
                        neo4j_user: str,
                        neo4j_password: str):
        pass