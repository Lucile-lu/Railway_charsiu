from flask import Flask, request

app = Flask(app.py_)

@app.route('/', methods=['GET'])
def home():
    return "✅ Bot keep-alive is running!", 200

@app.errorhandler(401)
def unauthorized(e):
    return "Unauthorized access disabled.", 200

# Vercel 用的 handler（一定要有）
def handler(request, response):
    response.text = "✅ Bot keep-alive is running via Vercel!"
    return response
