# -*- coding=utf-8 -*-
# author:MC
import time
import os
import uiautomator2 as u2
from tencentAiChat import *
import threading
import queue
import socket



def send_server():
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect(('101.34.28.245',8000))
    while True:
        message = yield
        socket1.send(b'%s' % message)
send = send_server()
send.send(None)



MOMO = "com.immomo.momo"
MoChatActivity = "com.immomo.momo.message.activity.ChatActivity"
MoMainActivity = "com.immomo.momo.maintab.MaintabActivity"


if os.name == 'nt':
    d = u2.connect()
    print(d.info)
else:
    d = u2.connect("0.0.0.0")


d.press("home")

def keep_clean():
    pass




def get_nickname(ui,q):
    text = ui.get_text()
    x,y = ui.center()
    q.put((text,x,y))


def get_center(ui):
    x,y = ui.center()
    return(ui.get_text(),x,y)

def check():
    """
    消费者
    判断生产者传递过来的消息，并且把判断后的值传回给生产者
    :return:
    """
    result = None
    while True:
        message = yield result
        messageList = message.split('-')
        part1 = messageList[0]
        part2 = messageList[1]
        if part1 == "A":  # 检测activity是否存在，回传布尔值
            result = d.wait_activity(part2)

        elif part1 == "T":  # 通过text属性检测目标元素是否存在，回传布尔值
            result = d(text=part2).exists

        elif part1 == "R":  # 通过resourceID检测目标元素是否存在，回传布尔值
            result = d(resourceId=part2).exists

        elif part1 == "RGT":  # 通过resourceID检测目标元素是否存在，如果存在则回传该元素的text属性，如果不存在则回传None

            try:
                result = d(resourceId=part2).get_text()
            except Exception as e:
                print(e)
                result = False

        elif part1 == "TGT":

            try:
                result = d(text=part2).get_text()
            except Exception as e:
                print(e)
                result = False


def reply_chat(n):
    send.send(b'Get into function replpy_chat')
    replyMessage = ""
    t = 1
    newsList = d(resourceId="com.immomo.momo:id/message_layout_rightcontainer")
    if len(newsList) >= n:
        try:
            while t <= n:
                d(resourceId="com.immomo.momo:id/message_layout_rightcontainer")[-t].long_click()
                if d(text="复制文本").exists:
                    d(text="复制文本").click()
                elif d(text="删除消息").exists:
                    d(text="删除消息").click()
                replyMessage = replyMessage + tencentchat(d.clipboard)

                t = t+1
        except Exception as e:
            print(e)
            d(resourceId="com.immomo.momo:id/message_layout_rightcontainer")[-1].long_click()
            if d(text="复制文本").exists:
                d(text="复制文本").click()
            elif d(text="删除消息").exists:
                d(text="删除消息").click()

            replyMessage = replyMessage + tencentchat(d.clipboard)


    else:
        d(resourceId="com.immomo.momo:id/message_layout_rightcontainer")[-1].long_click()
        if d(text="复制文本").exists:
            d(text="复制文本").click()
        elif d(text="删除消息").exists:
            d(text="删除消息").click()
        replyMessage = tencentchat(d.clipboard)

    send.send(b'Get reply message %s from tencentAi' % replyMessage)

    if replyMessage == "":
        d(text="请输入消息...").click_exists()
        d(text="请输入消息...").send_keys("啥")
        d(text="发送").click_exists()
    else:
        d(text="请输入消息...").click_exists()
        send.send(b'Input reply message')
        d(text="请输入消息...").send_keys(replyMessage)
        d(text="发送").click_exists()
    return True

def reply_hello():

    deadline = time.time() + 180
    while time.time() < deadline:
        if d(text="暂无新招呼").exists:
            return


        # while not d(text="回复开始聊天").exists:
        #     if d(text="暂无新招呼").exists:
        #         return
        #
        #     d.swipe(320,703,320,305)

        reciveMessage = ""
        for each in d(resourceId="com.immomo.momo:id/tv_plain_text"):
            reciveMessage = reciveMessage + each.get_text()
        d(resourceId="com.immomo.momo:id/rl_middle").click()
        #d(text="回复开始聊天").click()
        d.send_keys(tencentchat(reciveMessage))
        d(text="发送").click_exists()
    return

def mo_scroll():
    lastName = ""
    while True:
        if d(resourceId="com.immomo.momo:id/chatlist_item_tv_status_new").exists:
            return

        if lastName == d(resourceId="com.immomo.momo:id/chatlist_item_tv_name")[-1].get_text():
            while True:

                if d(text="互动通知").exists:
                    return
                if d(resourceId="com.immomo.momo:id/chatlist_item_tv_status_new").exists:
                    return
                if d(resourceId="com.immomo.momo:id/chatlist_item_tv_name")[-1].get_text() == "收到的招呼":
                    d.long_click(292.5, 1000)
                    d(text="删除对话").click_exists()
                if d(text="新朋友").exists:
                    d.swipe(326.4,326.6,326.6,748.4)
                else:
                    d.long_click(292.5,1445)
                    d(text="删除对话").click_exists()
        else:
            lastName = d(resourceId="com.immomo.momo:id/chatlist_item_tv_name")[-1].get_text()
        d.swipe(326.4,748.4,326.6,326.2)

IgnoreNickName = ['互动通知','动态小助手','订阅内容','MOMO会员中心','MOMO动态小助手']

def select():
    send.send(b'Run into function select')
    c = check()
    c.send(None)
    message = "R-com.immomo.momo:id/chatlist_item_tv_status_new"
    while True:
        result = c.send(message)
        if result:
            send.send(b'Chatlist status new exsit')
            unread = get_center(d(resourceId="com.immomo.momo:id/chatlist_item_tv_status_new")[0])
            # unreadQueue = queue.Queue(1)
            # c = threading.Thread(target=get_center,args=(d(resourceId="com.immomo.momo:id/chatlist_item_tv_status_new")[0],unreadQueue))
            # c.start()
            # c.join()

            d.click(320,unread[-1])
            if d.wait_activity("com.immomo.momo.message.activity.ChatActivity"):
                send.send(b'Get into chat activity')
                reply_chat(int(unread[0]))
                while not d(text="消息").exists:
                    d.press("back")
                    time.sleep(0.5)
            elif d.wait_activity("com.immomo.momo.message.sayhi.activity.HiCardStackActivity"):
                reply_hello()
                while not d(text="消息").exists:
                    d.press("back")
                    time.sleep(0.5)
            elif d(text='与MOMO动态小助手对话').exists:
                while not d(text="消息").exists:
                    d.press("back")
                    time.sleep(0.5)
            elif d(text='新朋友').exists:
                while not d(text="消息").exists:
                    d.press("back")
                    time.sleep(0.5)

            else:
                while not d(text="消息").exists:
                    d.press("back")
                    time.sleep(0.5)

                systemNews = queue.Queue(10)
                for each in d(resourceId="com.immomo.momo:id/chatlist_item_tv_name"):
                    s = threading.Thread(target=get_nickname,args=(each,systemNews))
                    s.start()
                    s.join()
                while True:
                    if systemNews.empty():
                        break
                    else:
                        systemNewsStatus = systemNews.get()
                        if systemNewsStatus[0] in IgnoreNickName:
                            d.long_click(systemNewsStatus[1],systemNewsStatus[2])
                            d(text="删除对话").click_exists()
            return True
        else:
            return False



def action():
    """
    生产者，经过一定的操作后，把需要判断的值传递给消费者，消费者经过判断
    把判断后得到的值传递回来
    :return:
    """
    c = check()
    c.send(None)
    while True:
        d.app_start(MOMO)
        message = "A-%s" % MoMainActivity
        result = c.send(message)
        if result:
            # 进入消息列表
            d(text='消息').click()
            if d(text='消息').count == 2:
                # 循环回复消息
                notice_count = None
                while True:
                    # 通过resourceId检查是否有有效的未读消息存在

                    if d(resourceId="com.immomo.momo:id/notice_iv_unread_count").exists:
                        notice_count = int(d(resourceId="com.immomo.momo:id/notice_iv_unread_count").get_text())

                    if notice_count == int(d(resourceId="com.immomo.momo:id/tab_item_tv_badge").get_text()):
                        return
                    message = 'RGT-com.immomo.momo:id/tab_item_tv_badge'  # 底部消息控件角标红色未读消息控件
                    send.send(b'Unread messages corner mark at buttom exists')
                    result = c.send(message)
                    if not result:
                        return
                    send.send(b'Unread message count:%s' % result)
                    select()
                    mo_scroll()



if __name__ == "__main__":


    while True:

        try:
            d.app_start(MOMO)
            action()

        except Exception as e:

            d.app_stop(MOMO)

            print(e)






