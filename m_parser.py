# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:31:05 2020

@author: elvis
"""
TABLES_NAMES = ["Tab_A","Tab_B","Tab_C","Tab_D","Tab_E","Tab_F","Tab_G",
                   "Tab_H","Tab_I","Tab_J","Tab_K","Tab_L","Tab_M",
                   "Tab_N","Tab_O","Tab_P","Tab_Q","Tab_R","Tab_S","Tab_T","Tab_U",
                   "Tab_V","Tab_W","Tab_X","Tab_Y","Tab_Z"]

def arrondir(text,c):
    for i in range(len(text)):
        if text[i] == ".":
            return text[0:i+c+1]
        

            
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
  
def get_arguments(text):
    a = list()
    for i in range(len(text)):
        if text[i] == ",":
            a.append(i)
    
    a.insert(0,0)
    a.append(len(text))
    args = list()
    for i in range(1,len(a)):
        if i == 1:    
            args.append(text[a[i-1]:a[i]])
        else:
            args.append(text[a[i-1]+1:a[i]])
        
    return args
   
def get_arguments_sepa(text,separator):
    a = list()
    for i in range(len(text)):
        if text[i] == separator:
            a.append(i)
    
    a.insert(0,0)
    a.append(len(text))
    args = list()
    for i in range(1,len(a)):
        if i == 1:    
            args.append(text[a[i-1]:a[i]])
        else:
            args.append(text[a[i-1]+1:a[i]])
        
    return args     
        
def is_only_number(tab):
    result = True
    for i in range(len(tab)):
        if tab[i] != "":
            try:
                tab[i] = int(tab[i])
            except:
                try:
                    tab[i] = float(tab[i]) 
                except:
                    result = False
                    return result,i
                break
            
    return result 
def all_to_number(tab):
    """ Permet de transformer les case vides en cases contenant 0 pour les fonctions comme mean etc """

def somme(tab):
    a = 0
    for i in range(len(tab)):
        try:
            a = a+int(tab[i])
        except:
            try:
                a = a+float(tab[i])
            except:
                break
    return a

def produit_(tab):
    a = 1
    for i in range(len(tab)):
        try:
            a = a*int(tab[i])
        except:
            try:
                a = a*float(tab[i])
            except:
                break
    return a
  
def get_element_poses(tab,element):
    compteur = list()
    for i in range(len(tab)):
        if tab[i] == element:
            compteur.append(i)
    return compteur
            
def str_to_list(st):
    a = list()
    for i in range(len(st)):
        a.append(st[i])
    return a

def list_to_str(tab):
    a = str()
    for i in range(len(tab)):
        a = a+str(tab[i])
    return a


    
"""

import random
a = list()
for i in range(4):
    a.append(str(random.randint(0,25)))
    
print(a)
print(m_sort(a))             

""" 

def generate_sorting_list(tab_a,tab_b):
    l = list()
    a = list(tab_a)
    b = list(tab_b)
    
    for i in range(len(a)):
        l.append(get_element_pos(a,b[i]))
        a[get_element_pos(a,b[i])] = "\n\n\n"
        
    #print(a)
        
    return l
        
def get_element_pos(tab,element):
    compteur = -1
    for i in range(len(tab)):
        if tab[i] == element:
            return i
        
    return compteur
def is_table_name(text):
    state = False
    for i in range(len(TABLES_NAMES)):
        if TABLES_NAMES[i] == text:
            state = True
            return state
            break
        
def to_number(tab,zero = False):
    for i in range(len(tab)):
        try:
            tab[i] = int(tab[i])
        except:
            try:    
                tab[i] = float(tab[i])
            except:
                if(zero):
                    tab[i] = 0
        
            
    return tab
            
            
def has_equal_symbol(text):
    state = False
    for i in range(len(text)):
        if text[i] == "=":
            state = True
            return state
            break
def get_tabes(text):
    l = list()
    for i in range(len(text)-5):
        if text[i] == "T":
            l.append(text[i:i+5])
    return l

def tab_definition_to_general_list_definition(text):
    #print(text,  "*******")
    text = cut_with_math_symbols(text)
    #print(text)
    for i in range(len(text)):
        text[i] = tab_definition_to_general_list_definition_1(text[i])
        
    t = str()
    for i in range(len(text)):
        t = t+text[i]
    
    return t
        
 
def get_radical_increment(text):
    """ Permet de  prélever comment le radical s'incrémente 
        Par exmple Tab[i] donne i
                   Tab[i-10] donne i - 10
                   etc
    """
    a,b = 0,0
    
    for i in range(len(text)):
        if text[i] == "[":
            a = i
        if text[i] == "]":
            b = i
    return text[a+1:b]
            

def tab_definition_to_general_list_definition_1_1(text):
    """ Retourne l'écriture basée sur general_list de la colonne """
    if text[0] == "T":
        return  "self.general_list["+str(get_tab_pos(text[0:5]))+"]"

   
def tab_definition_to_general_list_definition_1(text):
    for i in range(len(text)):
        if text[i] == "T":
            u =0
            for u in range(i,len(text)):
                if text[u] == "[":
                    break
            ele = text[i:u]
            p = text[0:i]
            s = text[u:len(text)]
            c = "self.general_list["+str(get_tab_pos(ele))+"]"
            text = p+c+s
            
    return text   
def is_math_symbols(a):
    if a == "+" or a == "-" or a == "/" or a=='*':
        return True
    else:
        return False
            
def cut_with_math_symbols(text):
    a = list()
    for i in range(len(text)):
        if is_math_symbols(text[i]):
            a.append(i)
            
    a.insert(0,0)
    a.append(len(text))
    args = list()
    for i in range(1,len(a)):
        if i == 1:    
            args.append(text[a[i-1]:a[i]])
        else:
            args.append(text[a[i-1]:a[i]])
        
    return args    
def equal_symbol_pos(text):
    for i in range(len(text)):
        if text[i] == "=":
            return i
            break
  
def is_only_tab_name(text):
    state = True
    for i in range(len(text)):
        if is_table_name(text[i]) == False:
            state = False
            return state,i
            break
    return state


def sort_with_list(list_to_be_sorted,sorting_list):
    a = list()
    #print(list_to_be_sorted)
    for i in range(len(sorting_list)):
        a.append(list_to_be_sorted[sorting_list[i]])
    
        #a.append(list_to_be_sorted[])
        
    return a
    
    
def m_sort(tab = [],key = str,reverse = False):
    final_tab = []
    a = tab
    b = str(tab)
    #print(" a ...",a," tab ...",tab)
    
    if key == str:
        if reverse == False:
            for i in range(len(tab)):
                u = max(a,key = str)
                final_tab.append(u)
                a.remove(u)
        else:
            for i in range(len(tab)):
                u = max(a,key = str)
                final_tab.append(u)
                a.remove(u)
    else:
        if reverse == False:
            for i in range(len(tab)):
                u = max(a,key = float)
                final_tab.append(u)
                a.remove(u)
        else:
            for i in range(len(tab)):
                u = max(a,key = float)
                final_tab.append(u)
                a.remove(u)
    return final_tab,b
        
def str_to_list_(text):
    text = text[1:len(text)-1]
    return get_arguments(text)



"""
y = [[14, 2, 4, 7, 7, 8], ["a", "b", "c", "d", "e", "f"]]
s = list(y[0])
s.sort()
a = generate_sorting_list(y[0],s)
print(a)
l = list()
for i in range(len(y)):
    l.append(sort_with_list(y[i],a))
    
print(y,l)
"""
