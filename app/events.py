from flask import session
from flask_socketio import emit, join_room, leave_room
from app import app
from app.stockData import StockData
from app.cryptoData import CryptoData
from . import socketio
import random
import string
import time


room_set = {}

@app.celery.task(name='task.message')
def 
s = sched.scheduler(time.time, time.sleep)
def emit_prices(sc): 
    for room in room_set:
        print('yo')
        stockData = StockData(room)
        cryptoData = StockData(room)
        price = stockData.getCurrentPrice()
        if price is None:
            price = cryptoData.getCurrentPrice()
        emit('price',{'price' : price} , room=room)    
    s.enter(2, 1, emit_prices, (sc,))

s.enter(2, 1, emit_prices, (s,))
s.run()

@socketio.on('joined', namespace='/chat')
def joined(data):
    room = data['ticker']
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10))
    join_room(room)
    emit('status', {'msg': name + ' has entered the room.'}, room=room)
    session['name'] = name
    room_set.add(room)

@socketio.on('text', namespace='/chat')
def text(data):
    room = data['ticker']
    name = session.get('name')
    emit('message', {'msg': name + ':' + data['msg']}, room=room)
