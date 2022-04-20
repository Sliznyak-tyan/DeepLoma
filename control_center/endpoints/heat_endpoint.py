import requests

from control_center.constans import HEAT_SENSOR_1_URL


def heat_handler():
    data_heat = None
    try:
        data_heat = requests.get(HEAT_SENSOR_1_URL, verify=False).json()
    except Exception as err:
        print(err)
    data = [current_data_heat['Quantity'] for current_data_heat in data_heat]
    print(data)
    return data
