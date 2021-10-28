import src.Utils as Utils

Utils.prepareSsl()

# Gunicorn config
bind = ['192.168.0.50:3000']
cert_reqs = True
certfile = Utils.SSL_CERT_FILE
keyfile = Utils.SSL_KEY_FILE
workers = 1
wsgi_app = 'wsgi:app'
