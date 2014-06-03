#!/usr/bin/env python
# -*- coding: utf-8 -*-

from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.websocket import WebSocketError
from gevent.pywsgi import WSGIServer
from werkzeug.exceptions import abort
from flask import Flask, request, render_template
import logging

chat_clients = set()

app = Flask(__name__)
app.config['DEBUG'] = True
app.logger.setLevel(logging.INFO)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    # environ['wsgi.websocket'] から WebSocket オブジェクトが得られる
    ws = request.environ['wsgi.websocket']

    if ws is None:
        app.logger.info("ws is none")
        abort(400)

    chat_clients.add(ws)

    app.logger.info('enter:' + str(len(chat_clients)) + '/' + request.environ['REMOTE_ADDR'] + '/' + str(request.environ['REMOTE_PORT']));
    #print 'enter:', len(chat_clients), request.environ['REMOTE_ADDR'], request.environ['REMOTE_PORT']
    user_name = request.environ['REMOTE_ADDR'] + ":" + request.environ['REMOTE_PORT']

    try:
        while True:
            # receive message
            message = ws.receive()
            if message is None:
                break;
            # broadcast message
            app.logger.info(message)
            err_clients = set()
            for client in chat_clients:
                try:
                    client.send(message)
                except Exception:
                    err_clients.add(client)

                for ec in err_clients:
                    chat_clients.remove(ec)

    #except WebSocketError, ex:
    except Exception:
        app.logger.error('exception')

    finally:
        # 退室処理
        chat_clients.remove(ws)
        app.logger.info("bye!")

if __name__ == '__main__':
    # WebSocketHandler が environ['wsgi.websocket'] をセットする
    http_server = WSGIServer(('', 8080), app, handler_class=WebSocketHandler)
    http_server.serve_forever()

