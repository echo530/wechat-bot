from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OPENAI_API_KEY = "你的API_KEY"

def ask_ai(msg):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": msg}]
    }
    res = requests.post(url, headers=headers, json=data)
    return res.json()['choices'][0]['message']['content']

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.json.get("msg")
    reply = ask_ai(msg)
    return jsonify({"reply": reply})

app.run(port=5000)