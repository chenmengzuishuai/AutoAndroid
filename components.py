# -*- coding:utf-8 -*-

class Component(object):
    def __init__(self, id, index=0):
        self.id = id
        self.index = index
        self.childid = ''

    def setchild(self, childid):
        self.childid = childid


noteId = "com.immomo.momo:id/fl_session_note_container"  # 纸条
comment = "com.immomo.momo:id/notice_layout_content_root"  # 互动通知
chatItem = "com.immomo.momo:id/item_layout"  # 聊天列表元素
chatItemName = "com.immomo.momo:id/chatlist_item_tv_name"  # 聊天列表元素名称
chatItemNew = "com.immomo.momo:id/chatlist_item_tv_status_new"  # 聊天列表元素消息状态
buttomItem = "com.immomo.momo:id/maintab_layout_chat"  # 主页底部元素
globalNew = "com.immomo.momo:id/tab_item_tv_badge"  # 全局未读消息状态



