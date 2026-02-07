#!/usr/bin/env python3
import time
import requests
import threading
from datetime import datetime

BASE_URL = "https://backendrahwachatapp.hosting.codeyourfuture.io"

def poll_messages(start_time_iso, stop_event):
    last_time = start_time_iso
    
    print(f"[{datetime.now()}] Starting long polling from {last_time}")
    
    while not stop_event.is_set():
        try:
            resp = requests.get(
                f"{BASE_URL}/messages/longpoll?after={last_time}", 
                timeout=25
            )
            
            if resp.status_code == 200:
                new_msgs = resp.json()
                if new_msgs:
                    print(f"\n[{datetime.now()}] ✅ Received {len(new_msgs)} new message(s):")
                    for msg in new_msgs:
                        print(f"  [{msg['timestamp_iso']}] {msg['username']}: {msg['content']}")
                    last_time = new_msgs[-1]['timestamp_iso']
                    print(f"\n✅ Long polling test PASSED! Real-time updates work!")
                    stop_event.set()
                else:
                    print(f"[{datetime.now()}] Long poll returned empty (timeout)")
            else:
                print(f"[{datetime.now()}] ❌ Poll returned {resp.status_code}: {resp.text}")
                
        except requests.exceptions.Timeout:
            print(f"[{datetime.now()}] Long poll timeout (no new messages)")
        except Exception as e:
            print(f"[{datetime.now()}] ❌ Poll failed: {e}")
            time.sleep(2)

def post_message(delay=3):
    time.sleep(delay)
    print(f"\n[{datetime.now()}] Posting new message via REST API...")
    try:
        resp = requests.post(
            f"{BASE_URL}/messages",
            json={
                "username": "LongPoll_Test",
                "content": f"Test message at {datetime.now().strftime('%H:%M:%S')}"
            }
        )
        print(f"[{datetime.now()}] POST response: {resp.status_code}")
        if resp.status_code == 200:
            print(f"[{datetime.now()}] Message posted successfully!")
    except Exception as e:
        print(f"[{datetime.now()}] ❌ Post failed: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("Long Polling Deployment Test")
    print("=" * 60)
    
    start_iso = datetime.now().isoformat()
    stop_event = threading.Event()
    
    poll_thread = threading.Thread(
        target=poll_messages, 
        args=(start_iso, stop_event), 
        daemon=True
    )
    poll_thread.start()
    
    post_message(delay=3)
    
    try:
        poll_thread.join(timeout=30)
        if poll_thread.is_alive():
            print(f"\n⚠️  Test timed out after 30 seconds")
            stop_event.set()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        stop_event.set()
