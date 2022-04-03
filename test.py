# -*- coding:utf-8 -*-
import uiautomator2 as u2
import re
import time
MOMO = "com.immomo.momo"

d = u2.connect()
d.app_start(MOMO)
print("互动通知角标数量》》》",d(resourceId="com.immomo.momo:id/notice_iv_unread_count").count)
print("收到的消息角标数量》》》",d(resourceId="com.immomo.momo:id/chatlist_item_tv_status_new").count)
print("用户名称数量》》》",d(resourceId="com.immomo.momo:id/chatlist_item_tv_name").count)

print("收到的消息文本数量》》》",d(resourceId="com.immomo.momo:id/message_layout_rightcontainer").count)

print(d(text="暂无新招呼").exists)
# for each in d(resourceId="com.immomo.momo:id/chatlist_item_tv_name"):
#     print(each.get_text())
#
# for each in d(resourceId="com.immomo.momo:id/chatlist_item_tv_status_new"):
#     print(each.get_text())
#
#
#
# def reply_chat(n):
#     replyMessage = ""
#     t = 1
#     while t <= n:
#         d(resourceId="com.immomo.momo:id/message_layout_rightcontainer")[-t].long_click()
#         d(text="复制文本").click_exists()
#         replyMessage = tencentchat(d.clipboard)
#         # d(text="请输入消息...").click_exists()
#         d(text="请输入消息...").set_text(replyMessage)
#         d(text="发送").click_exists()
#         t = t+1
#     return True
#


# for each in d(resourceId="com.immomo.momo:id/item_layout"):
#     print(each.child(resourceId="com.immomo.momo:id/chatlist_item_tv_name").get_text())

#
#
# timeStart = time.time()
#
# deadlineTime = timeStart + 20
#
# while time.time() < deadlineTime:
#     print(d.app_info(MOMO))
#     time.sleep(0.1)
