import eventlet
eventlet.monkey_patch()

from flask import Flask
from flask_socketio import SocketIO
from stockData import StockData
from cryptoData import CryptoData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)
rooms = {}
def bg_emit():
    for room in rooms:
        stockData = StockData(room)
        cryptoData = StockData(room)
        price = stockData.getCurrentPrice()
        if price is None:
            price = cryptoData.getCurrentPrice()
        socket.io.emit('price',{'price' : price} , room=room)    
def listen():
    while True:
        bg_emit()
        eventlet.sleep(2)

eventlet.spawn(listen)

from app import routes, events

if __name__ == '__main__':
    socketio.run(app,cors_allowed_origins='http://fincha.tv',host='137.184.101.17', port=80)
