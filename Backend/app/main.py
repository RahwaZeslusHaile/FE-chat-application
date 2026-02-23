
from fastapi import APIRouter,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.api.routes import messages,websocket
from repository.repository_in_memory import InMemoryMessageRepository
from services.message_service import MessageService
from long_polling.poller import LongPoller
from websocket.connection_manager import ConnectionManager

@asynccontextmanager
async def lifespan(app:FastAPI):
    repository = InMemoryMessageRepository()
    app.state.message_service = MessageService(repository)
    app.state.poller = LongPoller(app.state.message_service)
    app.state.ws_manager = ConnectionManager()

    yield

app = FastAPI(title="Chat API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
            "https://rahwafrontendchatapp.hosting.codeyourfuture.io",
            "https://frontendwschat.hosting.codeyourfuture.io",
            "http://localhost:5173",
            "http://localhost:5174",
            "http://127.0.0.1:5173",
            "http://127.0.0.1:5174"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(messages.router)
app.include_router(websocket.router)

@app.get("/")
@app.get("/health")
def health_check():
    return {"status": "ok", "service": "chat-api"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
