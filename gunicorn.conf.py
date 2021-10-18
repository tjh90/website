# Gunicorn config

bind = ['192.168.0.50:3000']
cert_reqs = True
certfile = './certs/index.crt'
keyfile = './certs/index.key'
workers = 1
wsgi_app = 'wsgi:app'
