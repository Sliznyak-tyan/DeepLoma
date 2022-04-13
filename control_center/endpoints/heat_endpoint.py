import requests

from control_center.constans import HEAT_SENSOR_1_URL


def heat_handler():
    data_humidity = None
    try:
        data_humidity = requests.get(HEAT_SENSOR_1_URL, verify=False).json()
    except Exception as err:
        print(err)
    print(data_humidity)
    time_data = data_humidity['date_n_time']
    time_data = time_data[:-10]
    data = {'quantity': data_humidity['Quantity']*0.01, 'date_and_time': time_data}
    print(data['quantity'])
    return data
