from fastapi import Request,Depends;
from repository.repository_in_memory import InMemoryMessageRepository
from services.message_service import MessageService
from long_polling.poller import LongPoller
from websocket.connection_manager import ConnectionManager

def get_message_service(request: Request)->MessageService:
    return request.app.state.message_service

def get_poller(request: Request)->LongPoller:
    return request.app.state.poller

def get_ws_manager(request: Request)->ConnectionManager:
    return request.app.state.ws_manager