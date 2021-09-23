# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:30:17 2020

@author: elvis
"""
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from m_parser import *
from translation.translator import translate
import math

class ScriptClass(QObject):
    send_warning = pyqtSignal(str)
    def __init__(self,tab):
        super().__init__()
        self.general_list = tab
        
        
    def to_fonction(self,text):
        fonc,arg = get_fonc_and_arg(text)
        if fonc == "remove":
            return self.remove(text)
        elif fonc == "sort":
            return self.sort(text)
        elif fonc == "delete":
            return self.delete(text)
        elif fonc == "mean":
            return self.mean(text)
        elif fonc == "variance":
            return self.variance(text)
        elif fonc == "ecart_type":
            return math.sqrt(self.variance(text))
        elif fonc == "max":
            return self.ma(text)
        elif fonc == "min":
            return self.mi(text)
        elif fonc == "to_percent":
            return self.to_percent(text)
        elif fonc == "to_freq":
            return self.to_freq(text)
        elif fonc == "count":
            return self.count(text)
        elif fonc == "general_sort":
            return self.general_sort(text)    
        elif fonc == "sum":
             return self.somme(text)
        elif fonc == "produce":
             return self.produit(text)  
        elif fonc == "sub":
            return self.sub(text)
        elif fonc == "add":
            return self.add(text)
        elif fonc == "mul":
            return self.mul(text)
        elif fonc == "div":
            return self.div(text)
        elif fonc == "operation":
            return self.operation(text)
        elif fonc == "subtitute":
            return self.subtitute(text)
        elif fonc == "fill":
            return self.fill(text)
        elif fonc == "upper":
            return self.upper(text)
        elif fonc == "lower":
            return self.lower(text)
        elif fonc == "alloc":
            return self.alloc(text)
        elif fonc == "translate":
            return self.translate(text)
        else:
            self.send_warning.emit("La fonction "+ fonc +" n'existe pas")
            
    def translate(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        if len(arg) == 5:
            if is_table_name(arg[0]):
                if is_table_name(arg[1]):
                    try:
                        arg[2] = int(arg[2]) -1
                    except:
                        self.send_warning.emit("Le troisième argument doit être un entier")
                    try:
                        arg[3] = int(arg[3])
                    except:
                        self.send_warning.emit("Le quatrième arguement doit être un entier")
                        
                    for i in range(get_tab_pos(arg[0]),get_tab_pos(arg[1])+1):
                        for u in range(arg[2],arg[3]):
                            
                            self.general_list[i][u] = translate(self.general_list[i][u],arg[4])
                            
                    #print(self.general_list)
                    return self.general_list
                else:
                    self.send_warning.emit("Le tableau "+ arg[1] +" n'existe pas")
            else:
                self.send_warning.emit("Le tableau "+ arg[0] +" n'existe pas")
                
                
        elif len(arg) == 4:
            if is_table_name(arg[0]):
                if is_table_name(arg[1]):
                    try:
                        arg[2] = int(arg[2])-1
                    except:
                        self.send_warning.emit("Le troisième argument doit être un entier")    
                    
                    for i in range(get_tab_pos(arg[0]),get_tab_pos(arg[1])+1):
                        self.general_list[i][arg[2]] = translate(self.general_list[i][arg[2]],arg[3])
                    return self.general_list
                
                elif arg[1].isdigit():
                    try:
                        arg[1] = int(arg[1]) -1
                    except:
                        self.send_warning.emit("Le second argument doit être un entier")
                    
                    try:
                        arg[2] = int(arg[2])
                    except:
                        self.send_warning.emit("Le troisième argument doit être un entier") 
                    
                    for i in range(arg[1],arg[2]):
                        self.general_list[get_tab_pos(arg[0])][i] = translate(self.general_list[get_tab_pos(arg[0])][i],arg[3])
                        
                    return self.general_list
                else:
                    self.send_warning.emit("Le deuxième argument n'est pas valide")
            
                    
        elif len(arg) == 3:
            if is_table_name(arg[0]):
                try:
                    arg[1] = int(arg[1]) -1
                except:
                    self.send_warning.emit("Le second argument doit être un entier")
                    
                self.general_list[get_tab_pos(arg[0])][arg[1]] = translate(self.general_list[get_tab_pos(arg[0])][arg[1]],arg[2])
                return self.general_list
                
    def alloc(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments_sepa(arg,";")
        print(arg)
        if len(arg) == 3:
            
            if is_table_name(arg[0]):
                try:
                    arg[1] = int(arg[1]) -1
                except:
                    self.send_warning.emit("Le second argument doit être un entier positif")
                
                if(arg[1] > len(self.general_list[get_tab_pos(arg[0])])):
                    for i in range(len(self.general_list[get_tab_pos(arg[0])]),arg[1]):
                        self.general_list[get_tab_pos(arg[0])].append("")
                        
                self.general_list[get_tab_pos(arg[0])][arg[1]] = arg[2]
                
                return self.general_list
                
            else:
                self.send_warning.emit("La colonne "+arg[0] + " n'existe pas ")
                
                
                
        elif len(arg) == 4:
            if is_table_name(arg[0]):
                try:
                    arg[1] = int(arg[1])
                except:
                    self.send_warning.emit("Le second argument doit être un entier positif")
                
                if arg[2] == "f":
                    a = self.to_fonction(arg[3])
                    print(a)

                    if(arg[1] > len(self.general_list[get_tab_pos(arg[0])])):
                        for i in range(len(self.general_list[get_tab_pos(arg[0])]),arg[1]):
                            self.general_list[get_tab_pos(arg[0])].append("")
            
                    self.general_list[get_tab_pos(arg[0])][arg[1]-1] = a
            
                    return self.general_list
            
    def upper(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        if len(arg) == 1:
            if type(is_table_name(arg[0])) == bool:
                for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                    self.general_list[get_tab_pos(arg[0])][i]  = self.general_list[get_tab_pos(arg[0])][i].upper()
                
            return self.general_list
        
        elif len(arg) == 3:
            
            try:
                arg[1] = int(arg[1])
            except:
                self.send_warning.emit("Le deuxième paramètre doit être un nombre entier")
                
            try:
                arg[2] = int(arg[2])
            except:
                self.send_warning.emit("Le troisième paramètre doit être un nombre entier") 
                
                
            for i in range(arg[1]-1,arg[2]):
                self.general_list[get_tab_pos(arg[0])][i]  = self.general_list[get_tab_pos(arg[0])][i].upper()
                
            return self.general_list
                
        elif len(arg) == 4:
            try:
                arg[1] = int(arg[1])
            except:
                self.send_warning.emit("Le deuxième paramètre doit être un nombre entier")
                
            try:
                arg[2] = int(arg[2])
            except:
                self.send_warning.emit("Le troisième paramètre doit être un nombre entier")
                
            try:
                arg[3] = int(arg[3])
            except:
                self.send_warning.emit("Le quatrième paramètre doit être un nombre entier")
                
                
            for i in range(arg[1]-1,arg[2]):
                a = self.general_list[get_tab_pos(arg[0])][i][arg[3]-1].upper()
                
                b = str_to_list(self.general_list[get_tab_pos(arg[0])][i])
                b[arg[3]-1] = a
                self.general_list[get_tab_pos(arg[0])][i] = list_to_str(b)
                
            return self.general_list
        
        elif len(arg) == 5:
            try:
                arg[1] = int(arg[1])
            except:
                self.send_warning.emit("Le deuxième paramètre doit être un nombre entier")
                
            try:
                arg[2] = int(arg[2])
            except:
                self.send_warning.emit("Le troisième paramètre doit être un nombre entier")
                
            try:
                arg[3] = int(arg[3])
            except:
                self.send_warning.emit("Le quatrième paramètre doit être un nombre entier")
                
            try:
                arg[4] = int(arg[4])
            except:
                self.send_warning.emit("Le cinquième  paramètre doit être un nombre entier")
                
                
            for i in range(arg[1]-1,arg[2]):
                a = self.general_list[get_tab_pos(arg[0])][i][arg[3]-1:arg[4]].upper()
                
                b = str_to_list(self.general_list[get_tab_pos(arg[0])][i])
                b[arg[3]-1:arg[4]] = a
                self.general_list[get_tab_pos(arg[0])][i] = list_to_str(b)
                
            return self.general_list
                
                
    def lower(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        if len(arg) == 1:
            if type(is_table_name(arg[0])) == bool:
                for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                    self.general_list[get_tab_pos(arg[0])][i]  = self.general_list[get_tab_pos(arg[0])][i].lower()
                
            return self.general_list
        
        elif len(arg) == 3:
            
            try:
                arg[1] = int(arg[1])
            except:
                self.send_warning.emit("Le deuxième paramètre doit être un nombre entier")
                
            try:
                arg[2] = int(arg[2])
            except:
                self.send_warning.emit("Le troisième paramètre doit être un nombre entier") 
                
                
            for i in range(arg[1]-1,arg[2]):
                self.general_list[get_tab_pos(arg[0])][i]  = self.general_list[get_tab_pos(arg[0])][i].lower()
                
            return self.general_list
                
        elif len(arg) == 4:
            try:
                arg[1] = int(arg[1])
            except:
                self.send_warning.emit("Le deuxième paramètre doit être un nombre entier")
                
            try:
                arg[2] = int(arg[2])
            except:
                self.send_warning.emit("Le troisième paramètre doit être un nombre entier")
                
            try:
                arg[3] = int(arg[3])
            except:
                self.send_warning.emit("Le quatrième paramètre doit être un nombre entier")
                
                
            for i in range(arg[1]-1,arg[2]):
                a = self.general_list[get_tab_pos(arg[0])][i][arg[3]-1].lower()
                
                b = str_to_list(self.general_list[get_tab_pos(arg[0])][i])
                b[arg[3]-1] = a
                self.general_list[get_tab_pos(arg[0])][i] = list_to_str(b)
                
            return self.general_list
        
        elif len(arg) == 5:
            try:
                arg[1] = int(arg[1])
            except:
                self.send_warning.emit("Le deuxième paramètre doit être un nombre entier")
                
            try:
                arg[2] = int(arg[2])
            except:
                self.send_warning.emit("Le troisième paramètre doit être un nombre entier")
                
            try:
                arg[3] = int(arg[3])
            except:
                self.send_warning.emit("Le quatrième paramètre doit être un nombre entier")
                
            try:
                arg[4] = int(arg[4])
            except:
                self.send_warning.emit("Le cinquième  paramètre doit être un nombre entier")
                
                
            for i in range(arg[1]-1,arg[2]):
                a = self.general_list[get_tab_pos(arg[0])][i][arg[3]-1:arg[4]].lower()
                
                b = str_to_list(self.general_list[get_tab_pos(arg[0])][i])
                b[arg[3]-1:arg[4]] = a
                self.general_list[get_tab_pos(arg[0])][i] = list_to_str(b)
                
            return self.general_list
                
            
                    
    def fill(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        
        if len(arg) == 4:
            try:
                arg[2] = int(arg[2])
            except:
                self.send_warning.emit("Le troisème argument doit être un nombre entier")
                    
            try:
                arg[3] = int(arg[3])
                    
            except:
                    self.send_warning.emit("Le quatrième argument doit être un nombre entier")
                    
            code = ""
            code = code + "from numpy import *\n"
            code = code + "x = arange("+str(arg[2])+","+str(arg[3]+1)+")"+"\n"
        
            if is_table_name(arg[0]):
                code = code + "self.general_list["+str(get_tab_pos(arg[0]))+"] = "+" list("+arg[1]+")"
                  
            print(code,"\n")
            
            print("**********************",self.general_list[get_tab_pos(arg[0])])
            
            f = open("fill_source.txt","w")
            f.write(code)
            f.close()
            c = compile(code,"fill_débug.txt","exec")
            result =  0
            try:
                result = exec(c)
                print("yes")
            
            except Exception as e:
                print(e)
            
            return self.general_list
                
            
    def subtitute(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        
        if len(arg) == 3:
            if is_table_name(arg[0]):
                for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                    if self.general_list[get_tab_pos(arg[0])][i] == arg[1]:
                       self.general_list[get_tab_pos(arg[0])][i] = arg[2]
                       
                return self.general_list
                       
        elif len(arg) == 4:
            if is_table_name(arg[0]):
                try:
                    arg[3] = int(arg[3])
                except:
                    self.send_warning.emit("Le quatrième argument doit être un nombre entier")
                    
                for i in range(arg[3],len(self.general_list[get_tab_pos(arg[0])])):
                    if self.general_list[get_tab_pos(arg[0])][i] == arg[1]:
                       self.general_list[get_tab_pos(arg[0])][i] = arg[2]
                       
                return self.general_list
        
        elif len(arg) == 5:
            if is_table_name(arg[0]):
                try:
                    arg[3] = int(arg[3])
                except:
                    self.send_warning.emit("Le quatrième argument doit être un nombre entier")
                    
                try:
                    arg[4] = int(arg[4])
                    
                except:
                    self.send_warning.emit("Le cinquième argument doit être un nombre entier")
                    
                for i in range(arg[3],arg[4]):
                    if self.general_list[get_tab_pos(arg[0])][i] == arg[1]:
                       self.general_list[get_tab_pos(arg[0])][i] = arg[2]
                       
                return self.general_list
                
    def operation(self,text):
        # On récupere la fonction et les arguments
        fonc,arg = get_fonc_and_arg(text)
        print(arg)
        
        if has_equal_symbol(arg):
            # On sépare les arguements en deux
            # D'une part la partie allant du début à la position de =
            # D'autre part la partie allant de la position suivant = à la fin
            sep = equal_symbol_pos(arg)
            
            # Ce qui vient avant le signe d'égalité
            radical = arg[0:sep]
            rad_inc = get_radical_increment(radical) 
            #print("\n\nVoici le radical brute ",radical,"et ce qu'on en retire ")
            # Ce qui vient après
            reste =arg[sep+1:len(arg)]
            # On récupere les argument restant xxxxx,borne1,borne2
            reste = get_arguments(reste)
            
            ra_tab = get_tabes(radical)
            print(ra_tab)
            re_tab = get_tabes(reste[0])
            
            if len(ra_tab) == 1:
                if is_table_name(ra_tab[0]):
                    if is_only_tab_name(re_tab):
                        try:
                            reste[1] = int(reste[1])
                        except:
                            self.send_warning.emit(str(reste[1]) +" n' est pas un nombre entier positif")
                            
                        try:
                            reste[2] = int(reste[2])
                        except:
                            self.send_warning.emit(str(reste[2]) +" n' est pas un nombre entier positif")
                            
                        for i in range(len(re_tab)):
                            if is_only_number(self.general_list[get_tab_pos(re_tab[i])]) == False:
                                self.send_warning.emit("L'élément se trouvant à la case "+
                                                       str(is_only_number(re_tab[i])[1])+" n'est pas un nombre")
                        
                        print("\n\n\n This is ",re_tab,"\nand ",ra_tab)
                        
                        a = int(reste[1])-1
                        b = int(reste[2])
                        
                        for i in range(len(re_tab)):
                            self.general_list[get_tab_pos(re_tab[i])][a:b] = to_number(self.general_list[get_tab_pos(re_tab[i])][a:b],
                                                                                       zero = True)
                                
                            
                        code = str()
                        code = code + "for i in range("+str(reste[1]-1)+","+str(reste[2])+"):\n"
                        code = code + "    "
                        code = code +tab_definition_to_general_list_definition_1_1(ra_tab[0])+\
                        "["+rad_inc+ "]" +"="
                        
                        code = code + tab_definition_to_general_list_definition(reste[0])+"\n"
                        #code = code +"print(self.general_list[0])"
                        
                        if len(self.general_list[get_tab_pos(ra_tab[0])]) < int(reste[2]):
                            for i in range(int(reste[2])):    
                                self.general_list[get_tab_pos(ra_tab[0])].append("")
                        
                        print("\n\n\n",code,"\n\n\n")
                        f = open("source.txt","w")
                        f.write(code)
                        f.close()
                        c = compile(code,"débug.txt","exec")
                        try:
                            exec(c)
                            print("yes")
                        except Exception as e:
                            print(e)
                            
                        return self.general_list

                            
                
                    else:
                        self.send_warning.emit(str(ret_tab[is_only_tab_name(re_tab)[1]])+ " ne désigne aucune colonne. Vous devez le changer")
                    
                else:
                    self.send_warning.emit(str(ra_tab[0]) +" ne désigne aucune colonne. Vous devez le changer")
            else:
                self.send_warning.emit(str("Vous ne pouvez choisir qu'une seule colonne pour acceuillir les données"))
            
        
    def is_crochet_syntax_correct(self,text):
        if text[0] == "[":
            if text[len(text)-1] == "]":
                return True
            else:
                self.send_warning.emit("Il manque ] à la fin de l'argument "+str(text))
        else:
            self.send_warning.emit("Il manque [ au début  de l'argument "+str(text))
            
    def to_freq(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        if len(arg) == 2:
            try:
                arg[1] = int(arg[1])
            except:
                self.send_warning.emit("Le second argument doit être un nommbre")
            if is_table_name(arg[0]):
                if is_only_number(arg[0]):
                    a = somme(self.general_list[get_tab_pos(arg[0])])
                    for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                        self.general_list[get_tab_pos(arg[0])][i] = arrondir(str(float(self.general_list[get_tab_pos(arg[0])][i])/a),arg[1])
                    return self.general_list
                else:
                    self.send_warning.emit("L'élément se trouvant à la case "+ str(is_only_number(arg[0])[1]) +" n'est pas un nombre")
            else:
                self.send_warning.emit("La colonne "+str(arg[0])+" n'existe pas")
                
        elif len(arg) == 3:
            if is_table_name(arg[0]):
                if is_only_number(arg[0]):
                   
                    try:
                        arg[1] = int(arg[1])
                    except:
                        self.send_warning.emit(arg[1]+ " ne peut être utilisé comme indice de début de l'algorithme")
                    
                    try:
                        arg[2] = int(arg[2])
                    except:
                        self.send_warning.emit("Le troisième argument doit être un nommbre")
                            
                            
                    a = somme(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])])
                    for i in range(arg[1]-1,len(self.general_list[get_tab_pos(arg[0])])):
                        self.general_list[get_tab_pos(arg[0])][i] =arrondir(str(float(self.general_list[get_tab_pos(arg[0])][i])/a),arg[2])
                    return self.general_list
                else:
                    self.send_warning.emit("L'élément se trouvant à la case "+ str(is_only_number(arg[0])[1]) +" n'est pas un nombre")
            else:
                self.send_warning.emit("La colonne "+str(arg[0])+" n'existe pas")
        
        elif len(arg) == 4:
            if is_table_name(arg[0]):
                if is_only_number(arg[0]):
                    
                    try:
                        arg[1] = int(arg[1])
                    except:
                        self.send_warning.emit(arg[1]+ " ne peut être utilisé comme indice de début de l'algorithme")
                        
                    try:
                        arg[2] = int(arg[2])
                    except:
                        self.send_warning.emit(arg[2]+ " ne peut être utilisé comme indice de début de l'algorithme")
                        
                    try:
                        arg[3] = int(arg[3])
                    except:
                        self.send_warning.emit("Le quatrième argument doit être un nommbre")
                        
                    a = somme(self.general_list[get_tab_pos(arg[0])][arg[1]-1:arg[2]])
                              
                    for i in range(arg[1]-1,arg[2]):
                        self.general_list[get_tab_pos(arg[0])][i] = arrondir(str(float(self.general_list[get_tab_pos(arg[0])][i])/a),arg[3])
                    return self.general_list
                else:
                    self.send_warning.emit("L'élément se trouvant à la case "+ str(is_only_number(arg[0])[1]) +" n'est pas un nombre")
            else:
                self.send_warning.emit("La colonne "+str(arg[0])+" n'existe pas")
                
                
            
       
                    
        
    def to_percent(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        
        if len(arg) == 2:
            if is_table_name(arg[0]):
                if is_only_number(arg[0]):
                    
                    try:
                        arg[1] = int(arg[1])
                    except:
                        self.send_warning.emit("Le second argument doit être un nommbre")
                        
                    a = somme(self.general_list[get_tab_pos(arg[0])])
                    for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                        self.general_list[get_tab_pos(arg[0])][i] =arrondir(str(100*float(self.general_list[get_tab_pos(arg[0])][i])/a),arg[1])
                    return self.general_list
                else:
                    self.send_warning.emit("L'élément se trouvant à la case "+ str(is_only_number(arg[0])[1]) +" n'est pas un nombre")
            else:
                self.send_warning.emit("La colonne "+str(arg[0])+" n'existe pas")
                
        elif len(arg) == 3:
            if is_table_name(arg[0]):
                if is_only_number(arg[0]):
                   
                    try:
                        arg[1] = int(arg[1])
                    except:
                        self.send_warning.emit(arg[1]+ " ne peut être utilisé comme indice de début de l'algorithme")
                        
                    try:
                        arg[2] = int(arg[2])
                    except:
                        self.send_warning.emit("Le troisième argument doit être un nommbre")
                        
                    a = somme(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])])
                    for i in range(arg[1]-1,len(self.general_list[get_tab_pos(arg[0])])):
                        self.general_list[get_tab_pos(arg[0])][i] =arrondir(str(100*float(self.general_list[get_tab_pos(arg[0])][i])/a),arg[2])
                    return self.general_list
                else:
                    self.send_warning.emit("L'élément se trouvant à la case "+ str(is_only_number(arg[0])[1]) +"n'est pas un nombre")
            else:
                self.send_warning.emit("La colonne "+str(arg[0])+" n'existe pas")
        
        elif len(arg) == 4:
            if is_table_name(arg[0]):
                if is_only_number(arg[0]):
                    
                    try:
                        arg[1] = int(arg[1])
                    except:
                        self.send_warning.emit(arg[1]+ " ne peut être utilisé comme indice de début de l'algorithme")
                        
                    try:
                        arg[2] = int(arg[2])
                    except:
                        self.send_warning.emit(arg[2]+ " ne peut être utilisé comme indice de début de l'algorithme")
                        
                    try:
                        arg[3] = int(arg[3])
                    except:
                        self.send_warning.emit("Le quatrième argument doit être un nommbre")
                        
                    a = somme(self.general_list[get_tab_pos(arg[0])][arg[1]-1:arg[2]])
                              
                    for i in range(arg[1]-1,arg[2]):
                        self.general_list[get_tab_pos(arg[0])][i] = arrondir(str(100*float(self.general_list[get_tab_pos(arg[0])][i])/a),arg[3])
                    return self.general_list
                else:
                    self.send_warning.emit("L'élément se trouvant à la case "+ str(is_only_number(arg[0])[1]) +" n'est pas un nombre")
            else:
                self.send_warning.emit("La colonne "+str(arg[0])+" n'existe pas")
        
    def ma(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        
        if len(arg) == 2:
            if arg[1] == "float":
                try:     
                    return max(self.general_list[get_tab_pos(arg[0])],key = float)
                except:
                    self.send_warning.emit("L'élément se trouvant à la case "+str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
            elif arg[1] == "str":
                return max(self.general_list[get_tab_pos(arg[0])],key = str)
            else:
                self.send_warning.emit(str(arg[1]) + " n'est pas un argument viable. Il faut utiliser soit float soit str")
        
        elif len(arg) == 3:
            try:
                arg[2] = int(arg[2])
            except:
                self.send_warning.emit(arg[1]+ " ne peut être utilisé comme indice de début de l'algorithme")
                
            if arg[1] == "float":
                try: 
                    return max(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])],key = float)
                except:
                    self.send_warning.emit("L'élément se trouvant à la case "+str(is_only_number(arg[0][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])])[1]) + " n'est pas un nombre")
            elif arg[1] == "str":
                return max(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])],key = str)
            else:
                self.send_warning.emit(str(arg[1]) + " n'est pas un argument viable. Il faut utiliser soit float soit str")
                
        
        elif len(arg) == 4:
             try:
                arg[2] = int(arg[2])
             except:
                self.send_warning.emit(arg[1]+ " ne peut être utilisé comme indice de début de l'algorithme")
                
             try:
                arg[3] = int(arg[3])
             except:
                self.send_warning.emit(arg[2]+ " ne peut être utilisé comme indice de début de l'algorithme")
                
                
             if arg[1] == "float":
                 try:
                     return max(self.general_list[get_tab_pos(arg[0])][arg[1]-1:arg[2]],key = float)
                 except:
                     self.send_warning.emit("L'élément se trouvant à la case"+str(is_only_number(arg[0][arg[1]-1:arg[2]]))+ " n'est pas un nombre")
             elif arg[1] == "str":
                return max(self.general_list[get_tab_pos(arg[0])][arg[1]-1:arg[2]],key = str)
             else:
                 self.send_warning.emit(str(arg[1]) + " n'est pas un argument viable. Il faut utiliser soit float soit str")
            
        
    def mi(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        if len(arg) == 2:
            if arg[1] == "float":
                try:     
                    return min(self.general_list[get_tab_pos(arg[0])],key = float)
                except:
                    self.send_warning.emit(" L'élément se trouvant à la case"+str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
            elif arg[1] == "str":
                return min(self.general_list[get_tab_pos(arg[0])],key = str)
            else:
                 self.send_warning.emit(str(arg[1]) + " n'est pas un argument viable. Il faut utiliser soit float soit str")
        
        
        elif len(arg) == 3:
            try:
                arg[2] = int(arg[2])
            except:
                self.send_warning.emit(arg[1]+ " ne peut être utilisé comme indice de début de l'algorithme")
                
            if arg[1] == "float":
                try: 
                    return min(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])],key = float)
                except:
                    self.send_warning.emit(" L'élément se trouvant à la case "+str(is_only_number(arg[0][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])])[1]) + " n'est pas un nombre")
            elif arg[1] == "str":
                return min(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])],key = str)
            else:
                 self.send_warning.emit(str(arg[1]) + " n'est pas un argument viable. Il faut utiliser soit float soit str")
        
        
        elif len(arg) == 4:
             try:
                arg[2] = int(arg[2])
             except:
                self.send_warning.emit(arg[1]+ " ne peut être utilisé comme indice de début de l'algorithme")
                
             try:
                arg[3] = int(arg[3])
             except:
                self.send_warning.emit(arg[2]+ " ne peut être utilisé comme indice de début de l'algorithme")
                
                
             if is_only_number(self.general_list[get_tab_pos(arg[0])][arg[1]-1:arg[2]]):
                 try:
                     return min(self.general_list[get_tab_pos(arg[0])][arg[1]-1:arg[2]],key = float)
                 except:
                     self.send_warning.emit("L'élément se trouvant à la case "+str(is_only_number(arg[0][arg[1]-1:arg[2]]))+ " n'est pas un nombre")
             elif arg[1] == "str":
                return min(self.general_list[get_tab_pos(arg[0])][arg[1]-1:arg[2]],key = str)
             else:
                 self.send_warning.emit(str(arg[1]) + " n'est pas un argument viable. Il faut utiliser soit float soit str")
                 
        
            
            
    def remove(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        if len(arg) == 1:
            if is_table_name(arg[0]):
                print("Ok")
                del self.general_list[get_tab_pos(arg[0])]
                return self.general_list
            else:
                self.send_warning.emit("La colonne "+str(arg[0])+" n'existe pas")
        else:
            self.send_warning.emit("La méthode </strong> remove </strong>"
                                   "ne recoit qu'une seule variable : le tableau à enlever")
    
    def variance(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        #print(arg)
        
        if len(arg) == 1:
            if is_table_name(arg[0]):
                if type(is_only_number(self.general_list[get_tab_pos(arg[0])]))== bool:
                    a = 0
                    for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                        a = a+ (self.general_list[get_tab_pos(arg[0])][i]-self.mean(text))**2
                    return a/len(self.general_list[get_tab_pos(arg[0])])
                else:
                    self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[0])])[1])+
                                       " n'est pas un nombre")
                        
        elif len(arg) == 2:
            try:
                arg[1] = int(arg[1])
                if is_table_name(arg[0]):
                    if is_only_number(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])]):
                        a = 0
                        for i in range(arg[1]-1,len(self.general_list[get_tab_pos(arg[0])])):
                            a = a+ (self.general_list[get_tab_pos(arg[0])][i]-self.mean(text))**2
                                
                        return a/len(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])])
            
                    else:
                        self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[0])])[1])+
                                       " n'est pas un nombre")
                else:
                    self.send_warning.emit("La colonne "+ arg[0] +" n'existe pas")
                    
            except:
                if is_table_name(arg[0]):
                    if is_table_name(arg[1]):
                        if is_only_number(arg[0]):
                            if is_only_number(arg[1]):
                                a = 0
                                for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                                    a =  a +float(self.general_list[get_tab_pos(arg[1])][i])*(float(self.general_list[get_tab_pos(arg[0])][i]) - self.mean(text))**2    
                            
                                return a/somme(self.general_list[get_tab_pos(arg[1])])
                            else:
                                self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[1])])[1])+
                                       " n'est pas un nombre")
                        else:
                            self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[0])])[1])+
                                       " n'est pas un nombre")
                    else:
                        self.send_warning.emit("La colonne "+ str(arg[1]) +" n'existe pas")
                else:
                    self.send_warning.emit("La colonne "+str( arg[0]) +" n'existe pas")
                    
        elif (len(arg)) == 3:
            if is_table_name(arg[0]):
                    if is_table_name(arg[1]):
                        if is_only_number(arg[0]):
                            if is_only_number(arg[1]):
                                try:
                                    arg[2] = int(arg[2])
                                except:
                                    self.send_warning.emit(arg[2] +" ne peut être utilisé comme indice de début de l'algorithme")
                                
                                a = 0
                                for i in range(arg[2]-1,len(self.general_list[get_tab_pos(arg[0])])):
                                    a =  a +float(self.general_list[get_tab_pos(arg[1])][i])*(float(self.general_list[get_tab_pos(arg[0])][i]) - self.mean(text))**2    
                                
                                return a/somme(self.general_list[get_tab_pos(arg[1])])
                                                 
                            else:
                                
                                self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[1])])[1])+
                                       " n'est pas un nombre")
                        else:
                            self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[0])])[1])+
                                       " n'est pas un nombre")
                    else:
                        try:
                            arg[1] = int(arg[1])
                        except:    
                            self.send_warning.emit("La colonne "+ str(arg[1]) +" n'existe pas")
                    
                        try:
                            arg[2] = int(arg[2])
                        except:
                            self.send_warning.emit(arg[2] +" ne peut être utilisé comme indice de début de l'algorithme")
                        a = 0
                        for i in range(arg[1]-1,arg[2]):
                            a =  a  + (float(self.general_list[get_tab_pos(arg[0])][i])-self.mean(text))**2
                        return a/len(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])])
                        
                        
            else:
                self.send_warning.emit("La colonne "+ arg[0] +" n'existe pas")
                
        elif len(arg) == 4:
            if is_table_name(arg[0]):
                    if is_table_name(arg[1]):
                        if is_only_number(arg[0]):
                            if is_only_number(arg[1]):
                                a = 0
                                b = 0
                                try:
                                    arg[2] = int(arg[2])
                                except:
                                    self.send_warning.emit(arg[2] +" ne peut être utilisé comme indice de début de l'algorithme")
                                    
                                try:
                                    arg[3] = int(arg[3])
                                except:
                                    self.send_warning.emit(arg[3] +" ne peut être utilisé comme indice de début de l'algorithme")
                                    
                                a = 0
                                for i in range(arg[2]-1,arg[3]):
                                    
                                    a = a +float(self.general_list[get_tab_pos(arg[1])][i])*(float(self.general_list[get_tab_pos(arg[0])][i]) - self.mean(text))**2
                                                                                                           
                                return a/somme(self.general_list[get_tab_pos(arg[1])][arg[2]-1:arg[3]])
                            else:
                                self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[1])])[1])+
                                       " n'est pas un nombre")
                        else:
                            self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[0])])[1])+
                                       " n'est pas un nombre")
                    else:
                        self.send_warning.emit("La colonne "+ arg[1] +" n'existe pas")
            else:
                self.send_warning.emit("La colonne "+ arg[0] +" n'existe pas")
                    
                
            
    def mean(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        
        if len(arg) == 1:
            if type(is_only_number(self.general_list[get_tab_pos(arg[0])])) == bool:
                a = 0
                for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                    try:    
                        a = a + int(self.general_list[get_tab_pos(arg[0])][i])
                    except:
                        try:
                            a = a + float(self.general_list[get_tab_pos(arg[0])][i])
                        except:
                            a = a+0
                        
                return a/len(self.general_list[get_tab_pos(arg[0])])
            else:
                self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[0])])[1])+
                                       " n'est pas un nombre")
        elif len(arg) == 2:
            try:
                arg[1] = int(arg[1])
                if is_table_name(arg[0]):
                    if is_only_number(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])]):
                        a = 0
                        for i in range(arg[1]-1,len(self.general_list[get_tab_pos(arg[0])])):
                            try:    
                                a = a + int(self.general_list[get_tab_pos(arg[0])][i])
                            except:
                                try:
                                    a = a + float(self.general_list[get_tab_pos(arg[0])][i])
                                except:
                                    a = a+0
                                    
                                
                        return a/len(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])])
            
                    else:
                        self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[0])])[1])+
                                       " n'est pas un nombre")
                else:
                    self.send_warning.emit("La colonne "+ arg[0] +" n'existe pas")
                    
            except:
                if is_table_name(arg[0]):
                    if is_table_name(arg[1]):
                        if is_only_number(arg[0]):
                            if is_only_number(arg[1]):
                                a = 0
                                b = 0
                                for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                                    a = a + float(self.general_list[get_tab_pos(arg[0])][i])*float(self.general_list[get_tab_pos(arg[1])][i])
                                    b = b + float(self.general_list[get_tab_pos(arg[1])][i])
                                return a/b
                            else:
                                self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[1])])[1])+
                                       " n'est pas un nombre")
                        else:
                            self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[0])])[1])+
                                       " n'est pas un nombre")
                    else:
                        self.send_warning.emit("La colonne "+ arg[1] +" n'existe pas")
                else:
                    self.send_warning.emit("La colonne "+ arg[0] +" n'existe pas")
                    
        elif (len(arg)) == 3:
            if is_table_name(arg[0]):
                    if is_table_name(arg[1]):
                        if is_only_number(arg[0]):
                            if is_only_number(arg[1]):
                                a = 0
                                b = 0
                                try:
                                    arg[2] = int(arg[2])
                                except:
                                    self.send_warning.emit(arg[2] +" ne peut être utilisé comme indice de début de l'algorithme")
                                    
                                                 
                                for i in range(arg[2]-1,len(self.general_list[get_tab_pos(arg[0])])):
                                    a = a + float(self.general_list[get_tab_pos(arg[0])][i])*float(self.general_list[get_tab_pos(arg[1])][i])
                                    b = b + float(self.general_list[get_tab_pos(arg[1])][i])
                                return a/b
                            else:
                                self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[1])])[1])+
                                       " n'est pas un nombre")
                        else:
                            self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[0])])[1])+
                                       " n'est pas un nombre")
                    else:
                        try:
                            arg[1] = int(arg[1])
                            a = 0
                            try:
                                arg[2] = int(arg[2])
                            except:
                                self.send_warning.emit(arg[2] +" ne peut être utilisé comme indice de début de l'algorithme")
                                    
                            for i in range(arg[1]-1,arg[2]):
                                a = a + float(self.general_list[get_tab_pos(arg[0])][i])
                            return a/len(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])])
                        
                        except:    
                            self.send_warning.emit("La colonne "+ str(arg[1]) +" n'existe pas")
            else:
                self.send_warning.emit("La colonne "+ arg[0] +" n'existe pas")
                
        elif len(arg) == 4:
            if is_table_name(arg[0]):
                    if is_table_name(arg[1]):
                        if is_only_number(arg[0]):
                            if is_only_number(arg[1]):
                                a = 0
                                b = 0
                                try:
                                    arg[2] = int(arg[2])
                                except:
                                    self.send_warning.emit(arg[2] +" ne peut être utilisé comme indice de début de l'algorithme")
                                    
                                try:
                                    arg[3] = int(arg[3])
                                except:
                                    self.send_warning.emit(arg[3] +" ne peut être utilisé comme indice de début de l'algorithme")
                                    
                                                 
                                for i in range(arg[2]-1,arg[3]):
                                    a = a + float(self.general_list[get_tab_pos(arg[0])][i])*float(self.general_list[get_tab_pos(arg[1])][i])
                                    b = b + float(self.general_list[get_tab_pos(arg[1])][i])
                                return a/b
                            else:
                                self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[1])])[1])+
                                       " n'est pas un nombre")
                        else:
                            self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(self.general_list[get_tab_pos(arg[0])])[1])+
                                       " n'est pas un nombre")
                    else:
                        self.send_warning.emit("La colonne "+ arg[1] +" n'existe pas")
            else:
                self.send_warning.emit("La colonne "+ arg[0] +" n'existe pas")
                    
                                    
                                    
                    
            
    def sort(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        if len(arg) == 3:
            if is_table_name(arg[0]):
                if arg[1] == "mM" or arg[1] == "Mm":
                    if arg[2] == "float" or arg[2] == "str":
                        if arg[1] == "mM":
                            if arg[2] == "float":
                                try:
                                    self.general_list[get_tab_pos(arg[0])].sort(key = float)
                                except:
                                    self.send_warning.emit("La colonne "+arg[0]+" contient un caractère non numérique")
                                        
                            elif arg[2] == "str":
                                self.general_list[get_tab_pos(arg[0])].sort(key = str)
                        elif arg[1] == "Mm":
                             if arg[2] == "float":
                                 try:      
                                    self.general_list[get_tab_pos(arg[0])].sort(key = float,reverse = True)
                                 except:
                                    self.send_warning.emit("La colonne "+arg[0]+" contient un caractère non numérique")
                             elif arg[2] == "str":
                                self.general_list[get_tab_pos(arg[0])].sort(key = str,reverse = True)

                        return self.general_list
                    else:
                        self.send_warning.emit("Le troisième argument doit être soit float"
                                          "soit str")
                else:
                    self.send_warning.emit("Le troisième argument doit être soit </strong> mM </strong> "
                                          "soit Mm")
            else:
                self.send_warning.emit("La colonne "+str(arg[0])+" n'existe pas")
                
        elif len(arg) == 4:
            if is_table_name(arg[0]):
                if arg[1] == "mM" or arg[1] == "Mm":
                    if arg[2] == "float" or arg[2] == "str":
                        try:
                            arg[3] = int(arg[3])
                            print(" hhhhhhhhhhhhhhhhhhh",arg[3])
                        except:
                            self.send_warning.emit("Le quatrième argument  " +str(arg[3]) +"  ne peut être utilisé comme indice de début de l'algorithme."+
                                                   "Utiliser un nombre entier supérieur à 0")
                            
                        if arg[1] == "mM":
                            if arg[2] == "float":
                                try:
                                    a = self.general_list[get_tab_pos(arg[0])][0:arg[3]-1]
                                    b = self.general_list[get_tab_pos(arg[0])][arg[3]-1:len(self.general_list[get_tab_pos(arg[0])])]
                                    print((a,b))
                                    b.sort(key = float)
                                    self.general_list[get_tab_pos(arg[0])] = a+b
                                except:
                                    self.send_warning.emit("La colonne "+arg[0]+" contient un caractère non numérique")
                                return self.general_list
                                   
                            elif arg[2] == "str":
                                a = self.general_list[get_tab_pos(arg[0])][0:arg[3]-1]
                                b = self.general_list[get_tab_pos(arg[0])][arg[3]-1:len(self.general_list[get_tab_pos(arg[0])])]
                                b.sort(key = str)
                                self.general_list[get_tab_pos(arg[0])] = a+b
                                return self.general_list
                                    
                                    
                        elif arg[1] == "Mm":
                            print("ok")
                            if arg[2] == "float":
                                print("oki")
                                print(arg[3])
                                a = self.general_list[get_tab_pos(arg[0])][0:arg[3]-1]
                                b = self.general_list[get_tab_pos(arg[0])][arg[3]-1:len(self.general_list[get_tab_pos(arg[0])])]
                                try:   
                                    b.sort(key = float,reverse = True)
                                    self.general_list[get_tab_pos(arg[0])] = a+b
                                except:
                                    self.send_warning.emit("La colonne "+arg[0]+" contient un caractère non numérique")
                                    print("oka")
                                return self.general_list
                                
                            elif arg[2] == "str":
                                a = self.general_list[get_tab_pos(arg[0])][0:arg[3]-1]
                                b = self.general_list[get_tab_pos(arg[0])][arg[3]-1:len(self.general_list[get_tab_pos(arg[0])])]
                                b.sort(key = str,reverse = True)
                                self.general_list[get_tab_pos(arg[0])] = a+b
                                return self.general_list

                    else:
                        self.send_warning.emit("Le troisième argument doit être soit float "
                                          "soit str ")
                else:
                    self.send_warning.emit("Le troisième argument doit être soit mM "
                                          "soit Mm ")
            else:
                self.send_warning.emit("La colonne "+str(arg[0])+" n'existe pas")
            
        elif len(arg) == 5:
            if is_table_name(arg[0]):
                if arg[1] == "mM" or arg[1] == "Mm":
                    if arg[2] == "float" or arg[2] == "str":
                        try:
                            arg[3] = int(arg[3])
                            print(" hhhhhhhhhhhhhhhhhhh",arg[3])
                        except:
                            self.send_warning.emit("Le quatrième argument  " +str(arg[3]) +"  ne peut être utilisé comme indice de début de l'algorithme."+
                                                   " Utiliser un nombre entier supérieur à 0 ")
                        try:
                            arg[4] = int(arg[4])
                            print(" hhhhhhhhhhhhhhhhhhh 4",arg[4])
                        except:
                            self.send_warning.emit("Le ciquième argument  " +str(arg[4]) +"  ne peut être utilisé comme indice de début de l'algorithme."+
                                                   " Utiliser un nombre entier supérieur à 0 ")
                            
                        if arg[1] == "mM":
                            if arg[2] == "float":
                                try:
                                    a = self.general_list[get_tab_pos(arg[0])][0:arg[3]-1]
                                    b = self.general_list[get_tab_pos(arg[0])][arg[3]-1:arg[4]]
                                    c = self.general_list[get_tab_pos(arg[0])][arg[4]:len(self.general_list[get_tab_pos(arg[0])])]
                                    b.sort(key = float)
                                    self.general_list[get_tab_pos(arg[0])] = a+b+c
                                except:
                                    self.send_warning.emit("La colonne "+arg[0]+" contient un caractère non numérique")
                                return self.general_list
                                   
                            elif arg[2] == "str":
                                a = self.general_list[get_tab_pos(arg[0])][0:arg[3]-1]
                                b = self.general_list[get_tab_pos(arg[0])][arg[3]-1:arg[4]]
                                c = self.general_list[get_tab_pos(arg[0])][arg[4]:len(self.general_list[get_tab_pos(arg[0])])]
                                b.sort(key = str)
                                self.general_list[get_tab_pos(arg[0])] = a+b+c
                                return self.general_list
                                    
                                    
                        elif arg[1] == "Mm":
                            if arg[2] == "float":
                                print(arg[3])
                                
                                a = self.general_list[get_tab_pos(arg[0])][0:arg[3]-1]
                                b = self.general_list[get_tab_pos(arg[0])][arg[3]-1:arg[4]]
                                c = self.general_list[get_tab_pos(arg[0])][arg[4]:len(self.general_list[get_tab_pos(arg[0])])]
                                try:   
                                    b.sort(key = float,reverse = True)
                                    self.general_list[get_tab_pos(arg[0])] = a+b+c
                                except:
                                    self.send_warning.emit("La colonne "+arg[0]+" contient un caractère non numérique")
                                    print("oka")
                                return self.general_list
                                
                            elif arg[2] == "str":
                                a = self.general_list[get_tab_pos(arg[0])][0:arg[3]-1]
                                b = self.general_list[get_tab_pos(arg[0])][arg[3]-1:arg[4]]
                                c = self.general_list[get_tab_pos(arg[0])][arg[4]:len(self.general_list[get_tab_pos(arg[0])])]
                                b.sort(key = str,reverse = True)
                                self.general_list[get_tab_pos(arg[0])] = a+b+c
                                return self.general_list

                    else:
                        self.send_warning.emit("Le troisième argument doit être soit  float "
                                          "soit str")
                else:
                    self.send_warning.emit("Le troisième argument doit être soit mM "
                                          "soit Mm ")
            else:
                self.send_warning.emit("La colonne "+str(arg[0])+" n'existe pas")
                
    def delete(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        if len(arg) == 2:
            if arg[0] != "All":
                if is_table_name(arg[0]):
                    try:
                        arg[1] = int(arg[1])
                    except:
                        self.send_warning.emit("L'indice "+arg[1] +" n'est pas valide")
                    
                    del self.general_list[get_tab_pos(arg[0])][arg[1]-1]
                    self.general_list[get_tab_pos(arg[0])].append("")
                    return self.general_list
                else:
                    self.send_warning.emit("La colonne " +arg[0]+" n'existe pas")
                    
            elif arg[0] == "All":
                try:
                    arg[1] = int(arg[1])
                except:
                    self.send_warning.emit("L'indice "+arg[1] +" n'estp pas valide")
                    
                for i in range(len(self.general_list)):
                    del self.general_list[i][arg[1]-1]
                return self.general_list,1
            else:
                self.send_warning.emit(arg[0] +" n'est pas un argument valable. Vous devez mettre All ou le nom d'une colonne")
            
        elif len(arg) == 3:
            if arg[0] != "All":
                if is_table_name(arg[0]):
                    try:
                        arg[1] = int(arg[1])
                    except:
                        self.send_warning.emit("L'indice "+arg[1] +" n'estp pas valide")
                        
                    try:
                        arg[2] =  int(arg[2])
                    except:
                        self.send_warning.emit("L'indice "+arg[2] +" n'estp pas valide")
                    
                    x = len(self.general_list[get_tab_pos(arg[0])])
                    
                    a = self.general_list[get_tab_pos(arg[0])][0:arg[1]-1]
                    c = self.general_list[get_tab_pos(arg[0])][arg[2]:len(self.general_list[get_tab_pos(arg[0])])]
                    self.general_list[get_tab_pos(arg[0])] = a+c
                    
                    for i in range(x):
                        self.general_list[get_tab_pos(arg[0])].append("")
                        
                    return self.general_list
                
            elif arg[0] == "All":
                try:
                    arg[1] = int(arg[1])
                except:
                    self.send_warning.emit("L'indice "+arg[1] +" n'est  pas valide")
                        
                try:
                    arg[2] =  int(arg[2])
                except:
                    self.send_warning.emit("L'indice "+arg[2] +" n'est  pas valide")
                for i in range(len(self.general_list)):
                    a = self.general_list[i][0:arg[1]-1]
                    c = self.general_list[i][arg[2]:len(self.general_list[i])]
                    self.general_list[i] =  a+c
                    
                return self.general_list,(arg[2]-arg[1]+1)
            else:
                self.send_warning.emit(arg[0] +" n'est pas un argument valable. Vous devez mettre All ou le nom d'une colonne")
                
    def count(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments_sepa(arg,";")
        print(arg)
        print(len(arg))
        
        if len(arg) == 2:
            arg1 = arg[0]
            arg2 = arg[1]
            if self.is_crochet_syntax_correct(arg1):
                if self.is_crochet_syntax_correct(arg2):
                    arg1 = get_arguments(arg1[1:len(arg1)-1])
                    arg2 = get_arguments(arg2[1:len(arg2)-1])

                    if is_table_name(arg2[0]):
                        if is_only_tab_name(arg2):
                            compteur = 0
                            pos = get_element_poses(self.general_list[get_tab_pos(arg2[0])],arg1[0])
                            
                            if len(arg1) == len(arg2):
                                if len(arg1) == 1:
                                    return len(pos)
                                else:
                                    print("*",len(arg1))
                                    print("+",len(arg2))
                                    
                                    for i in range(len(pos)):
                                        # On prend une position pariculière
                                        state = True
                                        for u in range(len(arg1)):
                                            # On vérifie si les élément se trouvant à la position sont exact
                                            if arg1[u] != self.general_list[get_tab_pos(arg2[u])][pos[i]]:
                                                state = False
                                                break
                                        if state == True:
                                            # Si oui on incrémente
                                            compteur = compteur + 1
                                    return compteur
                            else:
                                self.send_warning.emit("Le nombre des premiers arguments doit être égale au nombre des second arguments")
                        else:
                            self.send_warning.emit("La colonne " +str(arg2[is_only_tab_name(text)[1]]) + " n'existe pas")
    
    def general_sort(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        if len(arg) == 3:
            if is_table_name(arg[0]):
                if arg[1] == "mM" or arg[1] == "Mm":
                    if arg[2] == "float" or arg[2] == "str":
                        if arg[1] == "mM":
                            if arg[2] == "float":
                                try:
                                   old = self.general_list[get_tab_pos(arg[0])]
                                   new = list(old)
                                   new.sort(key = float)
                                   key = generate_sorting_list(old,new)
                                   a = list()
                                   #print("77888",key) #(old,new)
                                   
                                   self.general_list[get_tab_pos(arg[0])] = list(new)
                                  
                                   if arg[0] != "Tab_A":
                                      
                                       for i in range(0,get_tab_pos(arg[0])):
                                           self.general_list[i] = sort_with_list(self.general_list[i],key)
                                        
                                       for i in range(get_tab_pos(arg[0])+1,len(self.general_list)):
                                           self.general_list[i] = sort_with_list(self.general_list[i],key)
                                           
                                   else:
                                       for i in range(1,len(self.general_list)):
                                           self.general_list[i] = sort_with_list(self.general_list[i],key)
                                           
                                          
                                   return self.general_list
                                    
                                    
                                except:
                                    print("no")
                                    self.send_warning.emit("La colonne "+arg[0]+" contient un caractère non numérique")
                                        
                            elif arg[2] == "str":
                                
                                old = self.general_list[get_tab_pos(arg[0])]
                                new = list(old)
                                new.sort(key = str)
                                key = generate_sorting_list(old,new)
                                a = list()
                                #print("77888",key) #(old,new)
                                   
                                self.general_list[get_tab_pos(arg[0])] = list(new)
                                  
                                if arg[0] != "Tab_A":
                                      
                                    for i in range(0,get_tab_pos(arg[0])):
                                        self.general_list[i] = sort_with_list(self.general_list[i],key)
                                        
                                    for i in range(get_tab_pos(arg[0])+1,len(self.general_list)):
                                        self.general_list[i] = sort_with_list(self.general_list[i],key)
                                           
                                else:
                                    for i in range(1,len(self.general_list)):
                                        self.general_list[i] = sort_with_list(self.general_list[i],key)
                                                      
                                return self.general_list
                                
                                
                        elif arg[1] == "Mm":
                             if arg[2] == "float":
                                 try:  
                                     
                                     
                                     old = self.general_list[get_tab_pos(arg[0])]
                                     new = list(old)
                                     new.sort(key = float,reverse = True)
                                     key = generate_sorting_list(old,new)
                                     a = list()
                                     #print("77888",key) #(old,new)
                                   
                                     self.general_list[get_tab_pos(arg[0])] = list(new)
                                  
                                     if arg[0] != "Tab_A":
                                         
                             
                                         for i in range(0,get_tab_pos(arg[0])):
                                             self.general_list[i] = sort_with_list(self.general_list[i],key)
                                        
                                         for i in range(get_tab_pos(arg[0])+1,len(self.general_list)):
                                             self.general_list[i] = sort_with_list(self.general_list[i],key)
                                           
                                     else:
                                         for i in range(1,len(self.general_list)):
                                             self.general_list[i] = sort_with_list(self.general_list[i],key)
                                                      
                                     return self.general_list
                                     
                                    
                                 except:
                                    self.send_warning.emit("La colonne "+arg[0]+" contient un caractère non numérique")
                                
                             elif arg[2] == "str":
                                     old = self.general_list[get_tab_pos(arg[0])]
                                     new = list(old)
                                     new.sort(key = str,reverse = True)
                                     key = generate_sorting_list(old,new)
                                     a = list()
                                     #print("77888",key) #(old,new)
                                   
                                     self.general_list[get_tab_pos(arg[0])] = list(new)
                                  
                                     if arg[0] != "Tab_A":
                                         
                             
                                         for i in range(0,get_tab_pos(arg[0])):
                                             self.general_list[i] = sort_with_list(self.general_list[i],key)
                                        
                                         for i in range(get_tab_pos(arg[0])+1,len(self.general_list)):
                                             self.general_list[i] = sort_with_list(self.general_list[i],key)
                                           
                                     else:
                                         for i in range(1,len(self.general_list)):
                                             self.general_list[i] = sort_with_list(self.general_list[i],key)
                                                      
                                     return self.general_list
                                 
                                
                    else:
                        self.send_warning.emit("Le troisième argument doit être soit float "
                                          "soit str ")
                else:
                    self.send_warning.emit("Le quatrième argument doit être soit mM "
                                          "soit Mm ")
            else:
                self.send_warning.emit("La colonne "+str(arg[0])+" n'existe pas")
             
        elif len(arg) == 4:
            if is_table_name(arg[0]):
                try:
                    # Pour faire coincider
                    arg[3] = int(arg[3])-1
                except:
                    
                    self.send_warning.emit("Le quatrième argument doit être un nombre entier positif")
                l = len(self.general_list[get_tab_pos(arg[0])])
                if arg[1] == "mM" or arg[1] == "Mm":
                    if arg[2] == "float" or arg[2] == "str":
                        if arg[1] == "mM":
                            if arg[2] == "float":
                                try:
                                   
                                   old = self.general_list[get_tab_pos(arg[0])][arg[3]:l]
                                   new = list(old)
                                   new.sort(key = float)
                                   key = generate_sorting_list(old,new)
                                   a = list()
                                   #print("77888",key) #(old,new)
                                   
                                   self.general_list[get_tab_pos(arg[0])][arg[3]:l] = list(new)
                                  
                                   if arg[0] != "Tab_A":
                                      
                                       for i in range(0,get_tab_pos(arg[0])):
                                           self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                        
                                       for i in range(get_tab_pos(arg[0])+1,len(self.general_list)):
                                           self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                           
                                   else:
                                       for i in range(1,len(self.general_list)):
                                           self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                           
                                          
                                   return self.general_list
                                    
                                    
                                except:
                                    print("no")
                                    self.send_warning.emit("La colonne "+arg[0]+" contient un caractère non numérique")
                                        
                            elif arg[2] == "str":
                                
                                old = self.general_list[get_tab_pos(arg[0])][arg[3]:l]
                                new = list(old)
                                new.sort(key = str)
                                key = generate_sorting_list(old,new)
                                a = list()
                                #print("77888",key) #(old,new)
                                   
                                self.general_list[get_tab_pos(arg[0])][arg[3]:l] = list(new)
                                  
                                if arg[0] != "Tab_A":
                                      
                                    for i in range(0,get_tab_pos(arg[0])):
                                        self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                        
                                    for i in range(get_tab_pos(arg[0])+1,len(self.general_list)):
                                        self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                           
                                else:
                                    for i in range(1,len(self.general_list)):
                                        self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                                      
                                return self.general_list
                                
                                
                        elif arg[1] == "Mm":
                             if arg[2] == "float":
                                 try:  
                                     
                                     
                                     old = self.general_list[get_tab_pos(arg[0])][arg[3]:l]
                                     new = list(old)
                                     new.sort(key = float,reverse = True)
                                     key = generate_sorting_list(old,new)
                                     a = list()
                                     #print("77888",key) #(old,new)
                                   
                                     self.general_list[get_tab_pos(arg[0])][arg[3]:l] = list(new)
                                  
                                     if arg[0] != "Tab_A":
                                         
                             
                                         for i in range(0,get_tab_pos(arg[0])):
                                             self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                        
                                         for i in range(get_tab_pos(arg[0])+1,len(self.general_list)):
                                             self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                           
                                     else:
                                         for i in range(1,len(self.general_list)):
                                             self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                                      
                                     return self.general_list
                                     
                                    
                                 except:
                                    self.send_warning.emit("La colonne "+arg[0]+" contient un caractère non numérique")
                                
                             elif arg[2] == "str":
                                     old = self.general_list[get_tab_pos(arg[0])][arg[3]:l]
                                     new = list(old)
                                     new.sort(key = str,reverse = True)
                                     key = generate_sorting_list(old,new)
                                     a = list()
                                     #print("77888",key) #(old,new)
                                   
                                     self.general_list[get_tab_pos(arg[0])][arg[3]:l] = list(new)
                                  
                                     if arg[0] != "Tab_A":
                                         
                             
                                         for i in range(0,get_tab_pos(arg[0])):
                                             self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                        
                                         for i in range(get_tab_pos(arg[0])+1,len(self.general_list)):
                                             self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                           
                                     else:
                                         for i in range(1,len(self.general_list)):
                                             self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                                      
                                     return self.general_list
                                 
                                
                    else:
                        self.send_warning.emit("Le troisième argument doit être soit float "
                                          "soit str ")
                else:
                    self.send_warning.emit("Le troisième argument doit être soit mM "
                                          "soit Mm ")
            else:
                self.send_warning.emit("La colonne "+str(arg[0])+" n'existe pas")
                
        elif len(arg) == 5:
            if is_table_name(arg[0]):
                try:
                    arg[3] = int(arg[3])-1
                except:
                    
                    self.send_warning.emit("Le quatrième argument doit être un nombre entier positif")
                    
                try:
                    arg[4] = int(arg[4])
                except:
                    self.send_warning.emit("Le cinquième argument doit être un nombre entier positif")
                    
                l = arg[4]
                if arg[1] == "mM" or arg[1] == "Mm":
                    if arg[2] == "float" or arg[2] == "str":
                        if arg[1] == "mM":
                            if arg[2] == "float":
                                try:
                                   
                                   old = self.general_list[get_tab_pos(arg[0])][arg[3]:l]
                                   new = list(old)
                                   new.sort(key = float)
                                   key = generate_sorting_list(old,new)
                                   a = list()
                                   #print("77888",key) #(old,new)
                                   
                                   self.general_list[get_tab_pos(arg[0])][arg[3]:l] = list(new)
                                  
                                   if arg[0] != "Tab_A":
                                      
                                       for i in range(0,get_tab_pos(arg[0])):
                                           self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                        
                                       for i in range(get_tab_pos(arg[0])+1,len(self.general_list)):
                                           self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                           
                                   else:
                                       for i in range(1,len(self.general_list)):
                                           self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                           
                                          
                                   return self.general_list
                                    
                                    
                                except:
                                    print("no")
                                    self.send_warning.emit("La colonne "+arg[0]+" contient un caractère non numérique")
                                        
                            elif arg[2] == "str":
                                
                                old = self.general_list[get_tab_pos(arg[0])][arg[3]:l]
                                new = list(old)
                                new.sort(key = str)
                                key = generate_sorting_list(old,new)
                                a = list()
                                #print("77888",key) #(old,new)
                                   
                                self.general_list[get_tab_pos(arg[0])][arg[3]:l] = list(new)
                                  
                                if arg[0] != "Tab_A":
                                      
                                    for i in range(0,get_tab_pos(arg[0])):
                                        self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                        
                                    for i in range(get_tab_pos(arg[0])+1,len(self.general_list)):
                                        self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                           
                                else:
                                    for i in range(1,len(self.general_list)):
                                        self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                                      
                                return self.general_list
                                
                                
                        elif arg[1] == "Mm":
                             if arg[2] == "float":
                                 try:  
                                     
                                     
                                     old = self.general_list[get_tab_pos(arg[0])][arg[3]:l]
                                     new = list(old)
                                     new.sort(key = float,reverse = True)
                                     key = generate_sorting_list(old,new)
                                     a = list()
                                     #print("77888",key) #(old,new)
                                   
                                     self.general_list[get_tab_pos(arg[0])][arg[3]:l] = list(new)
                                  
                                     if arg[0] != "Tab_A":
                                         
                             
                                         for i in range(0,get_tab_pos(arg[0])):
                                             self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                        
                                         for i in range(get_tab_pos(arg[0])+1,len(self.general_list)):
                                             self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                           
                                     else:
                                         for i in range(1,len(self.general_list)):
                                             self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                                      
                                     return self.general_list
                                     
                                    
                                 except:
                                    self.send_warning.emit("La colonne "+arg[0]+" contient un caractère non numérique")
                                
                             elif arg[2] == "str":
                                     old = self.general_list[get_tab_pos(arg[0])][arg[3]:l]
                                     new = list(old)
                                     new.sort(key = str,reverse = True)
                                     key = generate_sorting_list(old,new)
                                     a = list()
                                     #print("77888",key) #(old,new)
                                   
                                     self.general_list[get_tab_pos(arg[0])][arg[3]:l] = list(new)
                                  
                                     if arg[0] != "Tab_A":
                                         
                             
                                         for i in range(0,get_tab_pos(arg[0])):
                                             self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                        
                                         for i in range(get_tab_pos(arg[0])+1,len(self.general_list)):
                                             self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                           
                                     else:
                                         for i in range(1,len(self.general_list)):
                                             self.general_list[i][arg[3]:l] = sort_with_list(self.general_list[i][arg[3]:l],key)
                                                      
                                     return self.general_list
                                 
                                
                    else:
                        self.send_warning.emit("Le troisième argument doit être soit float "
                                          "soit str ")
                else:
                    self.send_warning.emit("Le troisième argument doit être soit mM  "
                                          "soit Mm ")
            else:
                self.send_warning.emit("La colonne "+str(arg[0])+" n'existe pas")
                
                
                
            
        
                            
                            
    def somme(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        if len(arg) == 1:
            if is_only_number(arg[0]):
                return somme(self.general_list[get_tab_pos(arg[0])])
            else:
                self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
        elif len(arg) == 2:
            if is_only_number(arg[0]):
                try:
                    arg[1] = int(arg[1])
                except:
                    self.send_warning.emit(str(arg[1])+ "ne peut être utilisé comme indice de début de l'algorithme")
                return somme(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])])
            else:
                self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
                
        elif len(arg) == 3:
            if is_only_number(arg[0]):
                try:
                    arg[1] = int(arg[1])
                except:
                    self.send_warning.emit(str(arg[1])+ " ne peut être utilisé comme indice de début de l'algorithme")
                    
                    
                try:
                    arg[2] = int(arg[2])
                except:
                    self.send_warning.emit(str(arg[2])+ " ne peut être utilisé comme indice de début de l'algorithme")
                    
                    
                return somme(self.general_list[get_tab_pos(arg[0])][arg[1]-1:arg[2]])
            else:
                self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + "n'est pas un nombre")
    
    def sub(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        
        if len(arg) == 3:
            if is_table_name(arg[0]):
                if arg[2] == "str":
                    for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                        try:
                            a = str_to_list(self.general_list[get_tab_pos(arg[0])][i])
                            a.remove(arg[1])
                            
                            self.general_list[get_tab_pos(arg[0])][i] =list_to_str(a)
                        except:
                            continue
                        
                    return self.general_list
                        
                elif arg[2] == "float":
                    if is_only_number(self.general_list[get_tab_pos(arg[0])]):
                        
                        try:
                            arg[1] = int(arg[1])
                        except:
                            
                            try:
                                arg[1] = float(arg[1])
                            except:
                                self.send_warning.emit(str(arg[1]) +" n'est pas un nombre")
                        
                        for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                            if self.general_list[get_tab_pos(arg[0])][i] != "":
                                
                                try:
                                    self.general_list[get_tab_pos(arg[0])][i] = int(str(self.general_list[get_tab_pos(arg[0])][i]))-arg[1]
                                except:

                                    self.general_list[get_tab_pos(arg[0])][i] = float(str(self.general_list[get_tab_pos(arg[0])][i]))-arg[1]
                            
                        return self.general_list
                    
        elif len(arg) == 4:
            if is_table_name(arg[0]):
                try:
                    arg[3] = int(arg[3])
                    
                except:
                    self.send_warning.emit(arg[3] +" ne peut pas servir d'indice de début de l'algorithme")
                    
                if arg[2] == "str":
                    for i in range(arg[3]-1,arg[4]):
                        try:
                            a = str_to_list(self.general_list[get_tab_pos(arg[0])][i])
                            a.remove(arg[1])
                            
                            self.general_list[get_tab_pos(arg[0])][i] =list_to_str(a)
                        except:
                            continue
                    return self.general_list
                        
                elif arg[2] == "float":
                    try:
                        arg[1] = int(arg[1])
                    except:
                        try:
                            arg[1] = float(arg[1])
                        except:
                            self.send_warning.emit(str(arg[1]) +" n'est pas un nombre")
                    
                    if is_only_number(self.general_list[get_tab_pos(arg[0])]):
                        
                        for i in range(arg[3]-1,len(self.general_list[get_tab_pos(arg[0])])):
                            if self.general_list[get_tab_pos(arg[0])][i] != "":
                                
                                try:
                                    self.general_list[get_tab_pos(arg[0])][i] = int(str(self.general_list[get_tab_pos(arg[0])][i]))-arg[1]
                                except:

                                    self.general_list[get_tab_pos(arg[0])][i] = float(str(self.general_list[get_tab_pos(arg[0])][i]))-arg[1]
                            
                        return self.general_list
                            
            
                    else:
                        self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
        elif len(arg) == 5:
            if is_table_name(arg[0]):
                try:
                    arg[3] = int(arg[3])
                    
                except:
                    self.send_warning.emit(arg[3] +" ne peut pas servir d'indice de début de l'algorithme")
                    
                
                try:
                    arg[4] = int(arg[4])
                    
                except:
                    self.send_warning.emit(arg[4] +" ne peut pas servir d'indice de début de l'algorithme")
                    
                if arg[2] == "str":
                    for i in range(arg[3]-1,arg[4]):
                       try:
                            a = str_to_list(self.general_list[get_tab_pos(arg[0])][i])
                            a.remove(arg[1])
                            
                            self.general_list[get_tab_pos(arg[0])][i] = list_to_str(a)
                       except:
                           continue
                        
                    return self.general_list
                        
                elif arg[2] == "float":
                    try:
                        arg[1] = int(arg[1])
                    except:
                        try:
                            arg[1] = float(arg[1])
                        except:
                            self.send_warning.emit(str(arg[1]) +" n'est pas un nombre")
                    
                    
                    if is_only_number(self.general_list[get_tab_pos(arg[0])]):
                        for i in range(arg[3]-1,arg[4]):
                            if self.general_list[get_tab_pos(arg[0])][i] != "":
                                
                                try:
                                    self.general_list[get_tab_pos(arg[0])][i] = int(str(self.general_list[get_tab_pos(arg[0])][i]))-arg[1]
                                except:

                                    self.general_list[get_tab_pos(arg[0])][i] = float(str(self.general_list[get_tab_pos(arg[0])][i]))-arg[1]
                            
                        return self.general_list
                            
            
                    else:
                        self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
    
    def add(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        
        if len(arg) == 3:
            if is_table_name(arg[0]):
                if arg[2] == "str":
                    for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                        self.general_list[get_tab_pos(arg[0])][i] = str(self.general_list[get_tab_pos(arg[0])][i])+ str(arg[1])
                        
                    return self.general_list
                        
                elif arg[2] == "float":
                    try:
                        arg[1] = int(arg[1])
                    except:
                        try:
                            arg[1] = float(arg[1])
                        except:
                            self.send_warning.emit(arg[1] +" n'est pas un nombre")
                        
                    if is_only_number(self.general_list[get_tab_pos(arg[0])]):
                        for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                            if self.general_list[get_tab_pos(arg[0])][i] != "":
                                
                                try:    
                                    self.general_list[get_tab_pos(arg[0])][i] = int(str(self.general_list[get_tab_pos(arg[0])][i]))+(arg[1])
                                except:
                                    self.general_list[get_tab_pos(arg[0])][i] = float(str(self.general_list[get_tab_pos(arg[0])][i]))+(arg[1])
                                 
                        return self.general_list
                    
        elif len(arg) == 4:
            if is_table_name(arg[0]):
                try:
                    arg[3] = int(arg[3])
                    
                except:
                    self.send_warning.emit(arg[3] +" ne peut pas servir d'indice de début de l'algorithme")
                    
                if arg[2] == "str":
                    for i in range(arg[3]-1,len(self.general_list[get_tab_pos(arg[0])])):
                        self.general_list[get_tab_pos(arg[0])][i] = str(self.general_list[get_tab_pos(arg[0])][i])+ str(arg[1])
                        
                    return self.general_list
                        
                elif arg[2] == "float":
                    try:
                        arg[1] = int(arg[1])
                    except:
                        try:
                            arg[1] = float(arg[1])
                        except:
                            self.send_warning.emit(arg[1] +" n'est pas un nombre")
                            
                    if is_only_number(self.general_list[get_tab_pos(arg[0])]):
                        for i in range(arg[3]-1,len(self.general_list[get_tab_pos(arg[0])])):
                            if self.general_list[get_tab_pos(arg[0])][i] != "":
                                try:
                                    self.general_list[get_tab_pos(arg[0])][i] = int(str(self.general_list[get_tab_pos(arg[0])][i]))+(arg[1])
                                except:
                                    self.general_list[get_tab_pos(arg[0])][i] = float(str(self.general_list[get_tab_pos(arg[0])][i]))+(arg[1])
                               
                        return self.general_list
                            
            
                    else:
                        self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
        elif len(arg) == 5:
            if is_table_name(arg[0]):
                try:
                    arg[3] = int(arg[3])
                    
                except:
                    self.send_warning.emit(arg[3] +" ne peut pas servir d'indice de début de l'algorithme")
                    
                
                try:
                    arg[4] = int(arg[4])
                    
                except:
                    self.send_warning.emit(arg[4] +" ne peut pas servir d'indice de début de l'algorithme")
                    
                if arg[2] == "str":
                    for i in range(arg[3]-1,arg[4]):
                        self.general_list[get_tab_pos(arg[0])][i] = str(self.general_list[get_tab_pos(arg[0])][i])+ str(arg[1])
                        
                    return self.general_list
                        
                elif arg[2] == "float":
                    try:
                        arg[1] = int(arg[1])
                    except:
                        try:
                            arg[1] = float(arg[1])
                        except:
                            self.send_warning.emit(arg[1] +" n'est pas un nombre")
                            
                            
                    if is_only_number(self.general_list[get_tab_pos(arg[0])]):
                        for i in range(arg[3]-1,arg[4]):
                            if self.general_list[get_tab_pos(arg[0])][i] != "":
                                
                                try:
                                    self.general_list[get_tab_pos(arg[0])][i] = int(str(self.general_list[get_tab_pos(arg[0])][i]))+(arg[1])
                                except:
                                    self.general_list[get_tab_pos(arg[0])][i] = float(str(self.general_list[get_tab_pos(arg[0])][i]))+(arg[1])
                             
                        return self.general_list
                            
            
                    else:
                        self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
    
    def div(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        
        if len(arg) == 3:
            if is_table_name(arg[0]):
                # On transforme arg[1] en int ou en float
                try:
                    arg[1] = int(arg[1])
                except:
                    try:
                        arg[1] = float(arg[1])
                    except:
                        self.send_warning.emit(arg[1] +" n'est pas un nombre")
                        
                if arg[2] == "float":
                    if is_only_number(self.general_list[get_tab_pos(arg[0])]):
                        for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                            if self.general_list[get_tab_pos(arg[0])][i]  != "":
                                try:    
                                    self.general_list[get_tab_pos(arg[0])][i] = int(str(self.general_list[get_tab_pos(arg[0])][i])) / (arg[1])
                                except:
                                    self.general_list[get_tab_pos(arg[0])][i] = float(str(self.general_list[get_tab_pos(arg[0])][i])) / (arg[1])
                            
                        return self.general_list
                    
        elif len(arg) == 4:
            if is_table_name(arg[0]):
                try:
                    arg[3] = int(arg[3])
                    
                except:
                    self.send_warning.emit(arg[3] +" ne peut pas servir d'indice de début de l'algorithme")
                    
                    
                # On transforme arg[1] en int ou en float
                try:
                    arg[1] = int(arg[1])
                except:
                    try:
                        arg[1] = float(arg[1])
                    except:
                        self.send_warning.emit(arg[1] +" n'est pas un nombre")
                    
                if arg[2] == "float":
                    if is_only_number(self.general_list[get_tab_pos(arg[0])]):
                        for i in range(arg[3]-1,len(self.general_list[get_tab_pos(arg[0])])):
                            if self.general_list[get_tab_pos(arg[0])][i] != "":
                                try:    
                                    self.general_list[get_tab_pos(arg[0])][i] = int(str(self.general_list[get_tab_pos(arg[0])][i])) / (arg[1])
                                except:
                                    self.general_list[get_tab_pos(arg[0])][i] = float(str(self.general_list[get_tab_pos(arg[0])][i])) / (arg[1])
                             
                        return self.general_list
                            
            
                    else:
                        self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
        elif len(arg) == 5:
            if is_table_name(arg[0]):
                try:
                    arg[3] = int(arg[3])
                    
                except:
                    self.send_warning.emit(arg[3] +" ne peut pas servir d'indice de début de l'algorithme")
                    
                
                try:
                    arg[4] = int(arg[4])
                    
                except:
                    self.send_warning.emit(arg[4] +" ne peut pas servir d'indice de début de l'algorithme")
                    
                    
                # On transforme arg[1] en int ou en float
                try:
                    arg[1] = int(arg[1])
                except:
                    try:
                        arg[1] = float(arg[1])
                    except:
                        self.send_warning.emit(arg[1] +" n'est pas un nombre")
                    
                if arg[2] == "float":
                    if is_only_number(self.general_list[get_tab_pos(arg[0])]):
                        for i in range(arg[3]-1,arg[4]):
                            if self.general_list[get_tab_pos(arg[0])][i]:
                                try:    
                                    self.general_list[get_tab_pos(arg[0])][i] = int(str(self.general_list[get_tab_pos(arg[0])][i])) / (arg[1])
                                except:
                                    self.general_list[get_tab_pos(arg[0])][i] = float(str(self.general_list[get_tab_pos(arg[0])][i])) / (arg[1])
                             
                        return self.general_list
                            
            
                    else:
                        self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
    def mul(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        
        if len(arg) == 3:
            if is_table_name(arg[0]):
                if arg[2] == "str":
                    try:
                        arg[1] = int(arg[1])
                    
                    except:
                        self.send_warning.emit(arg[1] +" n'est pas un nombre entier positif")
                        
                    for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                        self.general_list[get_tab_pos(arg[0])][i] = str(self.general_list[get_tab_pos(arg[0])][i])* int(arg[1])
                        
                    return self.general_list
                        
                elif arg[2] == "float":
                    # On transforme le multiplicateur en int ou en float
                    try:
                        arg[1] = int(arg[1])
                    
                    except:
                        try:
                           arg[1] = float(arg[1]) 
                        except:
                             self.send_warning.emit(arg[1] +" n'est pas un nombre")
                    
                    if is_only_number(self.general_list[get_tab_pos(arg[0])]):
                        for i in range(len(self.general_list[get_tab_pos(arg[0])])):
                            if self.general_list[get_tab_pos(arg[0])][i] != "":
                                try:
                                    self.general_list[get_tab_pos(arg[0])][i] = int(str(self.general_list[get_tab_pos(arg[0])][i]))*(arg[1])
                                except:
                                    self.general_list[get_tab_pos(arg[0])][i] = float(str(self.general_list[get_tab_pos(arg[0])][i]))*(arg[1])
                                
                            
                        return self.general_list
                    
        elif len(arg) == 4:
            if is_table_name(arg[0]):
                try:
                    arg[3] = int(arg[3])
                    
                except:
                    self.send_warning.emit(arg[3] +" ne peut pas servir d'indice de début de l'algorithme")
                    
                if arg[2] == "str":
                    try:
                        arg[1] = int(arg[1])
                    
                    except:
                        self.send_warning.emit(arg[1] +" n'est pas un nombre entier positif")
                        
                    for i in range(arg[1]-1,len(self.general_list[get_tab_pos(arg[0])])):
                        self.general_list[get_tab_pos(arg[0])][i] = str(self.general_list[get_tab_pos(arg[0])][i])* int(arg[1])
                        
                    return self.general_list
                        
                elif arg[2] == "float":
                    # On transforme le multiplicateur en int ou en float
                    try:
                        arg[1] = int(arg[1])
                    
                    except:
                        try:
                           arg[1] = float(arg[1]) 
                        except:
                             self.send_warning.emit(arg[1] +" n'est pas un nombre")
                             
                    if is_only_number(self.general_list[get_tab_pos(arg[0])]):
                        for i in range(arg[3]-1,len(self.general_list[get_tab_pos(arg[0])])):
                            if self.general_list[get_tab_pos(arg[0])][i] !=  "":    
                                try:
                                    self.general_list[get_tab_pos(arg[0])][i] = int(str(self.general_list[get_tab_pos(arg[0])][i]))*(arg[1])
                                except:
                                    self.general_list[get_tab_pos(arg[0])][i] = float(str(self.general_list[get_tab_pos(arg[0])][i]))*(arg[1])
                                
                        return self.general_list
                            
            
                    else:
                        self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
        elif len(arg) == 5:
            if is_table_name(arg[0]):
                try:
                    arg[3] = int(arg[3])
                    
                except:
                    self.send_warning.emit(arg[3] +" ne peut pas servir d'indice de début de l'algorithme")
                    
                
                try:
                    arg[4] = int(arg[4])
                    
                except:
                    self.send_warning.emit(arg[4] +" ne peut pas servir d'indice de début de l'algorithme")
                    
                if arg[2] == "str":
                    try:
                        arg[1] = int(arg[1])
                    
                    except:
                        self.send_warning.emit(arg[1] +" n'est pas un nombre entier positif")
                        
                    for i in range(arg[1]-1,arg[4]):
                        self.general_list[get_tab_pos(arg[0])][i] = str(self.general_list[get_tab_pos(arg[0])][i])* int(arg[1])
                        
                    return self.general_list
                        
                elif arg[2] == "float":
                    # On transforme le multiplicateur en int ou en float
                    try:
                        arg[1] = int(arg[1])
                    
                    except:
                        try:
                           arg[1] = float(arg[1]) 
                        except:
                             self.send_warning.emit(arg[1] +" n'est pas un nombre")
                             
                    if is_only_number(self.general_list[get_tab_pos(arg[0])]):
                        for i in range(arg[3]-1,arg[4]):
                            if self.general_list[get_tab_pos(arg[0])][i] != "":
                                try:
                                    self.general_list[get_tab_pos(arg[0])][i] = int(str(self.general_list[get_tab_pos(arg[0])][i]))*(arg[1])
                                except:
                                    self.general_list[get_tab_pos(arg[0])][i] = float(str(self.general_list[get_tab_pos(arg[0])][i]))*(arg[1])
                                 
                        return self.general_list
                            
            
                    else:
                        self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
        
    def produit(self,text):
        fonc,arg = get_fonc_and_arg(text)
        arg = get_arguments(arg)
        print(arg)
        if len(arg) == 1:
            if is_only_number(arg[0]):
                return produit_(self.general_list[get_tab_pos(arg[0])])
            else:
                self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
        elif len(arg) == 2:
            if is_only_number(arg[0]):
                try:
                    arg[1] = int(arg[1])
                except:
                    self.send_warning.emit(str(arg[1])+ " ne peut être utilisé comme indice de début de l'algorithme")
                return produit_(self.general_list[get_tab_pos(arg[0])][arg[1]-1:len(self.general_list[get_tab_pos(arg[0])])])
            else:
                self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
                
        elif len(arg) == 3:
            if is_only_number(arg[0]):
                try:
                    arg[1] = int(arg[1])
                except:
                    self.send_warning.emit(str(arg[1])+ " ne peut être utilisé comme indice de début de l'algorithme")
                    
                    
                try:
                    arg[2] = int(arg[2])
                except:
                    self.send_warning.emit(str(arg[2])+ " ne peut être utilisé comme indice de début de l'algorithme")
                    
                    
                return produit_(self.general_list[get_tab_pos(arg[0])][arg[1]-1:arg[2]])
            else:
                self.send_warning.emit("L'élément se trouvant à la case "+
                                       str(is_only_number(arg[0])[1]) + " n'est pas un nombre")
        
         
"""    
a = [14,2,4,7,7,8]
b = [14,4,1,5,8,15]
d = ["ELVIS","CLEMENT","PIERRE","PAUL","ELIE","Justine"]
c = [a,b,d]
scri = ScriptClass(c)
print(c)
print(scri.to_fonction(("general_sort(Tab_A,mM,float)")))
 """     
#print(translate("Jesus est Roi","en"))