import json
import requests

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from control_center.endpoints import temp_handler
from control_center.endpoints import humidity_handler
from control_center.endpoints import heat_handler
from control_center.endpoints import recuperator_get_schedule_handler

class IndicatorsView(APIView):
    def get(self, request):
        temperature_data = temp_handler()
        humidity_data = humidity_handler()
        data = {'temperature_data': temperature_data, 'humidity_data': humidity_data}
        return render(request, 'html/indicators.html', {'data': data})


class StatisticsView(APIView):
    def get(self, request):
        heat_data = heat_handler()
        return render(request, 'html/statistics.html', {'data': heat_data})


def schedule_view(request):
    schedule = None
    if request.method == 'POST':
        requests.post("http://127.0.0.1:8088/recuperator/change_schedule/", request.body)
    else:
        schedule = recuperator_get_schedule_handler()

    return render(request, 'html/schedule.html', {'schedule': schedule})
