
def check_soc(soc):
    soc_check = True
    if soc < 20 or soc > 80:
       soc_check =  False
    return soc_check
