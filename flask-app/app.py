# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS
# import requests

# app = Flask(__name__)
# CORS(app)

# # RASA_URL = "http://rasa:5005/webhooks/rest/webhook"  # RasaコンテナへのURL
# RASA_URL = "https://RASA_rasaandflask.onrender.com/webhooks/rest/webhook"  # RasaコンテナへのURL

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     user_message = request.json.get('message')
#     if not user_message:
#         return jsonify({"error": "No message provided"}), 400
    
#     payload = {
#         "sender": "user",
#         "message": user_message
#     }

#     try:
#         response = requests.post(RASA_URL, json=payload)
#         response.raise_for_status()
#         return jsonify(response.json())
#     except requests.exceptions.RequestException as e:
#         return jsonify({"error": str(e)}), 500

# # if __name__ == '__main__':
# #     app.run(host='0.0.0.0', port=5000)
#---------------------------------------------------------------
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    rasa_response = requests.post(
        "https://RASA_rasaandflask.onrender.com/webhooks/rest/webhook",
        json={"sender": "user", "message": user_message}
    )
    bot_response = rasa_response.json()

    if bot_response:
        reply = bot_response[0].get("text", "すみません、理解できませんでした。")
    else:
        reply = "すみません、応答がありませんでした。"

    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

