import json
from django.http import HttpResponse, JsonResponse
from thirdparty import juhe

from django.views import View
from utils.response import CommonResponseMixin


class WeatherView(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        data = []
        received_body = request.body.decode('utf-8')
        received_body = json.loads(received_body)
        cities = received_body.get('cities')
        for city in cities:
            result = juhe.weather(city)
            result['city_info'] = city
            data.append(result)
        data = self.wrap_json_response(data=data)
        return JsonResponse(data=data, safe=False, status=200)
