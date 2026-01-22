from flask import Flask, request
import requests, os

TOKEN = os.environ.get("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/"

app = Flask(__name__)

def bot(method, data):
    requests.post(URL + method, data=data)

@app.route("/", methods=["GET"])
def home():
    return "Bot ishlayapti ✅"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()
    if "message" in update:
        cid = update["message"]["chat"]["id"]
        text = update["message"].get("text")
        if text == "/start":
            bot("sendMessage", {
                "chat_id": cid,
                "text": "👋 Salom! Render webhook ishlayapti ✅"
            })
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
