from flask import session
from flask_socketio import emit, join_room, leave_room
from app import app
from app.stockData import StockData
from app.cryptoData import CryptoData
from . import socketio
import random
import string

@socketio.on('joined', namespace='/chat')
def joined(data):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = data['ticker']
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10))
    join_room(room)
    emit('status', {'msg': name + ' has entered the room.'}, room=room)
    session['name'] = name
@socketio.on('text', namespace='/chat')
def text(data):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = data['ticker']
    name = session.get('name')
    emit('message', {'msg': name + ':' + data['msg']}, room=room)
@socketio.on('price-request', namespace='/chat')
def price_request(data):
    room = data['ticker']
    stockData = StockData(room)
    cryptoData = CryptoData(room)

    price = stockData.getCurrentPrice()
    if price is None:
        price = cryptoData.getCurrentPrice()
    emit('price', {'price': price}, room=room)