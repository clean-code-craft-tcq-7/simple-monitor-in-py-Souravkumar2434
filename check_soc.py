
def check_soc(soc):
    if soc < 20 or soc > 80:
        print("State of charge of battery is not OK!")
        return False
    print("State of charge of battery is OK!")
    return True
