# keep_alive.py（本地或 Replit 用）
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# -----------------------------
# Vercel 版本的 handler
def handler(request, response):
    return "Bot keep-alive running!"
