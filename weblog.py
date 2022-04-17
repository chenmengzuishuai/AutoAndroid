# import socket

import logging
import time

date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())


logging.basicConfig(filename=r"./bin/%slog.txt" % date,format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def send_server():
    # socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket1.connect(('101.34.28.245',8000))
    while True:
        message = yield
        message = str(message)
        logger.info(message)

WebSocket = send_server()
WebSocket.send(None)

