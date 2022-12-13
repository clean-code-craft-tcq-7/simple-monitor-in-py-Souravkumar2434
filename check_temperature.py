
def check_temperature(temperature):
    if temperature < 0 or temperature > 45:
        print("Temperature of battery is not OK!")
        return False
    print("Temperature of battery is OK!")
    return True
