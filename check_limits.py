from check_battery_condition import battery_is_ok
from check_soc import check_soc
from check_temperature import check_temperature
from check_charge_rate import check_charge_rate

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  #assert(battery_is_ok(50, 85, 0) is False)
  assert(check_soc(85) is False)
  assert(check_soc(25) is True)
  assert(check_temperature(40) is False)
  assert(check_temperature(50) is True)
  assert(check_charge_rate(0.9) is False)
  assert(check_charge_rate(0.7) is True)
