# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 17:06:45 2022

@author: PGS2KOR
"""
import take_input_for_language as tl


global LANGUAGE
LANGUAGE = tl.language


def print_in_English(flag, *args):
    if flag == True:
        print(" Paramter value is OK! : ", args)
        return
    print(" Parameter value is not OK! : ", args)
    return
    
def print_in_German(flag, *args):
    if flag == True:
        print(" Parameterwert ist nicht OK! : ", args)
        return
    print(" Parameterwert ist in Ordnung! : ", args)
    return
    
if LANGUAGE == 'ENGLISH':
    print_msg = print_in_English
elif LANGUAGE == 'GERMAN':
    print_msg = print_in_German