from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "YOUR_BOT_TOKEN"
URL = f"https://api.telegram.org/bot8414715928:AAE2TC18IKUpoyMkx3UasiHa4dwayyVLnpY/sendMessage"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        reply = f"شما فرستادید: {text}"
        requests.post(URL, json={"chat_id": chat_id, "text": reply})
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return "Bot is running ✅"

if __name__ == "__main__":
    app.run()
