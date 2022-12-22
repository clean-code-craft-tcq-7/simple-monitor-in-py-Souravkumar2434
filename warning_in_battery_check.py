# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 16:30:11 2022

@author: PGS2KOR
"""
from Battery_paramteres_threshold import BATTERY_PARAM_THD, MAXIMUM_THRESHOLD_FOR_SOC,\
 MINIMUM_THRESHOLD_FOR_SOC, MINIMUM_THRESHOLD_FOR_TEMPERATURE, MAXIMUM_THRESHOLD_FOR_TEMPERATURE,\
     MAXIMUM_THRESHOLD_FOR_CR, WARN_TOL_FOR_TEMP, WARN_TOL_FOR_CR, WARN_TOL_FOR_SOC
from print_messages import print_msg

def cal_warning_thd(val , tol):
    return val + (val / 100) * tol

def check_temperature_warning(temperature):
    warning_thd = cal_warning_thd(temperature, WARN_TOL_FOR_TEMP)
    low_warning_thd = MINIMUM_THRESHOLD_FOR_TEMPERATURE + warning_thd
    high_warning_thd = MAXIMUM_THRESHOLD_FOR_TEMPERATURE - warning_thd
    
    if ((temperature < low_warning_thd) and (temperature > MINIMUM_THRESHOLD_FOR_TEMPERATURE)\
        or (temperature < MAXIMUM_THRESHOLD_FOR_TEMPERATURE) and (temperature > high_warning_thd)):
        print_msg(False, 'Temperature', 'WARNING')
        return
    #print_msg(False, 'Temperature', 'WARNING')
    return

def check_soc_warning(soc):
    warning_thd = cal_warning_thd(soc, WARN_TOL_FOR_SOC)
    low_warning_thd = MINIMUM_THRESHOLD_FOR_SOC + warning_thd
    high_warning_thd = MAXIMUM_THRESHOLD_FOR_SOC - warning_thd
    
    if ((soc < low_warning_thd) and (soc > MINIMUM_THRESHOLD_FOR_SOC)\
        or (soc < MAXIMUM_THRESHOLD_FOR_SOC) and (soc > high_warning_thd)):
        print_msg(False, 'SOC', 'WARNING')
        return
    #print_msg(False, 'Temperature', 'WARNING')
    return

def check_charge_rate_warning(charge_rate):
    warning_thd = cal_warning_thd(charge_rate, WARN_TOL_FOR_CR)
    high_warning_thd = MAXIMUM_THRESHOLD_FOR_CR - warning_thd
    
    if ((charge_rate < MAXIMUM_THRESHOLD_FOR_CR) and (charge_rate > high_warning_thd)):
        print_msg(False, 'CHARGE_RATE', 'WARNING')
        return
    #print_msg(False, 'Temperature', 'WARNING')
    return


