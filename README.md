# FE Chat Application

A simple real-time chat application with a React frontend and a Python backend. Communication is implemented via REST endpoints and long-polling for near-real-time updates.

## Features

- Send and receive messages
- View messages from other users with timestamps
- Real-time updates via **WebSocket** or **Long-Polling**
- Message reactions (like / dislike) — stretch goal
- Reply, formatting, and color options — optional
- Automatic reconnection and connection status indicator

## Prerequisites

- Node.js (16+ recommended) and npm
- Python 3.8+ and virtualenv (for backend)

## Getting Started

1. Clone the repository

```bash
git clone <your-repo-url>
cd React-chat-app
```

2. Backend

```bash
cd Backend
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
# venv\Scripts\activate  # Windows (PowerShell)
pip install -r requirements.txt
python app.py
```

3. Frontend

```bash
cd Frontend
npm install
npm run dev    
```

Open the frontend URL shown by the dev server (usually http://localhost:3000 or http://localhost:5173).

## Project Structure

### Backend Architecture

The backend follows a clean architecture pattern with separation of concerns:

```
Backend/
├── app/
│   ├── main.py                    # FastAPI application entry point with lifespan management
│   ├── api/
│   │   └── routes/
│   │       ├── messages.py        # REST API endpoints for messages
│   │       └── websocket.py       # WebSocket connection endpoint
│   ├── core/
│   │   └── dependencies.py        # Dependency injection utilities
│   ├── domain/
│   │   └── message_model.py       # Domain model for messages
│   ├── repository/
│   │   ├── repository_base.py     # Abstract repository interface
│   │   ├── repository_in_memory.py # In-memory implementation
│   │   └── repository.py          # Repository pattern implementations
│   ├── schemas/
│   │   ├── message.py             # Pydantic schemas for messages
│   │   ├── reaction.py            # Pydantic schemas for reactions
│   │   └── types.py               # Custom type definitions
│   ├── services/
│   │   └── message_service.py     # Business logic for message operations
│   ├── validators/
│   │   └── validators.py          # Input validation logic
│   ├── long_polling/
│   │   └── poller.py              # Long-polling implementation
│   └── websocket/
│       ├── connection_manager.py  # WebSocket connection manager
│       └── handlers.py            # WebSocket message handlers
└── requirements.txt
```

**Dependency Flow:**
- **Repository Layer**: Data access abstraction (repository_in_memory.py)
- **Service Layer**: Business logic (message_service.py) → uses Repository
- **Long Polling**: Poller (poller.py) → uses Service
- **WebSocket**: ConnectionManager + Handlers → uses Service
- **API Routes**: REST endpoints → use Service via dependency injection

### Frontend Structure

```
Frontend/
├── src/
│   ├── components/
│   │   ├── ChatWindow.jsx         # Main chat container
│   │   ├── Header.jsx             # Application header
│   │   ├── MessageInput.jsx       # Message input component
│   │   ├── MessageItem.jsx        # Individual message display
│   │   ├── MessageList.jsx        # Message list container
│   │   ├── MessageReaction.jsx    # Reaction buttons
│   │   └── ReplyList.jsx          # Reply thread display
│   ├── services/
│   │   └── websocket/
│   │       └── wsClient.js        # WebSocket client
│   ├── utils/
│   │   └── api.jsx                # API utilities
│   └── config/
│       └── api.js                 # API configuration
├── hooks/
│   ├── useMessagePolling.js       # Long-polling hook
│   └── useWebSocket.js            # WebSocket hook
└── package.json
```

## Tech Stack

- Frontend: React, Vite, TailwindCSS
- Backend: Python (FastAPI), Repository Pattern, Service Layer
- Communication: REST API + WebSocket (or Long-Polling as fallback)
- Data Storage: In-memory repository (extensible to database)

## Communication Options

### WebSocket (Recommended)
Real-time bidirectional communication with automatic reconnection. Configure via `VITE_USE_WEBSOCKET=true` environment variable.

### Long-Polling
Alternative polling mechanism for environments where WebSocket is not available. Configure via `VITE_USE_WEBSOCKET=false` environment variable.

For detailed WebSocket setup and deployment instructions, see [WEBSOCKET_README.md](WEBSOCKET_README.md).

## Development Notes

- The frontend and backend are separated into their respective folders for clarity.
- Use a virtual environment for backend development to isolate dependencies.
- The project follows a MoSCoW prioritization (MVP -> Stretch -> Optional) for features.
- Choose between WebSocket and Long-Polling based on your deployment environment.

## Contributing

PRs and issues are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT License