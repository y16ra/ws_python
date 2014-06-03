bind = '127.0.0.1:8090'
workers = 1
backlog = 2048
worker_class = 'gevent'
debug = True
daemon = True
pidfile = '/tmp/gunicorn.pid'

logger_class = 'gunicorn.glogging.Logger'
logfile = '/tmp/gunicorn.log'
loglevel = 'debug'
logconfig = None
accesslog = 'gunicorn_access.log'
errorlog = 'gunicorn_error.log'
