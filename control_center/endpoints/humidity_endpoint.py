import requests

from control_center.constans import HUMIDITY_SENSOR_1_URL


def humidity_handler():
    data_humidity = None
    try:
        data_humidity = requests.get(HUMIDITY_SENSOR_1_URL, verify=False).json()
    except Exception as err:
        print(err)
    time_data = data_humidity[0]['date_n_time']
    time_data = time_data[:-10]
    print(time_data)
    data = {'message': str(data_humidity[0]['Quantity']) + '%', 'date_and_time': time_data}
    return data
