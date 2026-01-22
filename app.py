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
    data = request.get_json(force=True, silent=True)
    print("UPDATE:", data)

    if not data or "message" not in data:
        print("NO MESSAGE")
        return "ok", 200

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    print("TEXT:", text)
    print("CHAT_ID:", chat_id)
    print("BOT_TOKEN:", BOT_TOKEN)

    if text == "/start":
        r = requests.post(
            f"{API_URL}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": "✅ BOT ISHLADI! Bu DEBUG javobi"
            },
            timeout=10
        )

        print("SEND MESSAGE STATUS:", r.status_code)
        print("SEND MESSAGE RESPONSE:", r.text)

    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
