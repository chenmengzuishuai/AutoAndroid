# -*- coding: utf-8 -*-

class Message(object):
    def __init__(self, id, message):
        self.id = id
        self.message = message


class Couple(object):

    def __init__(self, cp0, cp1):
        self.cp0 = cp0
        self.cp1 = cp1
        self.commucation = []


    def get_cp(self, name):
        if name == self.cp1:
            return self.cp0
        else:
            return self.cp1


    def add_chat(self, message):
        self.commucation.append({message.id: message.message})


