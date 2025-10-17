# keep_alive.py
import os

# -----------------------------
# 這段只在本地或 Replit 用 Flask
if os.environ.get("VERCEL") is None:
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
# 這段會被 Vercel 自動呼叫
def handler(request, response):
    return "Bot keep-alive running!"
