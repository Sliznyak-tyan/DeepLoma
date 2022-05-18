TEMP_SENSOR_1_URL = 'http://127.0.0.1:8088/sensors/temperature?sensor_id=1'
HUMIDITY_SENSOR_1_URL = 'http://127.0.0.1:8088/sensors/humidity?sensor_id=1'
HEAT_SENSOR_1_URL = 'http://127.0.0.1:8088/sensors/heat?sensor_id=1'
RECUPERATOR_GET_SCHEDULE_URL = 'http://127.0.0.1:8088/recuperator/get_schedule/'
LOGIN_REDIRECTION_URL = '/system/login/'
INDICATORS_REDIRECTION_URL = '/system/indicators/'
CHANGE_SCHEDULE_URL = 'http://127.0.0.1:8088/recuperator/change_schedule/'
SCHEDULE_URL = 'http://127.0.0.1:8000/system/schedule/'

# HTML paths
INDICATORS_HTML_PATH = 'html/indicators.html'
LOGIN_HTML_PATH = 'html/login.html'
SCHEDULE_HTML_PATH = 'html/schedule.html'
STATISTICS_HTML_PATH = 'html/statistics.html'

# Analytics params
S_T = 40.0
Z_OT_PER = 240
COEF_RECALCULATE = 1163000
AMBIENT_TEMPERATURE = 8
CONSUMPTIONS = [
    {"specific_annual_consumption": 28.0, "consumption_reduction_potential": 0.0, "target_savings": 0.0},
    {"specific_annual_consumption": 29.5, "consumption_reduction_potential": 3.8, "target_savings": 0.0},
    {"specific_annual_consumption": 30.8, "consumption_reduction_potential": 7.8, "target_savings": 0.0},
    {"specific_annual_consumption": 32.0, "consumption_reduction_potential": 11.3, "target_savings": 1.1},
    {"specific_annual_consumption": 33.0, "consumption_reduction_potential": 14.0, "target_savings": 1.4},
    {"specific_annual_consumption": 33.8, "consumption_reduction_potential": 16.0, "target_savings": 1.6},
    {"specific_annual_consumption": 34.7, "consumption_reduction_potential": 18.2, "target_savings": 1.8},
    {"specific_annual_consumption": 35.6, "consumption_reduction_potential": 20.2, "target_savings": 2.0},
    {"specific_annual_consumption": 36.5, "consumption_reduction_potential": 22.2, "target_savings": 2.2},
    {"specific_annual_consumption": 37.3, "consumption_reduction_potential": 23.9, "target_savings": 2.4},
    {"specific_annual_consumption": 38.1, "consumption_reduction_potential": 25.5, "target_savings": 2.5},
    {"specific_annual_consumption": 38.8, "consumption_reduction_potential": 26.8, "target_savings": 2.7},
    {"specific_annual_consumption": 39.7, "consumption_reduction_potential": 28.5, "target_savings": 2.8},
    {"specific_annual_consumption": 40.6, "consumption_reduction_potential": 30.1, "target_savings": 3.0},
    {"specific_annual_consumption": 41.3, "consumption_reduction_potential": 31.3, "target_savings": 3.1},
    {"specific_annual_consumption": 42.1, "consumption_reduction_potential": 32.6, "target_savings": 3.3},
    {"specific_annual_consumption": 42.8, "consumption_reduction_potential": 33.7, "target_savings": 3.4},
    {"specific_annual_consumption": 43.6, "consumption_reduction_potential": 34.9, "target_savings": 3.5},
    {"specific_annual_consumption": 44.3, "consumption_reduction_potential": 35.9, "target_savings": 3.6},
    {"specific_annual_consumption": 45.2, "consumption_reduction_potential": 37.2, "target_savings": 3.7},
    {"specific_annual_consumption": 46.0, "consumption_reduction_potential": 38.3, "target_savings": 3.8},
    {"specific_annual_consumption": 46.9, "consumption_reduction_potential": 39.5, "target_savings": 3.9},
    {"specific_annual_consumption": 47.7, "consumption_reduction_potential": 40.5, "target_savings": 4.3},
    {"specific_annual_consumption": 48.6, "consumption_reduction_potential": 41.6, "target_savings": 4.9},
    {"specific_annual_consumption": 49.5, "consumption_reduction_potential": 42.6, "target_savings": 5.6},
    {"specific_annual_consumption": 50.4, "consumption_reduction_potential": 43.7, "target_savings": 6.2},
    {"specific_annual_consumption": 51.2, "consumption_reduction_potential": 44.5, "target_savings": 6.7},
    {"specific_annual_consumption": 52.2, "consumption_reduction_potential": 45.6, "target_savings": 7.4},
    {"specific_annual_consumption": 53.1, "consumption_reduction_potential": 46.5, "target_savings": 7.9},
    {"specific_annual_consumption": 54.1, "consumption_reduction_potential": 47.5, "target_savings": 8.5},
    {"specific_annual_consumption": 55.0, "consumption_reduction_potential": 48.4, "target_savings": 9.0},
    {"specific_annual_consumption": 56.0, "consumption_reduction_potential": 49.3, "target_savings": 9.6},
    {"specific_annual_consumption": 57.0, "consumption_reduction_potential": 50.2, "target_savings": 10.1},
    {"specific_annual_consumption": 58.1, "consumption_reduction_potential": 51.1, "target_savings": 10.7},
    {"specific_annual_consumption": 59.3, "consumption_reduction_potential": 52.1, "target_savings": 11.3},
    {"specific_annual_consumption": 60.7, "consumption_reduction_potential": 53.2, "target_savings": 11.9},
    {"specific_annual_consumption": 62.1, "consumption_reduction_potential": 54.3, "target_savings": 12.6},
    {"specific_annual_consumption": 63.6, "consumption_reduction_potential": 55.4, "target_savings": 13.2},
    {"specific_annual_consumption": 65.3, "consumption_reduction_potential": 56.5, "target_savings": 13.9},
    {"specific_annual_consumption": 67.2, "consumption_reduction_potential": 57.7, "target_savings": 14.6},
    {"specific_annual_consumption": 69.2, "consumption_reduction_potential": 59.0, "target_savings": 15.4},
    {"specific_annual_consumption": 71.2, "consumption_reduction_potential": 60.1, "target_savings": 16.1},
    {"specific_annual_consumption": 73.1, "consumption_reduction_potential": 61.2, "target_savings": 16.7},
    {"specific_annual_consumption": 75.4, "consumption_reduction_potential": 62.3, "target_savings": 17.4},
    {"specific_annual_consumption": 78.1, "consumption_reduction_potential": 63.6, "target_savings": 18.2},
    {"specific_annual_consumption": 81.4, "consumption_reduction_potential": 65.1, "target_savings": 19.1},
]
CLASSES_OF_BUILDINGS = [
    {'class': "A++", "value": -60, "color": "#009020"},
    {'class': "A+", "value": -50, "color": "#009020"},
    {'class': "A", "value": -40, "color": "#009020"},
    {'class': "B+", "value": -30, "color": "#7eb200"},
    {'class': "B", "value": -15, "color": "#7eb200"},
    {'class': "C+", "value": -5, "color": "#c7ce00"},
    {'class': "C", "value": 5, "color": "#c7ce00"},
    {'class': "C-", "value": 15, "color": "#c7ce00"},
    {'class': "D", "value": 50, "color": "#e7de00"},
    {'class': "E", "value": 51, "color": "#f6c400"}
]
