from enum import Enum
from pydantic import BaseModel

class ReactionRequest(str, Enum):
    like: str = "like"
    dislike: str = "dislike"

class ReactionType(BaseModel):
    reaction_type: ReactionRequest