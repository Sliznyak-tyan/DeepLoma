import json
import requests

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from control_center.endpoints import temp_handler
from control_center.endpoints import humidity_handler
from control_center.endpoints import heat_handler
from control_center.endpoints import recuperator_get_schedule_handler


class IndicatorsView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/system/login/')
        temperature_data = temp_handler()
        humidity_data = humidity_handler()
        data = {'temperature_data': temperature_data, 'humidity_data': humidity_data}
        return render(request, 'html/indicators.html', {'data': data})


class StatisticsView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/system/login/')
        heat_data = heat_handler()
        return render(request, 'html/statistics.html', {'data': heat_data})


def schedule_view(request):
    if not request.user.is_authenticated:
        return redirect('/system/login/')
    if request.method == 'POST':
        if request.POST.get('start_time', None):
            data_to_send = {
                "schedule_status": "add",
                "start_time": request.POST['start_time'],
                "end_time": request.POST['end_time'],
                "temperature": request.POST['temp_value']
            }
            requests.post("http://127.0.0.1:8088/recuperator/change_schedule/", json=data_to_send)
        else:
            requests.post("http://127.0.0.1:8088/recuperator/change_schedule/", request.body)
        schedule = recuperator_get_schedule_handler()
        return redirect('http://127.0.0.1:8000/system/schedule/', {'schedule': schedule})
    else:
        schedule = recuperator_get_schedule_handler()
        if schedule:
            max_id = max([schedule_element['id'] for schedule_element in schedule])
            print(max_id)

    return render(request, 'html/schedule.html', {'schedule': schedule})


def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/system/indicators/')
    else:
        return render(request, 'html/login.html')


def logout_view(request):
    logout(request)
    return redirect('/system/login/')