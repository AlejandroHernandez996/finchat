from flask import session
from flask_socketio import emit, join_room, leave_room
from app import app
from app.stockData import StockData
from app.cryptoData import CryptoData
from . import socketio
import random
import string
import time

priceCache = {}
roomCount = {}
@socketio.on('joined', namespace='/chat')
def joined(data):
    room = data['ticker']
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10))
    session['name'] = name
    join_room(room)
    join_room(name)
    if room in roomCount:
        roomCount[room] += 1
    else:
        roomCount[room] = 1
    emit('status', {'msg': name + ' has entered the room.'}, room=room)

@socketio.on('left', namespace='/chat')
def left(data):
    leave_room(data['ticker'])
    leave_room(session['name'])
    roomCount[data['ticker']] -= 1
    emit('status', {'msg': name + ' has left the room.'}, room=data['ticker'])
    
@socketio.on('text', namespace='/chat')
def text(data):
    room = data['ticker']
    name = session.get('name')
    emit('message', {'msg': name + ':' + data['msg']}, room=room)

@socketio.on('price-request', namespace='/chat')
def price_request(data):

    price = 0
    if data['ticker'] in priceCache and int(time.time()*1000) - priceCache[data['ticker']]['time'] > 1000:
        price = priceCache[data['ticker']]['price']
    else:
        stockData = StockData(data['ticker'])
        cryptoData = CryptoData(data['ticker'])
        price = stockData.getCurrentPrice()
        if price is None:
            price = cryptoData.getCurrentPrice()
        priceCache[data['ticker']] = {'price': price, 'time': int(time.time()*1000)}
    emit('price',{'price' : price,'count' : roomCount[data['ticker']]},room=session['name'])
