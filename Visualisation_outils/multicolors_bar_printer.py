# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 11:56:00 2021

@author: Elvis
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure
from matplotlib.backend_bases import Event
from matplotlib.backend_bases import MouseButton 
import matplotlib.pyplot as plt

from locals.datasfile import *
from State.global_state import SOFTWARE_NAME
from Visualisation_outils.m_parser import *
from Visualisation_outils.plothelper import *
from Visualisation_outils.textreceiver import *
from Visualisation_outils.printer import *

import numpy as np

class MulticolorBarPrinter(Printer):
    def __init__(self):
        super().__init__()
        
        self.layout_principale = QVBoxLayout()
        self.init_UI()
        
    def init_UI(self):
        self.setWindowTitle("Multicolors Bar")
        
    def multicolor_bar(self,info):
        #print("yes we get it ",info)
        labels = []
        choices = []
        colors = []
        limits = []
        for i in range(len(info)-1):
            a = info[i]
            choices.append(a[0][0])
            colors.append(a[1][0])
            limits.append(a[2][0])
            labels.append(a[3][0])
        
        prepared_data = []
        print("\n\n")
        print(labels,choices,colors,limits,sep = "\n")
        
        for i in range(len(choices)):
            a =limits[i][0]
            b = limits[i][1]
            if(b > a):
                b = b+1
            
                if is_only_number(self.datas[choices[i]][a:b]):
                    prepared_data.append(self.datas[choices[i]][a:b])
                else:
                    QMessageBox.information(self,"Information","La partie de la colonne "+
                                        TABLES_NAMES[choices[i]] + "allant de " +str(a) + 
                                        " à "+str(b-1) + " contient un caractère non numérique")
            elif b == a:
                if is_only_number(self.datas[choices[i]][a]):
                    prepared_data.append(self.datas[choices[i]])
                else:
                    QMessageBox.information(self,"Information","La partie de la colonne "+
                                        TABLES_NAMES[choices[i]] + "allant de " +str(a) + 
                                        " à "+str(b-1) + " contient un caractère non numérique")
        
        k = len(prepared_data)
        w = 0.35
        x = list(np.arange(0,len(prepared_data[0])))
        print("PREPARED DATA \n\n",x,"   ",str_to_float(prepared_data[0]))
        
        for i in range(len(prepared_data)):
            prepared_data[i] = str_to_float(prepared_data[i])
        
        
        self.ax.bar(x,
                    prepared_data[0],
                    color = colors[0],
                    label = labels[0],
                    width = w)
        
        k = 0
        bottoms = prepared_data[0]
        for  i in range(1,len(prepared_data)): 
            
            self.ax.bar(x,
                    prepared_data[i],
                    color = colors[i],
                    label = labels[i],
                    bottom = bottoms,
                    width = w)
            for u in range(len(bottoms)):
                bottoms[u] = bottoms[u]+prepared_data[i][u]
                
        self.ax.set_title(info[len(info)-1][0] + "                      | Created with "+SOFTWARE_NAME)
        self.ax.set_xlabel(info[len(info)-1][1])
        self.ax.set_ylabel(info[len(info)-1][2])
        
        self.ax.legend()
        self.canvas.draw()
        self.show()
            
        
def str_to_float(tab):
    print("tab = ",tab)
    r = []
    for i in range(len(tab)):
        r.append(float(tab[i]))
    return r

#print(str_to_float(["2","3"]))

"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MulticolorBarPrinter()
    w.show()
    sys.exit(app.exec_())
"""
    
        
        