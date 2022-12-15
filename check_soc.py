MINIMUM_THRESHOLD_FOR_SOC = 20
MAXIMUM_THRESHOLD_FOR_SOC = 80
def check_soc(soc):
    if soc < MINIMUM_THRESHOLD_FOR_SOC or soc > MAXIMUM_THRESHOLD_FOR_SOC:
        print("State of charge of battery is not OK!")
        return False
    print("State of charge of battery is OK!")
    return True
