from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from CI/CD Pipeline!",
        "status": "running",
        "version": "1.0.1"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"result": a + b})

@app.route("/subtract/<int:a>/<int:b>")
def subtract(a, b):
    return jsonify({"result": a - b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)