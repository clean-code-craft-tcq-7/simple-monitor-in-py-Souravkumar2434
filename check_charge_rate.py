from Battery_paramteres_threshold import BATTERY_PARAM_THD, MAXIMUM_THRESHOLD_FOR_CR
from print_messages import print_msg
from warning_in_battery_check import check_charge_rate_warning

def check_charge_rate(charge_rate):
    check_charge_rate_warning(charge_rate)
    if charge_rate > MAXIMUM_THRESHOLD_FOR_CR:
        print_msg(False, 'CHARGE_RATE', 'BREACH')
        return False
    print_msg(True, 'CHARGE_RATE', 'BREACH')
    return True
    
