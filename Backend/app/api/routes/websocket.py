from fastapi import APIRouter,WebSocket,Depends

from Backend.core.dependencies import get_message_service,get_poller,get_ws_manager
from services.message_service import MessageService
from websocket.handlers import handle_websocket
from websocket.connection_manager import ConnectionManager

router = APIRouter()

@ router.websocket("/ws")
async def websocket_endpoint(
    websocket:WebSocket,
    ws_manager:ConnectionManager = Depends(get_ws_manager),
    message_service: MessageService = Depends(get_message_service),
):
    await handle_websocket(websocket,ws_manager,message_service)
