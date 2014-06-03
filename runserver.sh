PID=/tmp/gunicorn.pid

if [ -f $PID ]; then
    kill `cat /tmp/gunicorn.pid`
fi

gunicorn -c gunicorn.conf.py -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" app:app

