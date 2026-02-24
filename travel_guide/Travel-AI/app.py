from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

DATA = {
    "andhra pradesh": {
        "low": ["Tirupati", "Srisailam", "Lepakshi", "Ahobilam", "Horsley Hills"],
        "medium": ["Vizag", "Araku", "Vijayawada", "Rajahmundry", "Amaravati"],
        "high": ["Papikondalu", "Lambasingi", "Borra Caves", "Kailasagiri"]
    },
    "telangana": {
        "low": ["Basar", "Yadadri", "Medak", "Bhongir"],
        "medium": ["Hyderabad", "Warangal", "Ananthagiri Hills"],
        "high": ["Golconda", "Charminar", "Ramoji Film City"]
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    step = data.get("step")
    text = data.get("text").lower().strip()
    state = data.get("state")
    budget = data.get("budget")

    if step == 0:
        if text in ["hi", "hello", "hey"]:
            return jsonify(reply="Hi 👋 Who are you traveling with? (family / friends / solo / old age)", step=1)
        return jsonify(reply="Please type hi to start 😊", step=0)

    if step == 1:
        if text in ["family", "friends", "solo", "old age", "oldage"]:
            return jsonify(reply="Which state do you want to visit?", step=2)
        return jsonify(reply="Type: family / friends / solo / old age", step=1)

    if step == 2:
        return jsonify(reply="Select budget: low / medium / high", step=3, state=text)

    if step == 3:
        if text in ["low", "medium", "high"]:
            places = DATA.get(state, {}).get(text, ["No data available"])
            reply = f"✨ Places in {state.upper()} ({text} budget):\n\n"
            reply += "\n".join([f"{i+1}. {p}" for i, p in enumerate(places)])
            reply += "\n\nType: change budget / change user"
            return jsonify(reply=reply, step=4, budget=text)
        return jsonify(reply="Type: low / medium / high", step=3)

    if step == 4:
        if "change budget" in text:
            return jsonify(reply="Select budget again: low / medium / high", step=3)
        if "change user" in text:
            return jsonify(reply="Who are you traveling with? (family / friends / solo / old age)", step=1)
        return jsonify(reply="Type: change budget / change user", step=4)

    return jsonify(reply="Something went wrong", step=0)

if __name__ == "__main__":
    app.run()