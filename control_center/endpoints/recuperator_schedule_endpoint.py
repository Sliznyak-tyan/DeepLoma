import requests

from control_center.constans import RECUPERATOR_GET_SCHEDULE_URL


def recuperator_get_schedule_handler():
    data = None
    try:
        data = requests.get(RECUPERATOR_GET_SCHEDULE_URL, verify=False).json()
    except Exception as err:
        print(err)
    return data
