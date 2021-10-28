from app import app

import src.Utils as Utils

if __name__ == '__main__':
    # Extract SSL key/cert from .p12 file.
    Utils.prepareSsl()

    # Set up SSL context and run app.
    sslContext = (Utils.SSL_CERT_FILE, Utils.SSL_KEY_FILE)
    app.run(host='0.0.0.0', port=3000, debug=False, ssl_context=sslContext)
