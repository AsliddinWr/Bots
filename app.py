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
    data = request.get_json(force=True)
    print("UPDATE:", json.dumps(data, indent=2))

    try:
        message = data.get("message")
        if not message:
            print("NO MESSAGE OBJECT")
            return "ok", 200

        chat_id = message["chat"]["id"]

        text = message.get("text")
        print("TEXT:", text)

        payload = {
            "chat_id": chat_id,
            "text": "✅ BOT ISHLAYAPTI!\nSizdan xabar keldi."
        }

        r = requests.post(
            f"{API_URL}/sendMessage",
            json=payload,
            timeout=15
        )

        print("SEND STATUS:", r.status_code)
        print("SEND BODY:", r.text)

    except Exception as e:
        print("ERROR:", e)

    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
