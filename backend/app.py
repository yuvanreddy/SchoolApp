from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost/schoolapp')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

@app.route('/')
def home():
    return jsonify({"message": "School App Backend Running"})

@app.route('/dashboard')
def dashboard():
    data = {
        "attendance": "95%",
        "assignments": 5,
        "notifications": Notification.query.count()
    }
    return jsonify(data)

@app.route('/notifications', methods=['POST'])
def create_notification():
    data = request.get_json()
    message = data.get('message')
    if message:
        notification = Notification(message=message)
        db.session.add(notification)
        db.session.commit()
        socketio.emit('new_notification', {'message': message, 'id': notification.id})
        return jsonify({'status': 'success', 'id': notification.id}), 201
    return jsonify({'error': 'Message required'}), 400

@socketio.on('connect')
def handle_connect():
    emit('connected', {'data': 'Connected to real-time updates'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))