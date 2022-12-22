from Battery_paramteres_threshold import BATTERY_PARAM_THD, MINIMUM_THRESHOLD_FOR_TEMPERATURE, MAXIMUM_THRESHOLD_FOR_TEMPERATURE
from print_messages import print_msg
from warning_in_battery_check import check_temperature_warning


def check_temperature(temperature):
    check_temperature_warning(temperature)
    if temperature < MINIMUM_THRESHOLD_FOR_TEMPERATURE or temperature > MAXIMUM_THRESHOLD_FOR_TEMPERATURE:
        print_msg(False, 'Temperature', 'BREACH')
        return False
    print_msg(True, 'Temperature', 'BREACH')
    return True
