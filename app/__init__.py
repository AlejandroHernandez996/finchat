from flask import Flask
from flask_socketio import SocketIO
from engineio.payload import Payload

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

socketio = SocketIO(app)
from app import routes, events

if __name__ == '__main__':
    Payload.max_decode_packets = 5000
    socketio.run(app,cors_allowed_origins='http://fincha.tv',host='http://fincha.tv', port=80)
