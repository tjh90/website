import SslUtils

SslUtils.prepareSsl()

# Gunicorn config
bind = ['0.0.0.0:3000']
cert_reqs = True
certfile = SslUtils.SSL_CERT_FILE
keyfile = SslUtils.SSL_KEY_FILE
workers = 1
wsgi_app = 'wsgi:app'
