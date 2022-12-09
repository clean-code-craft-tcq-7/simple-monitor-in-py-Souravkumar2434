from check_soc import check_soc
from check_temperature import check_temperature
from check_charge_rate import check_charge_rate
from print_results import print_results

def battery_is_ok(temperature, soc, charge_rate):
  temperature_check = check_temperature(temperature)
  soc_check = check_soc(soc)
  charge_rate_check = check_charge_rate(charge_rate)
  print_results(temperature_check, soc_check, charge_rate_check)
  if(temperature_check and soc_check and charge_rate_check):
    return True
