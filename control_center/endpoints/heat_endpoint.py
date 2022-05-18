import requests

from control_center.constans import HEAT_SENSOR_1_URL
from control_center.constans import TEMP_SENSOR_1_URL
from control_center.constans import S_T
from control_center.constans import Z_OT_PER
from control_center.constans import COEF_RECALCULATE
from control_center.constans import CONSUMPTIONS
from control_center.constans import AMBIENT_TEMPERATURE
from control_center.constans import CLASSES_OF_BUILDINGS

def heat_handler():
    data_heat = None
    try:
        data_heat = requests.get(HEAT_SENSOR_1_URL, verify=False).json()
        print(data_heat)
    except Exception as err:
        print(err)
    data = [current_data_heat['Quantity'] for current_data_heat in data_heat]

    print(data)
    return data


def urtoiv_computing():
    tetoiv = sum(heat_handler())
    urtoiv = tetoiv / S_T
    return urtoiv


def gsop_computing():
    ttv = requests.get(TEMP_SENSOR_1_URL, verify=False).json()
    ttv = ttv[0]['Temperature']
    ttot = AMBIENT_TEMPERATURE
    gsop = (ttv - ttot) * Z_OT_PER
    return gsop


def urtgsopoiv_computing():
    urtoiv = urtoiv_computing()
    gsopt = gsop_computing()
    urtgsopoiv = (urtoiv / gsopt) * COEF_RECALCULATE
    return urtgsopoiv


def computing_of_heat():
    consumption_reduction_potential = -1.0
    target_savings = -1.0
    urtgsopoiv_consumption = urtgsopoiv_computing()
    print(urtgsopoiv_consumption)
    for consumption in CONSUMPTIONS:
        if urtgsopoiv_consumption < consumption['specific_annual_consumption']:
            consumption_reduction_potential = consumption['consumption_reduction_potential']
            target_savings = consumption['target_savings']
            break

    if consumption_reduction_potential == -1.0:
        consumption_reduction_potential = CONSUMPTIONS[-1]['consumption_reduction_potential']
        target_savings = CONSUMPTIONS[-1]['target_savings']

    rate = ((urtgsopoiv_consumption * 100) / 47.32) - 100
    class_of_efficiency = "-"
    color = '-'

    for class_of_building in CLASSES_OF_BUILDINGS:
        if rate < class_of_building['value']:
            class_of_efficiency = class_of_building['class']
            color = class_of_building['color']
            break

    return {'specific_annual_consumption': "{:.2f}".format(urtgsopoiv_consumption),
            'consumption_reduction_potential': consumption_reduction_potential,
            'target_savings': target_savings,
            'class_of_efficiency': class_of_efficiency, 'color': color}
