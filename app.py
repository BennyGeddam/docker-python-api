from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"message": "Hello from Benny Agent Docker API"})

@app.get("/health")
def health():
    return jsonify({"status": "healthy"})

@app.get("/info")
def info():
    return jsonify({
        "name": "docker-python-api",
        "version": "1.0",
        "status": "running"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
