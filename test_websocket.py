#!/usr/bin/env python3

import asyncio
import websockets
import json
import requests
from datetime import datetime

WS_URL = "wss://backendwschat.hosting.codeyourfuture.io/ws"
REST_URL = "https://backendwschat.hosting.codeyourfuture.io"

async def test_websocket():
    print(f"[{datetime.now()}] Connecting to WebSocket: {WS_URL}")
    
    try:
        async with websockets.connect(WS_URL) as websocket:
            print(f"[{datetime.now()}] ✅ WebSocket connected!")
            
            print(f"[{datetime.now()}] Sending get_messages action...")
            await websocket.send(json.dumps({"action": "get_messages"}))
            
            print(f"[{datetime.now()}] Waiting for initial messages...")
            initial_msg = await asyncio.wait_for(websocket.recv(), timeout=5)
            data = json.loads(initial_msg)
            print(f"[{datetime.now()}] Received: {data['type']}")
            if data['type'] == 'messages_list':
                print(f"[{datetime.now()}] Initial messages count: {len(data['data'])}")
            
            print(f"\n[{datetime.now()}] Posting new message via REST API...")
            response = requests.post(
                f"{REST_URL}/messages",
                json={
                    "username": "WebSocket_Test",
                    "content": f"Test message at {datetime.now().strftime('%H:%M:%S')}"
                }
            )
            print(f"[{datetime.now()}] POST response: {response.status_code}")
            
            print(f"[{datetime.now()}] Waiting for WebSocket broadcast...")
            broadcast_msg = await asyncio.wait_for(websocket.recv(), timeout=10)
            broadcast_data = json.loads(broadcast_msg)
            print(f"[{datetime.now()}] ✅ Received broadcast: {broadcast_data['type']}")
            
            if broadcast_data['type'] == 'new_message':
                msg = broadcast_data['data']
                print(f"[{datetime.now()}] Message: [{msg['username']}] {msg['content']}")
                print(f"\n✅ WebSocket test PASSED! Real-time broadcasting works!")
            else:
                print(f"\n⚠️  Unexpected message type: {broadcast_data['type']}")
            
    except asyncio.TimeoutError:
        print(f"\n❌ Timeout waiting for WebSocket message")
    except websockets.exceptions.WebSocketException as e:
        print(f"\n❌ WebSocket error: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("WebSocket Deployment Test")
    print("=" * 60)
    asyncio.run(test_websocket())
