import requests

from django.shortcuts import redirect

from control_center.constans import RECUPERATOR_GET_SCHEDULE_URL
from control_center.constans import CHANGE_SCHEDULE_URL
from control_center.constans import SCHEDULE_URL


def recuperator_get_schedule_handler():
    data = None
    try:
        data = requests.get(RECUPERATOR_GET_SCHEDULE_URL, verify=False).json()
    except Exception as err:
        print(err)
    return data


def prepare_data_to_send(request_post):
    return {'schedule_status': 'add', 'start_time': request_post['start_time'], 'end_time': request_post['end_time'],
            'temperature': request_post['temp_value']}


def schedule_handler(request):
    if request.POST.get('start_time', None):
        data_to_send = prepare_data_to_send(request.POST)
        requests.post(CHANGE_SCHEDULE_URL, json=data_to_send)
    else:
        requests.post(CHANGE_SCHEDULE_URL, request.body)
    schedule = recuperator_get_schedule_handler()
    return redirect(SCHEDULE_URL, {'schedule': schedule})
