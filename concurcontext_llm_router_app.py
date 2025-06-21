
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "ConcurContext API is live!"})

@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok", "message": "Ping received!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
