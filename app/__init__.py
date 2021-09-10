from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
from app import routes, events

if __name__ == '__main__':
    socketio.run(app,cors_allowed_origins='http://fincha.tv',host='137.184.101.17', port=80)
