from flask import Flask, request
import requests, os

app = Flask(__name__)

TOKEN = os.environ.get("8448435876:AAHDZ-4eNdvHLanYStLe_q_-hli8W3vU8_g")
print("TOKEN =", TOKEN)  # 👈 MUHIM

API = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json(force=True)
    print("UPDATE =", update)

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")
        print("TEXT =", text)

        r = requests.post(f"{API}/sendMessage", json={
            "chat_id": chat_id,
            "text": "TEST OK"
        })
        print("TG RESPONSE =", r.text)

    return "ok", 200

@app.route("/")
def home():
    return "Bot ishlayapti", 200
