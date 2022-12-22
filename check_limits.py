from check_battery_condition import battery_is_ok
from check_soc import check_soc
from check_temperature import check_temperature
from check_charge_rate import check_charge_rate

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
    assert(battery_is_ok(0, 80, 0.8) is True)
    assert(battery_is_ok(-1, 19, 0.9) is False)
    assert(battery_is_ok(1, 79 , 0.7) is True)
    assert(battery_is_ok(40, 81, 0.8) is False)
    assert(check_soc(79) is True)
    assert(check_soc(80) is True)
    assert(check_soc(81) is False)
    assert(check_soc(19) is False)
    assert(check_soc(20) is True)
    assert(check_soc(21) is True)
    assert(check_temperature(1) is True)
    assert(check_temperature(-1) is False)
    assert(check_temperature(0) is True)
    assert(check_temperature(1) is True)
    assert(check_temperature(40) is True)
    assert(check_temperature(45) is True)
    assert(check_temperature(50) is False)
    assert(check_charge_rate(0.9) is False)
    assert(check_charge_rate(0.8) is True)
    assert(check_charge_rate(0.7) is True)
