from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextSendMessage, ImageMessage, ImageSendMessage)
import os
import sys
import json
import urllib.request
import trend as tr
import kokunai as kn
import kokusai as ks
import keizai as ke
import entame as en
import sports as sp
import it
import science as sc
import social as so

app = Flask(__name__)

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    word = event.message.text
    if word == "トレンド":
        trresult = tr.gettrend(word)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=trresult)
        )
    elif word == "国内":
        knresult = kn.getkokunai(word)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=knresult)
        )

    elif word == "国際":
        ksresult = ks.getkokusai(word)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=ksresult)
        )

    elif word == "経済":
        keresult = ke.getkeizai(word)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=keresult)
        )

    elif word == "エンタメ":
        enresult = en.getentame(word)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=enresult)
        )
    
    elif word == "スポーツ":
        spresult = sp.getsports(word)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=spresult)
        )

    elif word == "it":
        itresult = it.getit(word)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=itresult)
        )
    
    elif word == "科学":
        scresult = sc.getscience(word)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=scresult)
        )
    
    elif word == "地域":
        soresult = so.getsocial(word)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=soresult)
        )

    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=word)
        )

if __name__ == "__main__":#正しいファイル拡張子で実行されているか識別
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)