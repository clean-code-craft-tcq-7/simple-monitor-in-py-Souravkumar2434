THRESHOLD_FOR_CHARGE_RATE = 0.8
def check_charge_rate(charge_rate):
    if charge_rate > THRESHOLD_FOR_CHARGE_RATE:
        print("Charge rate of battery is not OK!")
        return False
    print("Charge rate of battery is OK!")
    return True
    
