def print_results(temperature_check, soc_check, charge_rate_check):
  if not (temperature_check):
    print('Temperature is out of range!')
  if not (soc_check):
    print('State of Charge is out of range!')
  if not(charge_rate_check):
    print('Charge rate is out of range!')
