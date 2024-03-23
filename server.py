import falcon
from waitress import serve
from resources import Resource
import webbrowser
import os

app = falcon.App(cors_enable=True)

# resource will handle all requests to the '/resource' URL path
resource = Resource()
app.add_route('/resource', resource)

# to serve some photos at the /images directory
#app.add_static_route('/images', os.getcwd() + '/images', True)

if __name__ == '__main__':
    print('Serving on port 8080...')
    #webbrowser.open('http://localhost:8080/resource')
    serve(app, host='0.0.0.0', port=8080)
    print('Shutting down')
