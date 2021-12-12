from App import app

import SslUtils

if __name__ == '__main__':
    # Extract SSL key/cert from .p12 file.
    SslUtils.prepareSsl()

    # Set up SSL context and run app.
    sslContext = (SslUtils.SSL_CERT_FILE, SslUtils.SSL_KEY_FILE)
    app.run(host='0.0.0.0', port=3000, debug=False, ssl_context=sslContext)
