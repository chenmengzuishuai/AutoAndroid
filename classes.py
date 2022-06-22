# -*- coding: utf-8 -*-






MOMO = "com.immomo.momo"  # 包名
MoChatActivity = "com.immomo.momo.message.activity.ChatActivity"  # 聊天详情页
MoMainActivity = "com.immomo.momo.maintab.MaintabActivity"  # 首页



class Message(object):
    def __init__(self, id, message):
        self.id = id
        self.message = message


class Couple(object):

    def __init__(self, cp0, cp1):
        self.cp0 = cp0
        self.cp1 = cp1
        self.commucation = []
        self.cpName = "%s&%s" % (cp0,cp1)

    def get_cp(self, name):
        if name == self.cp1:
            return self.cp0
        else:
            return self.cp1

    def add_chat(self, message):
        self.commucation.append({message.id: message.message})


class Judger(object):
    def __init__(self, device):
        self.device = device
        return

    def currentApp(self):
        return self.device.app_current()['package']

    def currentActivity(self):
        return self.device.app_current()['activity']

    def currentCustom(self):
        if self.device(text="消息").count == 2:
            return 1   # 如果文本“消息”的控件数量为2，返回int 1 ，代表聊天列表界面
        else:
            return self.currentActivity()



