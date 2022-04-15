import requests

from control_center.constans import HEAT_SENSOR_1_URL


def heat_handler():
    data_humidity = None
    try:
        data_humidity = requests.get(HEAT_SENSOR_1_URL, verify=False).json()
    except Exception as err:
        print(err)
    data = [current_data_humidity['Quantity'] for current_data_humidity in data_humidity]
    print(data)
    return data
