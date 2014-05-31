#!/usr/bin/env python
# -*- coding: utf-8 -*-

from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request
from werkzeug.exceptions import abort

chat_clients = set()

app = Flask(__name__)

@app.route('/')
def echo():
    # environ['wsgi.websocket'] から WebSocket オブジェクトが得られる
    ws = request.environ['wsgi.websocket']

    if ws is None:
        print "ws is none"
        abort(400)

    chat_clients.add(ws)

    print 'enter:', len(chat_clients), request.environ['REMOTE_ADDR'], request.environ['REMOTE_PORT']
    user_name = request.environ['REMOTE_ADDR'] + ":" + request.environ['REMOTE_PORT']

    try:
        while True:
            # receive message
            message = ws.receive()
            print user_name, message
            if message is None:
                break;
            # broadcast message
            err_clients = set()
            for client in chat_clients:
                try:
                    client.send(user_name + "/" + message)
                except Exception:
                    err_clients.add(client)

                for ec in err_clients:
                    chat_clients.remove(ec)

    except geventwebsocket.WebSocketError, ex:
        print "{0}: {1}".format(ex.__class__.__name__, ex)    

    finally:
        # 退室処理
        chat_clients.remove(ws)
        print "bye!", user_name

if __name__ == '__main__':
    # WebSocketHandler が environ['wsgi.websocket'] をセットする
    http_server = WSGIServer(('', 8080), app, handler_class=WebSocketHandler)
    http_server.serve_forever()

