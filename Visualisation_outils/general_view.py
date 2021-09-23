# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:13:45 2021

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

import numpy as np

from  Visualisation.visualisation_choose_widget import *

class GeneralPrinter(QMainWindow):
    def __init__(self):
        self.datas = []
        
        self.AXISNUMBER = 0
        self.AXIS_TAB = []
        self.datas = []
        self.ploting_info = dict()
        self.ax = 0
        
        
        super().__init__()
        self.figure = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas,self)
        
        # Le nombre de subdivision
        self.line_number_receiver = QSpinBox()
        self.column_number_receiver = QSpinBox()
        
        #L'abscisse du graphique
        self.draw_abcisse_receiver = QSpinBox()
        self.draw_ordonne_receiver = QSpinBox()
        
        # La taille du graphique
        self.new_line_number_receiver = QSpinBox()
        self.new_column_number_receiver = QSpinBox()
        self.new_ok_button = QPushButton("OK")
        
        
        self.choice_widget = VisualisationChooseWidget()
        
        self.layout_principale = QVBoxLayout()
        self.widget_layout = QHBoxLayout()
        self.make_connection()
        self.choice_widget.send_ploting_information.connect(self.manage_plot)
        self.manage()
        
        
        
        
    def make_connection(self):
        self.choice_widget.send_ploting_information.connect(self.manage_plot)
        
        
    def manage_plot(self,info):
        print("Received --- 100")
        print(info, "\n\n\n" 
              "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        if "plot info" in info:
            self.plot_on_axis(info["plot info"])
            
        elif "plot info annotation text" in info:
            self.text(info["plot info annotation text"])
            
        elif "plot info annotation modification" in info:
            self.modification(info["plot info annotation modification"])
            
            
    def text(self,info):
        print(info)
        
        if info[0] == 1:
            
            """
            [type d'annoation : text  ou annotation,[famille,couleur,point_size,text à afficher]]
         
             """
            dic = {
                 "family": info[1][0],
                 "color" : info[1][1],
                 "size" : info[1][2]
                 }
            
            self.ax.text(self.text_tuple[0],self.text_tuple[1],info[1][3],fontdict= dic)
            #Pour un transfert ultérieur
            self.text_list.append(info)
            self.canvas.draw()
        else:
            dic = {
                 "family": info[1][0],
                 "color" : info[1][1],
                 "size" : info[1][2]
                 }
            self.ax.annotate(info[1][3],
                             xy = (self.text_tuple[0],self.text_tuple[1]),
                             xytext = (float(info[2][0]),float(info[2][1])),
                             textcoords = "axes fraction",
                             arrowprops = dict(facecolor = info[1][1],color = info[1][1]))
            #Pour un transfert ultérieur
            self.text_list.append(info)
            self.canvas.draw()
        
    def modification(self,tab):
        """[1ou 2 u pour  pas de grille et deux pour grille ,
        [grid_line_style,grid_line_width,grid_color],
        [right,left,top,bottom],[x,y,x_color,y_color]]
        """
        if tab [0] == 1:
            self.figure.subplots_adjust(left = tab[2][1],
                                right = tab[2][0],
                                top = tab[2][2],
                                bottom = tab[2][3])
            
            for labels in self.ax.get_xticklabels():
                labels.set_rotation(tab[3][0])
                labels.set_color(tab[3][2])
            
            for labels in self.ax.get_yticklabels():
                labels.set_rotation(tab[3][1])
                labels.set_color(tab[3][3])
            #Pour un transfert ultérieur
            self.annotation_list.append(tab)
            self.canvas.draw()
            
        elif tab[0] == 2:
            
            self.ax.grid(True,color = tab[1][2],linestyle = tab[1][0],linewidth = tab[1][1])
            
            self.figure.subplots_adjust(left = tab[2][1],
                                right = tab[2][0],
                                top = tab[2][2],
                                bottom = tab[2][3])
            
            for labels in self.ax.xaxis.get_ticklabels():
                labels.set_rotation(tab[3][0])
            
            for labels in self.ax.yaxis.get_ticklabels():
                labels.set_rotation(tab[3][1])
            #Pour un transfert ultérieur
            self.annotation_list.append(tab)
            self.canvas.draw()
             
        
    def plot_on_axis(self,information):
        
        self.ax = self.AXIS_TAB[self.AXISNUMBER-1]
        
        print(information)        
        if information[0] == 1:
            if len(information[1]) == 1:
                
                if type(is_only_number(self.datas[information[1][0]])) == bool :
                    self.datas[information[1][0]] = to_number(self.datas[information[1][0]])
                    
                    
                x = 0
                print(x)
                self.data_1 = self.datas[information[1][0]]
                
                x = np.arange(len(self.datas[information[1][0]]))
                limits = information[4]
                if limits[0] != '' and limits[1] != '':
                    if limits[0] != limits[1]:
                        try:
                            limits[0] = int(limits[0]) -1
                        except:
                            QMessageBox.information(self,"Information","La valeur de la zone de saisie pour le début n'est pas un entier")
                        try:
                            limits[1] = int(limits[1])
                        except:
                             QMessageBox.information(self,"Information","La valeur de la zone de saisie fin n'est pas un entier")
                                
                        x = np.arange(limits[0],limits[1])
                        self.data_1 = self.datas[information[1][0]][limits[0]:limits[1]]
                        #print("I love it")
            
                    
                    
                width = information[3][3]
                
                try:
                    width = int(width)
                except:
                    try:
                        width = float(width)
                    except:
                        QMessageBox.information(self,"Information","La valeur "+str(width)+" que vous avez donnée "
                                                        "comme épaisseur ne convient pas")
                        
                        
                if width > 0:
                        
                    self.ax.plot(self.data_1,
                                color = information[3][0],
                                marker = information[3][1],
                                linestyle = information[3][2],
                                label = information[2][1],
                                linewidth = width)
                else:
                    self.ax.plot(self.data_1,
                                color = information[3][0],
                                marker = information[3][1],
                                label = information[2][1],
                                linewidth = width)
                
                self.ax.set_title(information[2][0])
                self.ax.set_xlabel(information[2][2])
                self.ax.set_ylabel(information[2][3])
                
                self.ploting_info["plot info"] = information
                                
                self.ax.legend()
                self.canvas.draw()
                plt.legend()
                #self.show()
                
            elif len(information[1]) == 2:
                
                if type(is_only_number(self.datas[information[1][0]])) == bool:
                    self.datas[information[1][0]] = to_number(self.datas[information[1][0]])
                    
                if type(is_only_number(self.datas[information[1][1]])) == bool:
                    self.datas[information[1][1]] = to_number(self.datas[information[1][1]])
                    
                    
                
                limits = information[4][0]
                limits1 = information[4][1]
                
                self.data_1 = self.datas[information[1][0]]
                self.data_2 = self.datas[information[1][1]]
                if limits[0] != '' and limits[1] != '':
                        
                    if limits[0] != limits[1]:
                        try:
                            limits[0] = int(limits[0]) -1
                        except:
                            QMessageBox.information(self,"Information","La valeur de la zone de saisie pour le début n'est pas un entier")
                        try:
                            limits[1] = int(limits[1])
                        except:
                            QMessageBox.information(self,"Information","La valeur de la zone de saisie fin n'est pas un entier")
                            
                        self.data_1 = self.datas[information[1][0]][limits[0]:limits[1]]
                            
                if limits1[0] != '' and limits1[1] != '':
                    if limits1[0] != limits1[1]:
                        try:
                            limits1[0] = int(limits1[0])-1
                        except:
                            QMessageBox.information(self,"Information","La valeur de la zone de saisie pour le début n'est pas un entier")
                        try:
                            limits1[1] = int(limits1[1])
                        except:
                            QMessageBox.information(self,"Information","La valeur de la zone de saisie fin n'est pas un entier")
                                
                        self.data_2 = self.datas[information[1][1]][limits1[0]:limits1[1]]
                        
                
                width = information[3][3]
                
                try:
                    width = int(width)
                except:
                    try:
                        width = float(width)
                    except:
                        QMessageBox.information(self,"Information","La valeur "+str(width)+" que vous avez donnée "
                                                        "comme épaisseur ne convient pas")
                
                
                if width > 0:
                        
                    self.ax.plot(self.data_1,
                                 self.data_2,
                                color = information[3][0],
                                marker = information[3][1],
                                linestyle = information[3][2],
                                label = information[2][1],
                                linewidth = width)
                else:
                    self.ax.plot(self.data_1,
                                 self.data_2,
                                color = information[3][0],
                                marker = information[3][1],
                                label = information[2][1],
                                linewidth = width)
                

                
                self.ax.set_title(information[2][0])
                self.ax.set_xlabel(information[2][2])
                self.ax.set_ylabel(information[2][3])
                self.ploting_info["plot info"] = information
                self.ax.legend()
                self.canvas.draw()
                plt.legend()
                #self.show()
        
        
        
        
    def set_printer_data(self,data):
        print("data received")
        self.datas = data
        self.choice_widget.set_printer_data(data)
        
        
    def make_connection(self):
        self.new_ok_button.clicked.connect(self.create_subplots)
        
    
    def create_subplots(self):
        print(((self.line_number_receiver.value(),
                self.column_number_receiver.value()),
               (self.draw_abcisse_receiver.value(),
                self.draw_ordonne_receiver.value()),
               self.new_line_number_receiver.value(),
               self.new_column_number_receiver.value()))
        
        self.AXIS_TAB.append(plt.subplot2grid((self.line_number_receiver.value()*2,
                                  self.column_number_receiver.value()*2),
                                              
                                 (self.draw_ordonne_receiver.value()+1,
                                  self.draw_abcisse_receiver.value()+1),
                                 rowspan = self.new_line_number_receiver.value(),
                                 colspan = self.new_column_number_receiver.value()))
        
        self.ax = self.AXIS_TAB[self.AXISNUMBER]
        self.choice_widget.show()
        
        #self.AXIS_TAB[self.AXISNUMBER].plot([1,-6,7,9,10,5,2,7])
        
        """
        
        self.AXIS_TAB.append(self.figure.add_axes([self.draw_abcisse_receiver.value(),
                                  self.draw_ordonne_receiver.value(),
                                  self.new_line_number_receiver.value(),
                                 self.new_column_number_receiver.value()]))
        
        self.AXIS_TAB[self.AXISNUMBER].plot([1,-6,7,9,10,5,2,7])
        """
        
        #self.canvas.draw()
        #plt.legend()
        #plt.show()
        
        
        self.AXISNUMBER = self.AXISNUMBER + 1
        
        
    def manage(self):
        
        toolbarSub = self.addToolBar("Nombre de subdivision :")
        toolbarSub.addWidget(self.toolbar)
        
        base_limit_layout = QFormLayout()
        base_limit_layout.addRow("Nombre de subdivision en abscisse  ",self.line_number_receiver)
        base_limit_layout.addRow("Nombre de subdivision en ordonée ",self.column_number_receiver)
        
        base_limit_widget = QWidget()
        base_limit_widget.setLayout(base_limit_layout)
        toolbarSub.addWidget(base_limit_widget)
        
        draw_size_layout = QFormLayout()
        draw_size_layout.addRow("Coordonnée en abscisse  ",self.draw_abcisse_receiver)
        draw_size_layout.addRow("Coordonnée en en ordonée ",self.draw_ordonne_receiver)
        draw_widget = QWidget()
        draw_widget.setLayout(draw_size_layout)
        toolbarSub.addWidget(draw_widget)
        
        widget_limit_layout = QFormLayout()
        widget_limit_layout.addRow("Nombre de subdivision en abscisse  ",self.new_line_number_receiver)
        widget_limit_layout.addRow("Nombre de subdivision en ordonée ",self.new_column_number_receiver)
        widget_limit_layout.addRow("Finir",self.new_ok_button)
        
        widget_limit_widget = QWidget()
        widget_limit_widget.setLayout(widget_limit_layout)
        toolbarSub.addWidget(widget_limit_widget)
        
        self.layout_principale.addWidget(self.canvas)
        w = QWidget()
        w.setLayout(self.layout_principale)
        self.setCentralWidget(w)
        
    def closeEvent(self,event):
        self.choice_widget.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = GeneralPrinter()
    a.show()
    sys.exit(app.exec())
        
        
        
        
        
        