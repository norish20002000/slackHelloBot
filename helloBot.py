#!/usr/local/pyenv/shims/python
# coding:utf-8

import time
import re
from slackclient import SlackClient
import AppConf

class SlackBotMain:
    sc = SlackClient(AppConf.token)

    def __init__(self):
        if SlackBotMain.sc.rtm_connect():
            while True:
                data = SlackBotMain.sc.rtm_read()

                if len(data) > 0:
                    for item in data:
                        if "type" in item.keys():
                            if item["type"] == "message":
                                SlackBotMain.sc.rtm_send_message(item["channel"], self.create_message(item))

                time.sleep(1)
        else:
            print("Connection Failed, invalid token?")

    def create_message(self, data):
        if re.search(u"(.*帰ります.*|.*帰宅.*)", data["text"]) is not None:
            return "<@" + data["user"] + ">" + u"お疲れ様。気をつけて帰ってください。:wink:"

sbm = SlackBotMain()
            