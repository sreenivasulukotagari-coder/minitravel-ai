from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/chat")
def chat():
    msg = request.args.get("msg", "").lower()

    if "family" in msg:
        return "Family Trip: Tirupati, Araku, Vizag"
    if "friends" in msg:
        return "Friends Trip: Goa, Manali, Bangalore"
    if "solo" in msg:
        return "Solo Trip: Rishikesh, Ooty, Hampi"

    return "Type: family / friends / solo"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)