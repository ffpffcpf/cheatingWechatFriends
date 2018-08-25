from apscheduler.schedulers.blocking import BlockingScheduler

import random
import message.util as util
import itchat
import threading
from itchat.content import *

should_send = True


def start_say_hello():
    util.send_msg()


def start_scheduler():
    scheduler = BlockingScheduler()

    off_min = random.randint(0, 10)
    off_second = random.randint(-10, 10)
    scheduler.add_job(util.send_msg_by_user("楠彬", "早安"), "cron"
                      , day_of_week="1-5", hour=9
                      , minute=10 + off_min
                      , second=30 + off_second)
    # scheduler.add_job(start_say_hello, "interval", seconds=10)

    scheduler.start()


@itchat.msg_register([TEXT, PICTURE])
def answer_msg(msg):
    print("match user")
    if should_send:
        util.send_msg_by_user(util.pop_reply(), msg["ToUserName"])


if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    t = threading.Thread(target=start_scheduler, name="SchedulerThread")
    t.start()
    itchat.start_receiving()
    itchat.run(blockThread=True)
