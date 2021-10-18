import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


import json

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    badCat = TextSendMessage(text="你才壞貓貓")

    line_bot_api.reply_message(event.reply_token, reply)
    if get_message == "壞貓貓":
        line_bot_api.reply_message(event.reply_token, badCat)
    elif get_message == "上架":
        updateCommodity()

def updateCommodity():
    update = {}
    reply01 = TextSendMessage(text="請輸入商品名稱")
    line_bot_api.reply_message(event.reply_token, reply01)
    




#環境變數DJANGO_SETTINGS_MODULE
