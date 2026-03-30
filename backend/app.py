from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "School App Backend Running"})

@app.route('/dashboard')
def dashboard():
    data = {
        "attendance": "95%",
        "assignments": 5,
        "notifications": 3
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)