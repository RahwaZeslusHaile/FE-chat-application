from fastapi import APIRouter,WebSocket,Depends

from core.dependencies import get_message_service,get_poller,get_ws_manager
from services.message_service import MessageService
from websocket.handlers import handle_websocket
from websocket.connection_manager import ConnectionManager

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket):
    ws_manager = websocket.app.state.ws_manager
    message_service = websocket.app.state.message_service
    await handle_websocket(websocket,ws_manager,message_service)
