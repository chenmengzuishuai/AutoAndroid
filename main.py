# -*- coding=utf-8 -*-
# author:MC
from MoMoChat import *

d.set_fastinput_ime(True)

if __name__ == "__main__":


    while True:

        try:
            d.app_start(MOMO)
            action()

        except Exception as e:

            d.app_stop(MOMO)
            WebSocket.send(e)








