import falcon
from resources import Resource
import webbrowser
import os
import ssl
import sys
import subprocess

port = 8085
app = falcon.App(cors_enable=True)

# resource will handle all requests to the base URL path
resource = Resource()
app.add_route('/', resource)
# could make it '/resource' for example

# optional, provide paths to certificate/key file from letsencrypt
CERT_FILE = ''
KEY_FILE = ''

# to serve some photos at the /images directory
#app.add_static_route('/images', os.getcwd() + '/images', True)

if __name__ == '__main__':
    print(f'Serving on port {port}...')
    if len( sys.argv ) > 1:
        arg1 = sys.argv[1]
        if arg1 == '-o' or arg1 == '-open':
            if sys.platform=='win32':
                webbrowser.open(f'http://localhost:{port}/')
            else:
                subprocess.Popen(['xdg-open', f'http://localhost:{port}/'])

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

    httpd = simple_server.make_server('0.0.0.0', 8080, app)

    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print('Serving on port 8080...')
    
    httpd.serve_forever()
    
    print('Shutting down')
