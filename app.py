from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "Bot ishlayapti ✅"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    print("UPDATE:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            requests.post(f"{API_URL}/sendMessage", json={
                "chat_id": chat_id,
                "text": "Salom 👋 Bot ishlayapti!"
            })

    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
