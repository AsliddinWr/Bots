from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("8448435876:AAHDZ-4eNdvHLanYStLe_q_-hli8W3vU8_g")
API_URL = f"https://api.telegram.org/bot{TOKEN}/"

def send_message(chat_id, text):
    requests.post(API_URL + "sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })

@app.route("/", methods=["GET"])
def home():
    return "Bot ishlayapti ✅", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json(force=True)

    if update is None:
        return "no data", 200

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "👋 Salom! Bot nihoyat ishlayapti 🎉")

    return "ok", 200   # 🔴 MUHIM

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
