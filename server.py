import falcon
from waitress import serve
from resources import Resource
import webbrowser
import os
import sys
import subprocess

port = 8085
app = falcon.App(cors_enable=True)

# resource will handle all requests to the base URL path
resource = Resource()
app.add_route('/', resource)
# could make it '/resource' for example

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
            
    serve(app, host='0.0.0.0', port=port)
    print('Shutting down')
