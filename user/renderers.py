import json

from rest_framework.renderers import JSONRenderer
from collections import OrderedDict
from rest_framework import status


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        
        token = data.get('token', None)
        email = data.get('email', None)
        # password = data.get('password', None)
        name = data.get('name', None)


        if token is not None and isinstance(token, bytes) :
            
            data['token'] = token.decode('utf-8')
        
        temp=data.copy()
        finaldata = OrderedDict(sorted(temp.items()))

        if email is not None and name is not None:
            finaldata.pop('email')
            finaldata.pop('name')
            return json.dumps(finaldata)

        temp2={}
        return json.dumps(temp2)

