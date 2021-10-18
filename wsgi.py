from app import app

# Server config.
if __name__ == '__main__':
    sslContext = ('certs/index.crt', 'certs/index.key')
    app.run(host='0.0.0.0', port=5000, debug=False, ssl_context=sslContext)
