import itchat
import logging as log
from message.core import should_send

_reply = [""]


def search_user_by_name(username):
    try:
        should_send = True
        _username = itchat.search_friends(username)[0].UserName
        return _username
    except IndexError as e:
        log.exception(e)


def send_msg():
    _username = search_user_by_name("胡汉三")
    print("send message to user:" + _username)
    send_msg_by_user("hello", username="filehelper")
    push_reply("有事烧纸")


def send_msg_by_user(msg, username):
    itchat.send_msg(msg=msg, toUserName=username)


def push_reply(msg):
    _reply[0] = msg


def pop_reply():
    _answer = _reply[0]
    _reply[0] = ""
    should_send = False
    return _answer
