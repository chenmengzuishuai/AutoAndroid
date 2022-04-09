import socket
import time
import logging


def send_server():
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect(('101.34.28.245',8000))
    while True:
        message = yield
        socket1.send(b'%s' % message)

WebSocket = send_server()
WebSocket.send(None)

