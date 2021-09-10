from flask import session
from flask_socketio import emit, join_room, leave_room
from app import app
from . import socketio
import random
import string
import time

@socketio.on('joined', namespace='/chat')
def joined(data):
    room = data['ticker']
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10))
    join_room(room)
    emit('status', {'msg': name + ' has entered the room.'}, room=room)
    session['name'] = name
    app.rooms.add(room)

@socketio.on('text', namespace='/chat')
def text(data):
    room = data['ticker']
    name = session.get('name')
    emit('message', {'msg': name + ':' + data['msg']}, room=room)
