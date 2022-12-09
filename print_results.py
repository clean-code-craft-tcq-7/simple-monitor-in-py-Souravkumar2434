def print_results(Temperature_check, soc_check, charge_rate_check):
  if not (Temperature_check):
    print('Temperature is out of range!')
  if not (soc_check):
    print('State of Charge is out of range!')
  if not(charge_rate_check):
    print('Charge rate is out of range!')
