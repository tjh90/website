import atexit
import logging
import os
from cryptography.hazmat.primitives.serialization import pkcs12, Encoding, NoEncryption, PrivateFormat, PublicFormat

# Key/cert files.
SSL_KEY_FILE = './certs/index.key'
SSL_CERT_FILE = './certs/index.crt'
SSL_P12_FILE = './certs/index.p12'

# Set up logging.
def __setupLog():
    '''
    Set up logger

    @returns the logger to use for custom logs.
    '''
    log = logging.getLogger('log')
    log.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)5s %(message)s', datefmt='%Y-%m-%dT%H:%M:%S')
    handler.setFormatter(formatter)

    log.addHandler(handler)

    return log

LOG = __setupLog()

def __cleanUp():
    ''' Run cleanup after the app is shutdown.'''

    LOG.info('Cleaning up SSL key/cert files')
    try:
        os.remove(SSL_KEY_FILE)
        os.remove(SSL_CERT_FILE)
    except:
        LOG.warning('Failed to delete SSL certificate and/or key during cleanup')

def prepareSsl():
    ''' Extract SSL key and certificate from encrypted file. '''

    LOG.info('Extracting SSL key/cert files')

    sslPasswd = os.getenv('WEBSITE_SSL_PASSWD').encode()
    if not sslPasswd:
        raise RuntimeError('Could not extract SSL certificates - environment variable: WEBSITE_SSL_PASSWD was not defined')

    with open(SSL_P12_FILE, 'rb') as file:
        content = file.read()

    (key, cert, _) = pkcs12.load_key_and_certificates(content, sslPasswd)

    with open(SSL_KEY_FILE, 'wb') as file:
        file.write(key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()))

    with open(SSL_CERT_FILE, 'wb') as file:
        file.write(cert.public_bytes(Encoding.PEM))

    # Register shutdown hook.
    atexit.register(__cleanUp)

def isMobile(request):
    '''
    Determine if the request was sent by a mobile agent.

    @param request the request.

    @returns True iff the user agent appears to be from a mobile device.
    '''

    agent = request.user_agent.string.lower()
    for keyword in ['android', 'iphone', 'mobile']:
        if keyword in agent:
            return True

    return False
