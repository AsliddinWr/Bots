from flask import Flask, request
import requests
import os
import json

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "Bot ishlayapti ✅", 200


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        print("RAW UPDATE:", json.dumps(data, indent=2))

        if "message" not in data:
            print("NO MESSAGE")
            return "ok", 200

        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        print("CHAT_ID:", chat_id)
        print("TEXT:", text)

        if text == "/start":
            payload = {
                "chat_id": chat_id,
                "text": "✅ BOT ISHLADI! /start QABUL QILINDI"
            }

            r = requests.post(
                f"{API_URL}/sendMessage",
                json=payload,
                timeout=15
            )

            print("SEND STATUS:", r.status_code)
            print("SEND BODY:", r.text)

        return "ok", 200

    except Exception as e:
        print("ERROR:", str(e))
        return "error", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
