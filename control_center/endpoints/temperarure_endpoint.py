import requests

from control_center.constans import TEMP_SENSOR_1_URL


def temp_handler():
    data_temp = None
    try:
        data_temp = requests.get(TEMP_SENSOR_1_URL, verify=False).json()
        print(data_temp)
    except Exception as err:
        print(err)
    time_data = data_temp[0]['date_n_time']
    time_data = time_data[:-10]
    print(time_data)
    data = {'message': str(data_temp[0]['Temperature']) + u'\N{DEGREE SIGN}' + 'C', 'date_and_time': time_data}
    return data