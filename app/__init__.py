from flask import Flask
from flask_socketio import SocketIO
from flask_celery import make_celery

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

app.config.update(
    CELERY_BROKER_URL = 'amqp://localhost//',
    CELERY_RESULT_BACKEND='rpc://'
)

celery = make_celery(app)
socketio = SocketIO(app)

from app import routes, events

if __name__ == '__main__':
    socketio.run(app,message_queue='amqp://',cors_allowed_origins='http://fincha.tv',host='137.184.101.17', port=80)
