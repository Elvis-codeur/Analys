from m_parser import *

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
        
def str_to_list(text):
    text = text[1:len(text)-1]
    return get_arguments(text)
            
