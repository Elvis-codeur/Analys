# -*- coding: utf-8 -*-
"""
Created on Mon May 31 06:32:23 2021

@author: Elvis
"""
import numpy as np
import pandas as pd

"""
VOICI LES BALISES DE MON FICHIER WDATA

<data>
Pour les donnée
</data>
<code>
Pour les différents codes
</code>
<script>
Pour chaque bout de code 
</script>
"""
def remove_alinea(text):
    for i in range(len(text)):
        if text[i] == "\n" :
            a = 0
def csv_read(text):
    last = -1
    result = []
    columnCount = 0
    for i in range(len(text)):
        if(text[i] == ","):
            columnCount = columnCount + 1
            result.append([])
        elif text[i] == "\n":
            columnCount = columnCount + 1
            result.append([])
            break
        
    i = 0 
    u = 0
    while i < len(text):
        if(text[i]== ","or text[i] == "\n"):
            result[u].append(text[last+1:i])
            u = u + 1
            if(u > columnCount-1):
                u = 0
                
            last = i 
        i = i + 1
        

    return result
        
def get_code(text):
    d = 0
    f = 0 
    for i in range(len(text)-6):
        if(text[i:i+6]) == "<code>":
            d = i
        if(text[i:i+7]) == "</code>":
            f = i
            break
    code = text[d+7:f] 
    return code

def get_scripts(text):
    d = 0
    f = 0
    datas = []
    for i in range(len(text)-8):
        if(text[i:i+8]) == "<script>":
            d = i 
        if(text[i:i+9]) == "</script>":
            f = i
            datas.append(text[d+8:f])
    
    return datas
    
    
def get_datas(text):
    d = 0
    f = 0
    datas = []
    for i in range(len(text)-6):
        if(text[i:i+6]) == "<data>":
            d = i 
        if(text[i:i+7]) == "</data>":
            f = i
            datas.append(text[d+7:f])
    
    return datas
def open_file(name):
    generalList = []
    f = open(name,"r",encoding = "utf-8")
    a = f.readline()
    #print(len(a),len("ANALYS-file-version-2"))
    
    if(a == "ANALYS-file-version-2\n"):
        a = f.read()
        datas = get_datas(str(a))
        scripts = get_scripts(str(a))
        generalList = csv_read(datas[0])
            
        return (generalList,scripts)
        f.close()
        
    else:
        print("nono")
        f.close()
        df = pd.read_csv(name,header = None,sep = ",")
        rowCount = len(df)
        columnCount = len(df.columns)
        #print(df)
        #print(self.rowCount)
        #print(self.columnCount)
                
        if columnCount > 26:
            columnCount = 26
                
        for i in range(columnCount):
            generalList.append(list(df[i]))
            
        #print(generalList)
        return (generalList)
    
def copy_list(r,copy):
    for i in range(len(copy)):
        r.append(copy[i])
    return r
    
A = """                            <data>
'195', '211', '110', '305', '379', '301',  
 </data>                       
 
 <data>
'195', '211', '110', '305', '379', '301',  
 </data>                       
 
 <data>
'195', '211', '110', '305', '379', '301',  
 </data>                       
 
 <data>
'195', '211', '110', '305', '379', '301',  
 </data>                       
 
 <code>
 
 
<script> 
R = 220
L = 0.1
Y = 0
I_0 = 1

</script>
<script> 
a = np.arange(0,0.004,0.0001)
b = []
for i in range(len(a)):
    b.append(courant_rl_serie(R,L,Y,I_0,a[i]))
</script>

print(max(a))
print(len(a))
#plt.yscale("log")
plt.plot(a,b)
plt.show()

</code>

 """
#print(csv_read("""'195', '211', '110'\n '305', '379', '301',"""))
#print(len(open_file("x.wdata")[0]))
