#!/usr/bin/env python3
"""
AI Morning Briefing script.
Run by the scheduled remote agent daily at 10am BST.
Researches AI/agentic trends and sends a briefing to Telegram.
"""
import json
import urllib.request
import urllib.error
import sys
from datetime import datetime

BOT_TOKEN = "8780009263:AAFajxMZr-7w1S-0jdP_mjTGASUVZb4OZH0"
CHAT_ID = 1741415406
BRIEFING_PATH = "/tmp/ai-briefing.txt"


def send_telegram(text: str) -> None:
    """Send plain-text message to Telegram, splitting at 4000 chars."""
    chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
    for i, chunk in enumerate(chunks):
        payload = json.dumps({
            "chat_id": CHAT_ID,
            "text": chunk,
            "disable_web_page_preview": True,
        }).encode()
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        try:
            resp = urllib.request.urlopen(req)
            result = json.loads(resp.read().decode())
            msg_id = result.get("result", {}).get("message_id")
            print(f"Chunk {i+1}/{len(chunks)} sent OK (message_id={msg_id})")
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            print(f"HTTP {e.code} on chunk {i+1}: {body}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    with open(BRIEFING_PATH) as f:
        briefing = f.read()
    print(f"Sending briefing ({len(briefing)} chars) in {(len(briefing)//4000)+1} chunk(s)...")
    send_telegram(briefing)
    print("Done.")
