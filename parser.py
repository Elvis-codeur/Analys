# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:31:05 2020

@author: elvis
"""
TABLES_NAMES = ["Tab_A","Tab_B","Tab_C","Tab_D","Tab_E","Tab_F","Tab_G",
                   "Tab_H","Tab_I","Tab_J","Tab_K","Tab_L","Tab_M",
                   "Tab_N","Tab_O","Tab_P","Tab_Q","Tab_R","Tab_S","Tab_T","Tab_U",
                   "Tab_V","Tab_W","Tab_X","Tab_Y","Tab_Z"]
            
def get_fonc_and_arg(text):
    for i in range(len(text)):
        if text[i] == "(":
            return text[0:i],text[i+1:len(text)-1]
            break
        
def get_tab_pos(text):
    for i in range(len(TABLES_NAMES)):
        if TABLES_NAMES[i] == text:
            return i
            break
        
def is_table_name(text):
    state = False
    for i in range(len(TABLES_NAMES)):
        if TABLES_NAMES[i] == text:
            state = True
            return state
            break


        
        