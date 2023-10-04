import abc
from dataclasses import dataclass

@dataclass
class LLMBase(abc.ABC):

    # @staticmethod
    # @abc.abstractmethod
    # def empty():
    #     pass

    @abc.abstractclassmethod
    def chat_completion(self):
        pass