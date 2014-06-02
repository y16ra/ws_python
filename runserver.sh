PID=gunicorn.pid

if [ -f $PID ]; then
    kill `cat gunicorn.pid`
fi

gunicorn -c gunicorn.conf.py -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" app:app

