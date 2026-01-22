from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "Bot ishlayapti ✅", 200


@app.route("/webhook", methods=["POST"])
def webhook():
    # JSON ni majburan o‘qiymiz
    data = request.get_json(force=True)

    # Render loglari uchun
    print("UPDATE RECEIVED")

    if "message" not in data:
        print("NO MESSAGE IN UPDATE")
        return "ok", 200

    message = data["message"]
    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    print("TEXT:", text)

    if text == "/start":
        resp = requests.post(
            f"{API_URL}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": "🔥 TABRIKLAYMAN! BOT ISHLADI 🎉"
            },
            timeout=15
        )

        print("SEND STATUS:", resp.status_code)
        print("SEND RESPONSE:", resp.text)

    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
