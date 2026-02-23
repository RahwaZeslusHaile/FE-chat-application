from typing import Optional
from pydantic import BaseModel
from schemas.types import Username,MessageContent

class MessageRequest(BaseModel):
    username: Username
    content: MessageContent
    scheduled_for: Optional[str] = None
    text_color: Optional[str] = None
    is_bold: bool = False
    is_italic: bool = False


class ReplyRequest(BaseModel):
    username: str
    content: str
    scheduled_for: Optional[str] = None
    text_color: Optional[str] = None
    is_bold: bool = False
    is_italic: bool = False


class MessageResponse(BaseModel):
    id: str
    username: str
    content: str
    timestamp: str
    timestamp_iso: str
    parent_message_id: Optional[str] = None
    likes: int = 0
    dislikes: int = 0
    scheduled_for: Optional[str] = None
    text_color: Optional[str] = None
    is_bold: bool = False
    is_italic: bool = False