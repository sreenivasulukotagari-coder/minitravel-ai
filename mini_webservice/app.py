from flask import Flask, send_file
import os

app = Flask(__name__)   # 🔴 MUST be named app

@app.route("/")
def home():
    return "Mini Travel AI is running ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
