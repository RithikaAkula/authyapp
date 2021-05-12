import json
from rest_framework.renderers import JSONRenderer


class BookingJSONRenderer(JSONRenderer):

    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        
        response_dict = {
                    'user_bookings': data,
                }
        data = response_dict

        return json.dumps(response_dict)

