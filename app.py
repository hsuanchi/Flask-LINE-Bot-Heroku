import os
from datetime import datetime
from typing import Text
import psycopg2
from flask import Flask, abort, request

#連接資料庫
#conn = psycopg2.connect(database = 'postgres',host = 'localhost',port = '5432',user = 'Tim',password = 'Tim910111')
#print('Connectecd')
#cursor = conn.cursor()

#連linebot
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


def text_reply(content, event):
    reply = TextSendMessage(text=content)
    line_bot_api.reply_message(event.reply_token, reply)

#資料庫函數
#def writeInfo():
    #cursor.execute('CREATE TABLE inventory(id serial PRIMARY KEY,name VARCHAR(50),quantity INTEGER);')


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text
    if get_message == "壞貓貓":
        badcat = "你才壞貓貓"
        text_reply(badcat,event)
    else:
        confuse = "我聽不懂你在說什麼"
        text_reply(confuse,event)
        


#環境變數DJANGO_SETTINGS_MODULE
