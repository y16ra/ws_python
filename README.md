ws_python
=========

implements chat using websocket server

pythonでチャットサーバの実装をしました。
Websocketを使っています。
よくあるサンプルは、自分が送信したメッセージをエコーバックするだけのものが多かったのでもう少し実装を追加しました。

# 利用モジュール
* flask
* gevent-websocket

# Install
```
git clone https://github.com/y16ra/ws_python.git
pip install -r requirements.txt
```
# WebSocket serverの起動
```
sh runserver.sh
```
# 機能
* port 8090で起動します
* ユーザ名としてIPを使ってますが変更予定
* ルームは１つだけ(接続した人は全て同じ部屋で会話することになります)
* 接続しているユーザ全員にメッセージが届きます。

# 今後修正&追加実装したいこと
* ルームがひとつだけしかない事
* 履歴が残らず後から入った人が過去ログを見られない事
