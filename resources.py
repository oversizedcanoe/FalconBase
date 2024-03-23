import datetime
import traceback
import json
import os
import sys
import falcon

class Resource:
    # / HTTP GET handler
    def on_get(self, req, resp):
        # below not needed, they are defaults. just shown for reference
        #resp.status = falcon.HTTP_200
        #resp.content_type = falcon.MEDIA_JSON

        try:
            print(str(datetime.datetime.now()) + ': Incoming GET request')
            resp.text = "Hello, World!"
            # some_param = req.get_param_as_int('id')
            print(str(datetime.datetime.now()) + ': Sending response')
        except Exception as e:
            print('-----ERROR-----')
            print(traceback.format_exc())
            resp.status = falcon.HTTP_500

    # /resource HTTP POST handler
    def on_post(self, req, resp):
        try:
            print(str(datetime.datetime.now()) + ': Incoming GET request')
            print('Doing some POSTing...')
            #req_body = req.media
            print(str(datetime.datetime.now()) + ': Sending response')
        except Exception as e:
            print('-----ERROR-----')
            print(traceback.format_exc())
            resp.status = falcon.HTTP_500
        pass


