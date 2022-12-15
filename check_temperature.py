MINIMUM_THRESHOLD_FOR_TEMPERATURE = 0
MAXIMUM_THRESHOLD_FOR_TEMPERATURE = 45
def check_temperature(temperature):
    if temperature < MINIMUM_THRESHOLD_FOR_TEMPERATURE or temperature > MAXIMUM_THRESHOLD_FOR_TEMPERATURE:
        print("Temperature of battery is not OK!")
        return False
    print("Temperature of battery is OK!")
    return True
