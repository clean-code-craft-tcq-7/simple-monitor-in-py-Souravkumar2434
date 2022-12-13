
def check_charge_rate(charge_rate):
    if charge_rate > 0.8:
        print("Charge rate of battery is not OK!")
        return False
    print("Charge rate of battery is OK!")
    return True
    
