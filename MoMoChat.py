from connect import d
from weblog import WebSocket
from tencentAiChat import *
import time
import threading
import queue
from classes import *
import uiautomator2 as u2
from components import *
from mylog import *


# 包名
MOMO = "com.immomo.momo"
d.press("home")
d = u2.connect()

def startmomo(device):
    d.app_stop(MOMO)
    d.app_start(MOMO)
    result = d(resourceId=buttomItem).exists(timeout=5)
    if not result:
        logger.error("拉起应用失败")
    return result


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
    WebSocket.send(b'Get into function replpy_chat')
    replyMessage = ""
    d(text="请输入消息...").click_exists()
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
                replyMessage = tencentchat(d.clipboard)
                if replyMessage == "":
                    d(text="请输入消息...").click_exists()
                    d(text="请输入消息...").set_text("啥")
                    d(text="发送").click_exists(timeout=3)

                else:
                    d(text="请输入消息...").click_exists()
                    WebSocket.send(b'Input reply message')
                    d(text="请输入消息...").set_text(replyMessage)
                    d(text="发送").click_exists(timeout=3)


                t = t+1


        except Exception as e:
            print(e)
            d(resourceId="com.immomo.momo:id/message_layout_rightcontainer")[-1].long_click()
            if d(text="复制文本").exists:
                d(text="复制文本").click()
            elif d(text="删除消息").exists:
                d(text="删除消息").click()

            replyMessage = tencentchat(d.clipboard)
            if replyMessage == "":
                d(text="请输入消息...").click_exists()
                d(text="请输入消息...").set_text("啥")
                d(text="发送").click_exists(timeout=3)

            else:
                d(text="请输入消息...").click_exists()
                WebSocket.send(b'Input reply message')
                d(text="请输入消息...").set_text(replyMessage)
                d(text="发送").click_exists(timeout=3)



    else:
        d(resourceId="com.immomo.momo:id/message_layout_rightcontainer")[-1].long_click()
        if d(text="复制文本").exists:
            d(text="复制文本").click()
        elif d(text="删除消息").exists:
            d(text="删除消息").click()
        replyMessage = tencentchat(d.clipboard)
        if replyMessage == "":
            d(text="请输入消息...").click_exists()
            d(text="请输入消息...").set_text("啥")
            d(text="发送").click_exists(timeout=3)

        else:
            d(text="请输入消息...").click_exists()
            WebSocket.send(b'Input reply message')
            d(text="请输入消息...").set_text(replyMessage)
            d(text="发送").click_exists(timeout=3)

    WebSocket.send(b'Get reply message %b from tencentAi' % bytes(replyMessage,'utf-8'))

    return True


def reply_hello():

    deadline = time.time() + 180
    while time.time() < deadline:
        time.sleep(1)
        if d(text="暂无新招呼").exists:
            return

        reciveMessage = ""
        for each in d(resourceId="com.immomo.momo:id/tv_plain_text"):
            reciveMessage = reciveMessage + each.get_text()
        d(resourceId="com.immomo.momo:id/rl_middle").click()
        d(text="回复即可开始聊天").click_exists(timeout=3)
        d(text="回复即可开始聊天").set_text(tencentchat(reciveMessage))
        d(text="发送").click_exists(timeout=3)
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
                    while not d(text="消息").exists:
                        d.press("back")
                        time.sleep(0.5)
                if d(text="新朋友").exists:
                    d.swipe(326.4,326.6,326.6,748.4)
                else:
                    d.long_click(292.5,1445)
                    d(text="删除对话").click_exists()
                    if d(text="新朋友").exists:
                        while not d(text="消息").exists:
                            d.press("back")
                            time.sleep(0.5)
        else:
            lastName = d(resourceId="com.immomo.momo:id/chatlist_item_tv_name")[-1].get_text()
        d.swipe(326.4,748.4,326.6,326.2)


IgnoreNickName = ['互动通知','动态小助手','订阅内容','MOMO会员中心','MOMO动态小助手']


def select():
    WebSocket.send(b'Run into function select')
    c = check()
    c.send(None)
    message = "R-com.immomo.momo:id/chatlist_item_tv_status_new"
    while True:
        result = c.send(message)
        if result:
            WebSocket.send(b'Chatlist status new exsit')
            unread = get_center(d(resourceId="com.immomo.momo:id/chatlist_item_tv_status_new")[0])
            d.click(320,unread[-1])


            if d.wait_activity("com.immomo.momo.message.activity.ChatActivity"):
                WebSocket.send(b'Get into chat activity')
                if d(text="请输入消息...").exists:
                    reply_chat(int(unread[0]))
                while not d(text="消息").exists:
                    d.press("back")
                    time.sleep(0.5)
            elif d.wait_activity("com.immomo.momo.message.sayhi.activity.HiCardStackActivity"):
                reply_hello()
                while not d(text="消息").exists:
                    d.press("back")


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
                    WebSocket.send(b'Unread messages corner mark at buttom exists')
                    result = c.send(message)
                    if not result:
                        return
                    else:

                        WebSocket.send(b'Unread message count:%b' % bytes(result,'utf-8'))
                    select()
                    mo_scroll()
