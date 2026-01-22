from flask import Flask, request
import requests
import os
import json

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "Bot ishlayapti ✅"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True, silent=True)

    print("RAW DATA:", data)

    if not data:
        return "no data", 200

    message = data.get("message")
    if not message:
        return "no message", 200

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    if text == "/start":
        requests.post(f"{API_URL}/sendMessage", json={
            "chat_id": chat_id,
            "text": "🔥 ISHLADI! Bot javob beryapti."
        })

    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
