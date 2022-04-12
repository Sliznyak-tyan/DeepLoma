from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from control_center.endpoints import temp_handler
from control_center.endpoints import humidity_handler


class IndicatorsView(APIView):
    def get(self, request):
        temperature_data = temp_handler()
        humidity_data = humidity_handler()
        data = {'temperature_data': temperature_data, 'humidity_data': humidity_data}
        return render(request, 'html/indicators.html', {'data': data})


class StatisticsView(APIView):
    def get(self, request):
        return render(request, 'html/statistics.html')
