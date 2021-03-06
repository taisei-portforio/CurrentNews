from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextSendMessage, TextMessage)
import os # ファイル管理、OS処理を行うモジュール
import sys # システム情報を取得、システムに関する設定を操作が入ってるモジュール
import json
import urllib.request
import trend as tr # 各ファイルから継承
import kokunai as kn
import kokusai as ks
import keizai as ke
import entame as en
import sports as sp
import it
import science as sc
import social as so

app = Flask(__name__) # インスタンス作成

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None) # os.getenvでLineで設定されているアクセストークン、チャネルシークレットを取得
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

if channel_secret is None: # 上記の環境変数が返されなかった場合、エラーを返す。
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST']) # リクエストチェック
def callback():
    signature = request.headers['X-Line-Signature'] # リクエストがLineから送られたのを確認するために、x-line-signatureに含まれている署名を検証。

    # 取得
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 検証。問題なければhandleに定義されている関数を呼び出す
    try:
        events = handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    word = event.message.text
    if word == "トレンド": # 各ファイルから継承。それぞれに対応したトピックを返す。
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

    else: # 上記以外のワードの場合、オウム返しにする。
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=word)
        )

if __name__ == "__main__":#正しいファイル拡張子で実行されているか識別
    port = int(os.getenv("PORT", 5000)) # ポート番号の設定
    app.run(host="0.0.0.0", port=port, debug=True)

    