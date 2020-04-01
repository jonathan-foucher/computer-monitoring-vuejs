import socketio
import eventlet
from data_format import DataToSend

# contains the data to send (temperatures, load...)
myData = DataToSend()

# create the socket
sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

# update and send the data every second
def listen():
    while True:
        myData.update()
        sio.emit('data', myData.toJSON())
        eventlet.sleep(1)

eventlet.spawn(listen)

# listen on localhost => port 80
if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 80)), app)