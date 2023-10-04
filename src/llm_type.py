from enum import Enum, unique

@unique
class LLMType(Enum):
    UNKNOWN = 0,
    OPENAI = 1,
    LLAMA = 2,