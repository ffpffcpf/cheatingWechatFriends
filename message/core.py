from apscheduler.schedulers.blocking import BlockingScheduler

import random
import itchat
import threading
import time
from itchat.content import *

should_send = False


def start_say_hello():
    send_msg()


def start_scheduler():
    scheduler = BlockingScheduler()

    off_min = random.randint(0, 10)
    off_second = random.randint(-10, 10)
    # scheduler.add_job(util.send_msg_by_user("胡汉三", "早安"), "cron"
    #                   , day_of_week="1-5", hour=9
    #                   , minute=10 + off_min
    #                   , second=30 + off_second)
    scheduler.add_job(start_say_hello, "interval", seconds=15)

    scheduler.start()


_reply = [""]


def search_user_by_name(username):
    try:
        global should_send
        should_send = True
        _username = itchat.search_friends(username)[0].UserName
        print(should_send)
        return _username
    except IndexError as e:
        itchat.log.exception(e)


def send_msg():
    _username = search_user_by_name("胡汉三")
    print("send message to user:" + _username)
    itchat.send_msg(msg="hello", toUserName="filehelper")
    push_reply("有事烧纸")


def send_msg_by_user(msg, username):
    print("send message to user:" + username)
    itchat.send_msg(msg=msg, toUserName=username)
    push_reply("有事烧纸")


def push_reply(msg):
    _reply[0] = msg


def pop_reply():
    _answer = _reply[0]
    _reply[0] = ""
    global should_send
    should_send = False
    return _answer


@itchat.msg_register([TEXT, PICTURE])
def answer_msg(msg):
    print("match user")
    if should_send:
        time.sleep(random.randint(3, 10))
        send_msg_by_user(pop_reply(), msg["ToUserName"])


if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    t = threading.Thread(target=start_scheduler, name="SchedulerThread")
    t.start()
    itchat.start_receiving()
    itchat.run(blockThread=True)
