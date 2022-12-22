from Battery_paramteres_threshold import BATTERY_PARAM_THD, MINIMUM_THRESHOLD_FOR_SOC, MAXIMUM_THRESHOLD_FOR_SOC
from print_messages import print_msg
from warning_in_battery_check import check_soc_warning


def check_soc(soc):
    check_soc_warning(soc)
    if soc < MINIMUM_THRESHOLD_FOR_SOC or soc > MAXIMUM_THRESHOLD_FOR_SOC:
        print_msg(False, 'SOC', 'BREACH')
        return False
    print_msg(True, 'SOC', 'BREACH')
    return True
