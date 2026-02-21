
from fastapi import APIRouter,FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import messages,websocket

app = FastAPI(title="Chat API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
            "https://rahwafrontendchatapp.hosting.codeyourfuture.io",
            "https://frontendwschat.hosting.codeyourfuture.io",
            "http://localhost:5173",
            "http://127.0.0.1:5173"
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
