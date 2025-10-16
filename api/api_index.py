# api/index.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bot keep-alive endpoint (Vercel)."}), 200