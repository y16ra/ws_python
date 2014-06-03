ws_python
=========
implements chat using websocket server

# 概要
pythonでチャットサーバの実装をしました。
Websocketを使っています。
よくあるサンプルは、自分が送信したメッセージをエコーバックするだけのものが多かったのでもう少し実装を追加しました。

# 機能
* port 8090で起動します
* ユーザ名としてIPを使ってますが変更予定
* ルームは１つだけ(接続した人は全て同じ部屋で会話することになります)
* 接続しているユーザ全員にメッセージが届きます。
* チャットができる簡易なHTML画面を実装しました。

# Python version
Python 2.7.6 で開発しています。

# 動作環境
動作確認済みの環境は以下の通りです。
Linux (CentOS6.5)
Mac OSX(10.9.3)

# 利用モジュール
* flask
* gevent-websocket
* Flask-uWSGI-WebSocket

# Install
```
git clone https://github.com/y16ra/ws_python.git
pip install -r requirements.txt
```
# WebSocket serverの起動
```
sh runserver.sh
```
gunicornで起動するスクリプトを入れています。
gunicornでワーカー増やすとそれぞれ別ルームになってしまいます。
```python app.py ```
とかでも起動します。

# 今後修正&追加実装したいこと
* ルームがひとつだけしかない事
* 履歴が残らず後から入った人が過去ログを見られない事
