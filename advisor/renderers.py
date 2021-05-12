import json
from rest_framework.renderers import JSONRenderer


class AdvisorJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        
        response_dict = {
                    'advisors': data,
                }
        data = response_dict
        return json.dumps(data)

