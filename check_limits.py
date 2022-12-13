from check_battery_condition import battery_is_ok
from check_soc import check_soc
from check_temperature import check_temperature
from check_charge_rate import check_charge_rate

if __name__ == '__main__':
  temperature_check = check_temperature(25)
  soc_check = check_soc(70)
  charge_rate_check = check_charge_rate(0.7)
  assert(battery_is_ok(temperature_check, soc_check, charge_rate_check) is True)
  temperature_check = check_temperature(50)
  soc_check = check_soc(85)
  charge_rate_check = check_charge_rate(0)
  assert(battery_is_ok(temperature_check, soc_check, charge_rate_check) is False)
  assert(check_soc(85) is False)
  assert(check_soc(25) is True)
  assert(check_temperature(40) is True)
  assert(check_temperature(50) is False)
  assert(check_charge_rate(0.9) is False)
  assert(check_charge_rate(0.7) is True)
