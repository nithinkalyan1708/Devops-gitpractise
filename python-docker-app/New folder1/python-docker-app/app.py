from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>🚀 Python Flask App running in Docker</h1>"

@app.route('/about')
def about():
    return "<h2>Name: Nithin | Role: DevOps Learner</h2>"

@app.route('/api')
def api():
    return jsonify({
        "message": "Hello from Python API",
        "status": "success"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "UP"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
