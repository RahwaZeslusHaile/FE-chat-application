import time
import requests
import threading
from datetime import datetime

BASE_URL = "https://backendrahwachatapp.hosting.codeyourfuture.io"

def poll_messages(start_time_iso):
    """Continuously long-poll the backend for new messages"""
    last_time = start_time_iso

    while True:
        print(f"[{datetime.utcnow().isoformat()}] Long polling from {last_time} ...")
        try:
            resp = requests.get(f"{BASE_URL}/messages/longpoll?after={last_time}", timeout=30)
            if resp.status_code == 200:
                new_msgs = resp.json()
                if new_msgs:
                    for msg in new_msgs:
                        print(f"[{msg['timestamp_iso']}] {msg['username']}: {msg['content']}")
                    last_time = new_msgs[-1]['timestamp_iso']
            else:
                print(f"[{datetime.now()}] Poll returned {resp.status_code}: {resp.text}")

        except Exception as e:
            print(f"[{datetime.now()}] Poll failed: {e}")
            time.sleep(2) 

        time.sleep(0.1)  

def post_message():
    """Post a test message after a short delay"""
    time.sleep(5)  
    print(f"[{datetime.now()}] Posting new message...")
    try:
        resp = requests.post(
            f"{BASE_URL}/messages",
            json={"username": "test_user", "content": "Hello from long polling test!"}
        )
        print(f"[{datetime.now()}] Post returned: {resp.status_code}")
    except Exception as e:
        print(f"[{datetime.now()}] Post failed: {e}")

if __name__ == "__main__":
    start_iso = datetime.now().isoformat()

    poll_thread = threading.Thread(target=poll_messages, args=(start_iso,), daemon=True)
    poll_thread.start()

    post_message()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting long-polling test.")
