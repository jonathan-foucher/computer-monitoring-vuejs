import socketio
import eventlet

sio = socketio.Server(cors_allowed_origins='*')

app = socketio.WSGIApp(sio)

def listen():
    while True:
        sio.emit('test', 'mydataTest')
        eventlet.sleep(1)

eventlet.spawn(listen)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 80)), app)