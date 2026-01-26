from datetime import datetime
import time
from typing import Optional
from models import IMessage, Message, IMessageRepository, UsernameValidator, MessageContentValidator

class MessageService:
  
    def __init__(self, repository: IMessageRepository):
        self.repository = repository
    
    def create_message(self, username: str, content: str) -> IMessage:
        if not UsernameValidator.validate(username):
            raise ValueError(f"Invalid username: {username}")
        if not MessageContentValidator.validate(content):
            raise ValueError(f"Invalid message content: {content}")
        
        message = Message(username=username, content=content)
        self.repository.save(message)
        return message
    
    def get_message_by_id(self, message_id: str) -> Optional[IMessage]:
        return self.repository.get_by_id(message_id)
    
    def get_all_messages(self):
        return self.repository.get_all()

    def get_message_by_id(self, message_id: str) -> Optional[IMessage]:
        return self.repository.get_by_id(message_id)

    def get_messages_after(self, after_dt: datetime):
        messages = [msg for msg in self.repository.get_all() if msg.timestamp > after_dt]
        return sorted(messages, key=lambda m: m.timestamp.value, reverse=True)