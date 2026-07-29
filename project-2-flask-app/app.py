from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    name = os.environ.get("APP_NAME", "World")
    return f"<h1>Hello, {name}! This is running inside Docker 🐳 Hello, {name}! Live reload works! 🔥</h1>"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)