import SslUtils

SslUtils.prepareSsl()

# Gunicorn config
bind = ['0.0.0.0:3000']
cert_reqs = True
certfile = SslUtils.SSL_CERT_FILE
keyfile = SslUtils.SSL_KEY_FILE
threads = 2
timeout = 300
worker_class = 'gevent'
workers = 2
wsgi_app = 'wsgi:app'
