from enum import Enum, unique

@unique
class LLMType(Enum):
    UNKNOWN = 0,
    OPENAI = 1,
    LLAMA = 2,
    VECTOR = 3,
    CYPHER_RAG = 4

    def to_string(self) -> str:
        """
        Convert a LLMType enum value to its corresponding string representation.

        Returns:
            str: The string representation of the GeneratorType enum value.

        Raises:
            TypeError: If the GeneratorType enum value is not supported.
        """
        type_map = {
            LLMType.OPENAI: "OpenAI",
            LLMType.CYPHER_RAG: "CypherRag",
            LLMType.VECTOR: "Vector Search",
        }
        result = type_map.get(self, None)
        if result is None:
            raise TypeError(f"{self} type not supported")
        return result
    
    @staticmethod
    def type_from_string(aType: str):
        type = aType.lower()
        if type == "openai":
            return LLMType.OPENAI
        elif type == "cypherrag" or type == "cypher rag":
            return LLMType.CYPHER_RAG
        elif type == "vector":
            return LLMType.VECTOR
        else:
            raise TypeError("Type not supported")