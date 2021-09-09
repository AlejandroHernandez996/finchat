from flask import session
from flask_socketio import emit, join_room, leave_room
from app import app
from app.stockData import StockData
from app.cryptoData import CryptoData
from . import socketio

@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    name = session.get('name')
    join_room(room)
    emit('status', {'msg': name + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    name = session.get('name')
    emit('message', {'msg': name + ':' + message['msg']}, room=room)
@socketio.on('price-request', namespace='/chat')
def price_request(data):
    room = session.get('room')

    stockData = StockData(room)
    cryptoData = CryptoData(room)

    price = stockData.getCurrentPrice()
    if price is None:
        price = cryptoData.getCurrentPrice()
    emit('price', {'price': price}, room=room)