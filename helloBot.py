#!/usr/local/pyenv/shims/python
# coding:utf-8

import time
import re
from slackclient import SlackClient
import AppConf
import Constant

class SlackBotMain:
    sc = SlackClient(AppConf.token)

    def __init__(self):
        if SlackBotMain.sc.rtm_connect():
            print(SlackBotMain.sc.user)
            # print(SlackBotMain.sc.server.login_data['self']['id'])
            while True:
                data = SlackBotMain.sc.rtm_read()

                if len(data) > 0:
                    print(data)
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
        
        if re.search(u"(.*もどります.*|.*戻ります.*|.*帰社.*)", data["text"]) is not None:
            return "<@" + data["user"] + ">" + u"ご連絡ありがとうございます。気をつけて戻ってください。:wink:"
        
        if re.search(u".*おはよう.*", data["text"]) is not None:
            return "<@" + data["user"] + ">" + u"おはようございます。今日も一日頑張ってください。:wink:"
        
        if re.search(u".*dbmain.*", data["text"], re.IGNORECASE) is not None:
            return "<@" + data["user"] + ">main系DBですね。:wink:" + "\n" + "```" + Constant.dbMainStr + "```\n\n"\
                    + "こちらで、よろしいですか。:relieved:"

        if re.search(u".*dbres.*", data["text"], re.IGNORECASE) is not None:
            return "<@" + data["user"] + ">res系DBですね。:wink:" + "\n" + "```" + Constant.dbResStr + "```\n\n"\
                    + "こちらで、よろしいですか。:relieved:"

        if re.search(u".*dbmroo.*", data["text"], re.IGNORECASE) is not None:
            return "<@" + data["user"] + ">search系DBですね。:wink:" + "\n" + "```" + Constant.dbMroongaStr + "```\n\n"\
                    + "こちらで、よろしいですか。:relieved:"
        
        if re.search(u".*dbcass.*", data["text"], re.IGNORECASE) is not None:
            return "<@" + data["user"] + ">NoSqlのcassandraですね。:wink:" + "\n" + "```" + Constant.dbCassandraStr + "```\n\n"\
                    + "こちらで、よろしいですか。:relieved:"

        if re.search(u".*dbmem.*", data["text"], re.IGNORECASE) is not None:
            return "<@" + data["user"] + ">NoSqlのmemcacheですね。:wink:" + "\n" + "```" + Constant.dbMemcacheStr + "```\n\n"\
                    + "こちらで、よろしいですか。:relieved:"

        if re.search(u".*vmaddress.*", data["text"], re.IGNORECASE) is not None:
            return "<@" + data["user"] + ">皆さんご使用のVMのアドレスですね。:wink:" + "\n" + "```" + Constant.vmAddressStr + "```\n\n"\
                    + "こちらで、よろしいですか。:relieved:"

sbm = SlackBotMain()
            