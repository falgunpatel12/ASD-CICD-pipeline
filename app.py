
from flask import Flask, request, jsonify

app = Flask(__name__)


def add(a, b):
    return a + b


def greet(name):
    return f"Hello, {name}! Welcome to the DevOps pipeline."


def login(email, password):
    return bool(email) and len(password) >= 6


@app.route("/")
def home():
    return jsonify({
        "message": greet("Student"),
        "available_routes": ["/add?a=5&b=3", "/greet?name=Student"]
    })


@app.route("/add")
def add_route():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        return jsonify({"result": add(a, b)})
    except ValueError:
        return jsonify({"error": "Please provide valid numbers"}), 400


@app.route("/greet")
def greet_route():
    name = request.args.get("name", "Student")
    return jsonify({"message": greet(name)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
