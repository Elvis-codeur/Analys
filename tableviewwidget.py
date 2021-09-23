# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:47:00 2020

@author: elvis
"""

### Qt ###
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import sqlite3
import io

###    ###

import pandas as pd
import numpy as np

### Mes propres fichiers ###
from mytablemodel import *
from mytableview import *
from algorithms import *
from editor.mainwindow import *
import State.global_state as global_state
from Files import open

####                     ###

# Module personnel

import locals.datasfile 
#

class TableViewWidget(QWidget):
    send_data = pyqtSignal(list)
    send_errormessage = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
        self.rowCount = 10
        self.columnCount = 26
        
        self.generalList = list()
        
        self.listA = list()
        self.listB = list()
        self.listC = list()
        self.listD = list()
        self.listE = list()
        self.listF = list()
        self.listG = list()
        self.listH = list()
        self.listI = list()
        self.listJ = list()
        self.listK = list()
        self.listL = list()
        self.listM = list()
        self.listN = list()
        self.listO = list()
        self.listP = list()
        self.listQ = list()
        self.listR = list()
        self.listS = list()
        self.listT = list()
        self.listU = list()
        self.listV = list()
        self.listW = list()
        self.listX = list()
        self.listY = list()
        self.listZ = list()
        
        # Pour entrer les scripts
        self.scriptLineEdit = QLineEdit()
        self.scriptLayout = QFormLayout()
        self.resultLineEdit = QLineEdit()
        self.resultLineLayout = QFormLayout()
        
        self.layoutPrincipale = QVBoxLayout()
        
        self.tableModel = MyTableModel()
        self.tableView = MyTableView()
        
        
        # Pour les codes
        self.codeWidget = EditorMainWindow()
        font = QFont("Consolas")
        font.setPixelSize(20)
        # Pour la lecture des csv
        self.w = QWidget()
        
        self.scriptLineEdit.setFont(font)
        self.resultLineEdit.setFont(font)
        self.scriptLayout.addRow("Script",self.scriptLineEdit)
        self.resultLineLayout.addRow("Résultat",self.resultLineEdit)
        
        self.layoutPrincipale.addLayout(self.scriptLayout)
        self.layoutPrincipale.addWidget(self.tableView)
        self.layoutPrincipale.addLayout(self.resultLineLayout)
        self.setLayout(self.layoutPrincipale)
        
        self.tableView.setModel(self.tableModel)
        self.init_connection()
        
        
        # Pour l'export vers une base de donnée existante
        self.data_base_table_name_receiver = QLineEdit()
        self.data_base_table_name_widget = QDialog(self)
        self.data_base_table_name_widget.setWindowTitle("Donnez le nom de votre TABLE")
        self.data_base_table_name_button = QPushButton("Ok")
        
        self.data_base_table_name_receiver2 = QLineEdit()
        self.data_base_table_name_widget2 = QDialog(self)
        self.data_base_table_name_widget2.setWindowTitle("Donnez le nom de votre TABLE")
        self.data_base_table_name_button2 = QPushButton("Ok")
        
        l = QVBoxLayout()
        l.addWidget(self.data_base_table_name_receiver)
        l.addWidget(self.data_base_table_name_button)
        self.data_base_table_name_widget.setLayout(l)
        
        l2 = QVBoxLayout()
        l2.addWidget(self.data_base_table_name_receiver2)
        l2.addWidget(self.data_base_table_name_button2)
        self.data_base_table_name_widget2.setLayout(l2)
        
        l = QFormLayout()
        self.line_edit = QLineEdit()
        l.addRow("Choisissez un séparateur : ",self.line_edit)
        f_button = QPushButton("Ok")
        l.addRow("Terminer",f_button)
            
        f_button.clicked.connect(self.other_open)
                
        self.w.setLayout(l)
        
    def get_table_name(self):
        self.data_base_table_name_widget.show()
        self.data_base_table_name_button.clicked.connect(self.data_base_table_name_widget.hide)
        self.data_base_table_name_button.clicked.connect(self.existing_base_export)
    
    def get_table_name2(self):
        self.data_base_table_name_widget2.show()
        self.data_base_table_name_button2.clicked.connect(self.data_base_table_name_widget2.hide)
        self.data_base_table_name_button2.clicked.connect(self.new_base_export)
    
    def new_base_export(self):
        if 1:
            
            f = QFileDialog()
            name = f.getSaveFileName(self,"Enrégister dans une nouvelle base de donnée",str(),"")
            if len(name) !=0:
                print(name)
                conn = sqlite3.connect(name[0])
                cur = conn.cursor()
                text_to_execute = "CREATE TABLE IF NOT EXISTS " +self.data_base_table_name_receiver2.text()+\
                "(id INTEGER PRIMARY\n"+"KEY AUTOINCREMENT UNIQUE,\n"
            
                # On prépare les données pour le travail
                self.clear_list()
                self.clear_general_list()
                self.add_list_to_general_list()
                self.table_view_to_list()
                
                for i in range(len(self.generalList)):
                    if self.is_list_empty(self.generalList[i]) == False:
                        self.columnCount = i+1
            
            # On crée la table
                for i in range(self.columnCount):
                    if(is_only_number(self.generalList[i][1:])):
                        # S'il n y a que des nombres alors c'est DOUBLE
                        text_to_execute = text_to_execute+ str(self.generalList[i][0])+" DOUBLE,\n"
                    else:
                        # Sinon c'est TEXT
                        text_to_execute = text_to_execute+ str(self.generalList[i][0])+" TEXT,\n"
                    
                text_to_execute = text_to_execute[0:len(text_to_execute)-2]+")"
            
                #On crée le code permettant d'enregister les donneés
            
                insert_text = "INSERT INTO "+self.data_base_table_name_receiver2.text()+"("
                
                v = " VALUES("
                for i in range(self.columnCount):
                    insert_text = insert_text+str(self.generalList[i][0])+","
                    v = v+"?,"
            
                v = v[0:len(v)-1] + ")"    
                insert_text = insert_text[0:len(insert_text)-1] +")"
            
                insert_text = insert_text+v 
                print(text_to_execute,"\n\n")
                print(insert_text)
                
                conn.execute(text_to_execute)
                data = []
                
                for i in range(self.rowCount):
                    r = []
                    for u in range(self.columnCount):
                        r.append(self.generalList[u][i])
                    data.append(tuple(r))
                    
                conn.executemany(insert_text,data)
                conn.commit()
                    
                
            
        
        
        #POUR DETERMINER LES ITEMS CHOISI
        
        
    def existing_base_export(self):
        
        if 1:
            
            f = QFileDialog()
            name = f.getOpenFileName(self,"Enrégister dans une base de donnée existante",str(),"")
            if len(name) !=0:
                name = name[0]
                conn = sqlite3.connect(name)
                cur = conn.cursor()
                text_to_execute = "CREATE TABLE IF NOT EXISTS " +self.data_base_table_name_receiver.text()+\
                "(id INTEGER PRIMARY\n"+"KEY AUTOINCREMENT UNIQUE,\n"
            
                # On prépare les données pour le travail
                self.clear_list()
                self.clear_general_list()
                self.add_list_to_general_list()
                self.table_view_to_list()
                
                for i in range(len(self.generalList)):
                    if self.is_list_empty(self.generalList[i]) == False:
                        self.columnCount = i+1
            
            # On crée la table
                for i in range(self.columnCount):
                    if(is_only_number(self.generalList[i][1:])):
                        text_to_execute = text_to_execute+ str(self.generalList[i][0])+" DOUBLE,\n"
                    else:
                        text_to_execute = text_to_execute+ str(self.generalList[i][0])+" TEXT,\n"
                    
                text_to_execute = text_to_execute[0:len(text_to_execute)-2]+")"
            
                #On crée le code permettant d'enregister les donneés
            
                insert_text = "INSERT INTO "+self.data_base_table_name_receiver.text()+"("
                
                v = " VALUES("
                for i in range(self.columnCount):
                    insert_text = insert_text+str(self.generalList[i][0])+","
                    v = v+"?,"
            
                v = v[0:len(v)-1] + ")"    
                insert_text = insert_text[0:len(insert_text)-1] +")"
            
                insert_text = insert_text+v 
                print(text_to_execute,"\n\n")
                print(insert_text)
                
                conn.execute(text_to_execute)
                data = []
                
                for i in range(self.rowCount):
                    r = []
                    for u in range(self.columnCount):
                        r.append(self.generalList[u][i])
                    data.append(tuple(r))
                    
                conn.executemany(insert_text,data)
                conn.commit()
                    
                
            
        
        
        #POUR DETERMINER LES ITEMS CHOISI
        
    
    def copy(self):
        self.selected_items()
        
    def selected_items(self):
        print("yes")
        selection = self.tableView.selectionModel()
        listeSelections = selection.selectedColumns(0)
        elementsSelectionnes = ""
        for i in range(len(listeSelections)):
            print(self.tableModel.data(listeSelections[i],Qt.DisplayRole))
        
        
    def update_local_data(self):
        self.clear_list()
        self.clear_general_list()
        self.add_list_to_general_list()
        self.table_view_to_list()
        
        a = list(self.generalList)
        for i in range(len(a)):
            x = a[i]
            for i in range(len(x)):
                if x[i] == "":
                    x[i] = "0"  
        print(len(a))
                    
        self.send_data.emit(a)
        
        
    def save_as(self):
        fd = QFileDialog()
        name = ""
        filename = fd.getSaveFileName(self,"Enrégistrer le fichier",str(),"*.wdata")
        if len(filename) != 0:
            print(filename)
            name = filename[0]
           
            
            self.clear_list()
            self.clear_general_list()
            self.add_list_to_general_list()
        
            self.table_view_to_list()
            
            self.columnCount = 0
            for i in range(1,len(self.generalList)):
                if self.is_list_empty(self.generalList[i]) == False:
                    self.columnCount = i+1
                    
            f = io.open(filename[0],"w",encoding = "utf-8")
            if global_state.CODE_CREATED:
                f.write("ANALYS-file-version-2\n")
                f.write("<data>\n")
                
            for i in range(self.rowCount):
                for u in range(self.columnCount):
                    if u <self.columnCount-1:    
                        f.write(str(self.generalList[u][i])+"," )
                    else:
                        f.write(str(self.generalList[u][i]))
                f.write(" \n")
                
            if global_state.CODE_CREATED:
                f.write("</data>\n")
                f.write("<code>\n")
                for i in self.codeWidget.editor_list:
                    i.update_code()
                    f.write("<script>\n"+i.code+"\n</script>\n")
                f.write("</code>\n")
                
            f.close()
                    
                
            
        
    def init_connection(self):
        self.scriptLineEdit.returnPressed.connect(self.init_script)
        self.tableModel.row_m_modified.connect(self.increase_m_modi)
        
    def csv_export(self):
        
        f = QFileDialog()
        filename = f.getSaveFileName(self,"Exporter comme un csv",str()," *.csv")
        if len(filename) != 0:
            print(filename)
            name = filename[0]
            dic = dict()
            
            self.clear_list()
            self.clear_general_list()
            self.add_list_to_general_list()
        
            self.table_view_to_list()
            
            for i in range(1,len(self.generalList)):
                if self.is_list_empty(self.generalList[i]) == False:
                    self.columnCount = i+1
                
            for i in range(self.columnCount):
                if i != 0:
                    if self.generalList[i][0] == self.generalList[i-1][0]:
                        dic[str(self.generalList[i][0])+" "*i] = self.generalList[i][1:len(self.generalList[i])]
                    else:
                        dic[self.generalList[i][0]] = self.generalList[i][1:len(self.generalList[i])]
                else:
                    dic[self.generalList[i][0]] = self.generalList[i][1:len(self.generalList[i])]
                
            df = pd.DataFrame(dic)
            df.to_csv(name)
    def html_export(self):
        f = QFileDialog()
        filename = f.getSaveFileName(self,"Exporter sous forme html",str(),"*.html")
        if len(filename) != 0:
            print(filename)
            name = filename[0]
            dic = dict()
            
            self.clear_list()
            self.clear_general_list()
            self.add_list_to_general_list()
        
            self.table_view_to_list()
            
            for i in range(1,len(self.generalList)):
                if self.is_list_empty(self.generalList[i]) == False:
                    self.columnCount = i+1
                
            for i in range(self.columnCount):
                if i != 0:
                    if self.generalList[i][0] == self.generalList[i-1][0]:
                        dic[str(self.generalList[i][0])+" "*i] = self.generalList[i][1:len(self.generalList[i])]
                    else:
                        dic[self.generalList[i][0]] = self.generalList[i][1:len(self.generalList[i])]
                else:
                    dic[self.generalList[i][0]] = self.generalList[i][1:len(self.generalList[i])]
                
            df = pd.DataFrame(dic)
            df.to_html(name)
            
    def excel_export(self):
        f = QFileDialog()
        filename = f.getSaveFileName(self,"Exporter sous forme excel",str(),"*.xlsx *.xls")
        if len(filename) != 0:
            print(filename)
            name = filename[0]
            dic = dict()
            
            self.clear_list()
            self.clear_general_list()
            self.add_list_to_general_list()
        
            self.table_view_to_list()
            
            for i in range(1,len(self.generalList)):
                if self.is_list_empty(self.generalList[i]) == False:
                    self.columnCount = i+1
                
            for i in range(self.columnCount):
                if i != 0:
                    if self.generalList[i][0] == self.generalList[i-1][0]:
                        dic[str(self.generalList[i][0])+" "*i] = self.generalList[i][1:len(self.generalList[i])]
                    else:
                        dic[self.generalList[i][0]] = self.generalList[i][1:len(self.generalList[i])]
                else:
                    dic[self.generalList[i][0]] = self.generalList[i][1:len(self.generalList[i])]
                
            df = pd.DataFrame(dic)
            df.to_excel(name)
    
    def init_table_view(self):
        if self.columnCount > 26:
            self.columnCount = 26
            
        
        
        # On détermine le nombre de colonne qu'il y a   
        for i in range(len(self.generalList)):
            if self.is_list_empty(self.generalList[i]) == False:
                #print("ELVIS ",len(self.generalList[i]))
                self.rowCount = max(self.rowCount,len(self.generalList[i]))
                self.columnCount = i+1
            
        """ Maintenant on met toute les colonnes à la même taille """
        
        for i in range(len(self.generalList)):
            if len(self.generalList[i]) < self.rowCount:
                for u in range(len(self.generalList[i]),self.rowCount):
                    self.generalList[i].append("")
                    
        """ On prépare le rendu visuel """
        
        for i in range(self.columnCount):
            for u in range(self.rowCount):
                self.tableModel.setItem(u,i,QStandardItem(""))
                
        # On remplit toutes les cellules
        for i in range(self.rowCount):
            a = list()
            for u in range(26):
                a.append(QStandardItem(""))
            self.tableModel.insertRow(i,a)
            a.clear()
            
        
        #print("##########################################################",self.rowCount)
        for i in range(self.rowCount):
            for u in range(self.columnCount):
                self.tableModel.setItem(i,u,QStandardItem(str(self.generalList[u][i])))
                
        self.tableModel.setRowCount(self.rowCount)
    
    def increase_m_modi(self):
        a= 0
        #self.rowCount = self.rowCount + 1
        
    def table_view_to_list(self):
        self.rowCount = self.tableModel.rowCount(QModelIndex())
        for i in range(26):
            for u in range(self.rowCount):
                self.generalList[i].append(self.tableModel.item(u,i).text())
    
            
    def open_file(self):
        f = QFileDialog()
        filename = f.getOpenFileName(self)
        if len(filename) != 0:
            
            print(filename)
            self.name = filename[0]
            info = QFileInfo(self.name)
            if info.suffix() == "xlsx" or info.suffix() == "xls":
                
                self.clear_list()
                self.clear_general_list()
                self.add_list_to_general_list()
                
                df = pd.read_excel(self.name,header = None)
                self.rowCount = len(df)
                self.columnCount = len(df.columns)
                if self.columnCount > 26:
                    self.columnCount = 26
                
                for i in range(self.columnCount):
                    self.generalList[i] = open.copy_list(self.generalList[i],df[i])
                    
                self.init_table_view()
                
            elif info.suffix() == "wdata":
                self.wdata_open(self.name)
            else:
                self.w.show()
    
    def open_file_(self,name):
        self.name = name
        
        info = QFileInfo(name)
        if info.suffix() == "xlsx" or info.suffix() == "xls":
                
            self.clear_list()
            self.clear_general_list()
            self.add_list_to_general_list()
                
            df = pd.read_excel(self.name,header = None)
            self.rowCount = len(df)
            self.columnCount = len(df.columns)
            if self.columnCount > 26:
                self.columnCount = 26
                
            for i in range(self.columnCount):
                self.generalList[i] = open.copy_list(self.generalList[i],df[i])
                    
            self.init_table_view()
            
        elif info.suffix() == "wdata":
            self.wdata_open(self.name)
        else:
            self.w.show()
        
    def wdata_open(self,name):
        self.clear_list()
        self.clear_general_list()
        self.add_list_to_general_list()
        
        a = open.open_file(name)
        if(len(a) != 2):
            print("simple wdata")
            for i in range(len(a)):
                self.generalList[i] = open.copy_list(self.generalList[i],a[i])
            self.init_table_view()
            
        elif (len(a) == 2):
            
            for i in range(len(a[0])):
                self.generalList[i] = open.copy_list(self.generalList[i],a[0][i])

            self.init_table_view()
            # Ici on se charge des codes
            for i in a[1]:
                self.codeWidget.addeditor_whithcode(i)
                
            self.showcodewidget()
            
        
            
    def other_open(self):
        self.clear_list()
        self.clear_general_list()
        self.add_list_to_general_list()
        
        print( "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", self.line_edit.text())
                
        df = pd.read_csv(self.name,header = None,sep = self.line_edit.text())
        self.rowCount = len(df)
        self.columnCount = len(df.columns)
        #print(df)
        #print(self.rowCount)
        #print(self.columnCount)
                
        if self.columnCount > 26:
            self.columnCount = 26
                
        for i in range(self.columnCount):
            self.generalList[i] = list(df[i])
            
        self.init_table_view()
        self.w.close()
            
        
    def show_warning(self,text):
        QMessageBox.information(self,"Information",text)
                
    def init_script(self):
        self.clear_list()
        self.clear_general_list()
        self.add_list_to_general_list()
        self.table_view_to_list()
        
        self.script_object = ScriptClass(self.generalList)
        self.script_object.send_warning.connect(self.show_warning)
        
        result = self.script_object.to_fonction(self.scriptLineEdit.text())
        
        if type(result) == list:   
            self.generalList = result
            self.init_table_view()
            
        elif type(result) == tuple:
            if type(result[0]) == list:
                self.generalList = result[0]
                if type(result[1]) == int:
                    self.rowCount = self.rowCount -int(result[1])
                self.init_table_view()
        elif type(result) == float or type(result) == int or type(result) == str:
            self.resultLineEdit.setText(self.scriptLineEdit.text()+ " = " +str(result))
            
        
    def exec(self,code):
        print(code)
        self.clear_list()
        self.clear_general_list()
        self.add_list_to_general_list()
        self.table_view_to_list()
        
        self.script_object = ScriptClass(self.generalList)
        self.script_object.send_warning.connect(self.show_warning)
        
        result = self.script_object.to_fonction(code)
        
        if type(result) == list:   
            self.generalList = result
            self.init_table_view()
            
        elif type(result) == tuple:
            if type(result[0]) == list:
                self.generalList = result[0]
                if type(result[1]) == int:
                    self.rowCount = self.rowCount -int(result[1])
                self.init_table_view()
        elif type(result) == float or type(result) == int or type(result) == str:
            self.resultLineEdit.setText(self.scriptLineEdit.text()+ " = " +str(result))
        
         
        
    def add_list_to_general_list(self):
        self.generalList.append(self.listA)
        self.generalList.append(self.listB)
        self.generalList.append(self.listC)
        self.generalList.append(self.listD)
        self.generalList.append(self.listE)
        self.generalList.append(self.listF)
        self.generalList.append(self.listG)
        self.generalList.append(self.listH)
        self.generalList.append(self.listI)
        self.generalList.append(self.listJ)
        self.generalList.append(self.listK)
        self.generalList.append(self.listL)
        self.generalList.append(self.listM)
        self.generalList.append(self.listN)
        self.generalList.append(self.listO)
        self.generalList.append(self.listP)
        self.generalList.append(self.listQ)
        self.generalList.append(self.listR)
        self.generalList.append(self.listS)
        self.generalList.append(self.listT)
        self.generalList.append(self.listU)
        self.generalList.append(self.listV)
        self.generalList.append(self.listW)
        self.generalList.append(self.listX)
        self.generalList.append(self.listY)
        self.generalList.append(self.listZ)
        
    def clear_general_list(self):
        self.generalList.clear()
        
    def clear_list(self):
        self.listA.clear()
        self.listB.clear()
        self.listC.clear()
        self.listD.clear()
        self.listE.clear()
        self.listF.clear()
        self.listG.clear()
        self.listH.clear()
        self.listI.clear()
        self.listJ.clear()
        self.listK.clear()
        self.listL.clear()
        self.listM.clear()
        self.listN.clear()
        self.listO.clear()
        self.listP.clear()
        self.listQ.clear()
        self.listR.clear()
        self.listS.clear()
        self.listT.clear()
        self.listU.clear()
        self.listV.clear()
        self.listW.clear()
        self.listX.clear()
        self.listY.clear()
        self.listZ.clear()
        
        
    def execute(self,code):
        compiled = ""
        comp_error = ""
        executed = ""

        try:
            compiled = compile(code,"error.txt","exec")
        except Exception as e:
            self.send_errormessage.emit(str(e))
            #print("error--------",e)
            
        try:
            executed = exec(compiled)
            
        except Exception as e:
            self.send_errormessage.emit(str(e))
            #print("error++++++++++",e)
            
                
    def is_list_empty(self,tab):
        empty = True
        for i in range(len(tab)):
            if tab[i] != "":
                empty = False
                return empty
                break
            
    def showcodewidget(self):
        global_state.CODE_CREATED = True
        self.codeWidget.mainwindow_send_code.connect(self.execute)
        self.send_errormessage.connect(self.codeWidget.set_error_message)
        self.codeWidget.show()
        
        
    def closeEvent(self,event):
        self.codeWidget.close()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TableViewWidget()
    w.show()
    sys.exit(app.exec())