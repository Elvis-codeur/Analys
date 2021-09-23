# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 14:10:55 2021

@author: Elvis
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 16:08:55 2020

@author: Elvis
"""


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

from locals.datasfile import *
from Visualisation_outils.buttons import *
from Visualisation_outils.m_parser import *
from Visualisation_outils.multiplebarprinter3d import *
from Visualisation_outils.stackbuttons import *

class MultipleColorsBarInfoReceiver(QWidget):
    data = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        
        self.radio_button_list = list()
        self.stackbutton_list = list()
        
        self.radio_button_A = QCheckBox("Tab_A")
        self.radio_button_B = QCheckBox("Tab_B")
        self.radio_button_C = QCheckBox("Tab_C")
        self.radio_button_D = QCheckBox("Tab_D")
        
        self.radio_button_E = QCheckBox("Tab_E")
        self.radio_button_F = QCheckBox("Tab_F")
        self.radio_button_G = QCheckBox("Tab_G")
        self.radio_button_H = QCheckBox("Tab_H")
        
        self.radio_button_I = QCheckBox("Tab_I")
        self.radio_button_J = QCheckBox("Tab_J")
        self.radio_button_K = QCheckBox("Tab_K")
        self.radio_button_L = QCheckBox("Tab_L")
        
        self.radio_button_M = QCheckBox("Tab_M")
        self.radio_button_N = QCheckBox("Tab_N")
        self.radio_button_O = QCheckBox("Tab_O")
        self.radio_button_P = QCheckBox("Tab_P")
        
        self.radio_button_Q = QCheckBox("Tab_Q")
        self.radio_button_R = QCheckBox("Tab_R")
        self.radio_button_S = QCheckBox("Tab_S")
        self.radio_button_T = QCheckBox("Tab_T")
        
        self.radio_button_U = QCheckBox("Tab_U")
        self.radio_button_V = QCheckBox("Tab_V")
        self.radio_button_W = QCheckBox("Tab_W")
        self.radio_button_X = QCheckBox("Tab_X")
        
        self.radio_button_Y = QCheckBox("Tab_Y")
        self.radio_button_Z = QCheckBox("Tab_Z")
        
        #BUTTONS
        
        self.text_receiver_button_A = StackButton("Tab_A")
        self.text_receiver_button_B = StackButton("Tab_B")
        self.text_receiver_button_C = StackButton("Tab_C")
        self.text_receiver_button_D = StackButton("Tab_D")
        
        self.text_receiver_button_E = StackButton("Tab_E")
        self.text_receiver_button_F = StackButton("Tab_F")
        self.text_receiver_button_G = StackButton("Tab_G")
        self.text_receiver_button_H = StackButton("Tab_H")
        
        self.text_receiver_button_I = StackButton("Tab_I")
        self.text_receiver_button_J = StackButton("Tab_J")
        self.text_receiver_button_K = StackButton("Tab_K")
        self.text_receiver_button_L = StackButton("Tab_L")
        
        self.text_receiver_button_M = StackButton("Tab_M")
        self.text_receiver_button_N = StackButton("Tab_N")
        self.text_receiver_button_O = StackButton("Tab_O")
        self.text_receiver_button_P = StackButton("Tab_P")
        
        self.text_receiver_button_Q = StackButton("Tab_Q")
        self.text_receiver_button_R = StackButton("Tab_R")
        self.text_receiver_button_S = StackButton("Tab_S")
        self.text_receiver_button_T = StackButton("Tab_T")
        
        self.text_receiver_button_U = StackButton("Tab_U")
        self.text_receiver_button_V = StackButton("Tab_V")
        self.text_receiver_button_W = StackButton("Tab_W")
        self.text_receiver_button_X = StackButton("Tab_X")
        
        self.text_receiver_button_Y = StackButton("Tab_Y")
        self.text_receiver_button_Z = StackButton("Tab_Z")
        
        
        
        
        
     
        
        # LES LAYOUTS
        self.inter_layout = QVBoxLayout()
        self.radio_button_groupbox = QGroupBox()
        self.radio_button_layout = QGridLayout()
        self.layout_principale = QVBoxLayout()
        
        self.button_groupbox = QGroupBox("Information")
        self.button_layout = QGridLayout()
        
       
        
        self.final_button = QPushButton("Terminer")
       
        
        self.init_UI()
        
    def init_UI(self):
        
        self.final_button.clicked.connect(self.terminer)
        
        self.setWindowIcon(QIcon("analys.png"))
        self.setWindowTitle("Fenêtre de renseignement du diagramme bandes multicolores")
        self.add_radiobutton_to_list()
        self.manage_radio_button()
        self.manage_stackbutton()
        self.add_stackbutton_to_list()
        self.other_manage()
        
        self.radio_button_groupbox.setLayout(self.radio_button_layout)
        self.inter_layout.addWidget(self.radio_button_groupbox)
        
        
        self.button_groupbox.setLayout(self.button_layout)
        self.inter_layout.addWidget(self.button_groupbox)
        
        self.layout_principale.addLayout(self.inter_layout)
        self.layout_principale.addWidget(self.final_button)
        
        
        self.setLayout(self.layout_principale)
        
        
        
    def other_manage(self):
        
        a = 0
        
    def add_stackbutton_to_list(self):
        self.stackbutton_list.append(self.text_receiver_button_A)
        self.stackbutton_list.append(self.text_receiver_button_B)
        self.stackbutton_list.append(self.text_receiver_button_C)
        self.stackbutton_list.append(self.text_receiver_button_D)
        self.stackbutton_list.append(self.text_receiver_button_E)
        
        self.stackbutton_list.append(self.text_receiver_button_F)
        self.stackbutton_list.append(self.text_receiver_button_G)
        self.stackbutton_list.append(self.text_receiver_button_H)
        self.stackbutton_list.append(self.text_receiver_button_I)
        self.stackbutton_list.append(self.text_receiver_button_J)
        
        self.stackbutton_list.append(self.text_receiver_button_K)
        self.stackbutton_list.append(self.text_receiver_button_L)
        self.stackbutton_list.append(self.text_receiver_button_M)
        self.stackbutton_list.append(self.text_receiver_button_N)
        self.stackbutton_list.append(self.text_receiver_button_O)
        
        self.stackbutton_list.append(self.text_receiver_button_P)
        self.stackbutton_list.append(self.text_receiver_button_Q)
        self.stackbutton_list.append(self.text_receiver_button_R)
        self.stackbutton_list.append(self.text_receiver_button_S)
        self.stackbutton_list.append(self.text_receiver_button_T)
        
        self.stackbutton_list.append(self.text_receiver_button_U)
        self.stackbutton_list.append(self.text_receiver_button_V)
        self.stackbutton_list.append(self.text_receiver_button_W)
        self.stackbutton_list.append(self.text_receiver_button_X)
        self.stackbutton_list.append(self.text_receiver_button_Y)
        
        self.stackbutton_list.append(self.text_receiver_button_Z)
        
        
        
    def manage_stackbutton(self):
        self.button_layout.addWidget(self.text_receiver_button_A,0,0,1,1)
        self.button_layout.addWidget(self.text_receiver_button_B,0,1,1,1)
        self.button_layout.addWidget(self.text_receiver_button_C,0,2,1,1)
        self.button_layout.addWidget(self.text_receiver_button_D,0,3,1,1)
        self.button_layout.addWidget(self.text_receiver_button_E,0,4,1,1)
        
        self.button_layout.addWidget(self.text_receiver_button_F,1,0,1,1)
        self.button_layout.addWidget(self.text_receiver_button_G,1,1,1,1)
        self.button_layout.addWidget(self.text_receiver_button_H,1,2,1,1)
        self.button_layout.addWidget(self.text_receiver_button_I,1,3,1,1)
        self.button_layout.addWidget(self.text_receiver_button_J,1,4,1,1)
        
        self.button_layout.addWidget(self.text_receiver_button_K,2,0,1,1)
        self.button_layout.addWidget(self.text_receiver_button_L,2,1,1,1)
        self.button_layout.addWidget(self.text_receiver_button_M,2,2,1,1)
        self.button_layout.addWidget(self.text_receiver_button_N,2,3,1,1)
        self.button_layout.addWidget(self.text_receiver_button_O,2,4,1,1)
        
        self.button_layout.addWidget(self.text_receiver_button_P,3,0,1,1)
        self.button_layout.addWidget(self.text_receiver_button_Q,3,1,1,1)
        self.button_layout.addWidget(self.text_receiver_button_R,3,2,1,1)
        self.button_layout.addWidget(self.text_receiver_button_S,3,3,1,1)
        self.button_layout.addWidget(self.text_receiver_button_T,3,4,1,1)
        
        self.button_layout.addWidget(self.text_receiver_button_U,4,0,1,1)
        self.button_layout.addWidget(self.text_receiver_button_V,4,1,1,1)
        self.button_layout.addWidget(self.text_receiver_button_W,4,2,1,1)
        self.button_layout.addWidget(self.text_receiver_button_X,4,3,1,1)
        self.button_layout.addWidget(self.text_receiver_button_Y,4,4,1,1)
        
        self.button_layout.addWidget(self.text_receiver_button_Z,5,2,1,1)
        
        
        
    def manage_radio_button(self):
        self.radio_button_layout.addWidget(self.radio_button_A,0,0,1,1)
        self.radio_button_layout.addWidget(self.radio_button_B,0,1,1,1)
        self.radio_button_layout.addWidget(self.radio_button_C,0,2,1,1)
        self.radio_button_layout.addWidget(self.radio_button_D,0,3,1,1)
        self.radio_button_layout.addWidget(self.radio_button_E,0,4,1,1)
        
        self.radio_button_layout.addWidget(self.radio_button_F,1,0,1,1)
        self.radio_button_layout.addWidget(self.radio_button_G,1,1,1,1)
        self.radio_button_layout.addWidget(self.radio_button_H,1,2,1,1)
        self.radio_button_layout.addWidget(self.radio_button_I,1,3,1,1)
        self.radio_button_layout.addWidget(self.radio_button_J,1,4,1,1)

        self.radio_button_layout.addWidget(self.radio_button_K,2,0,1,1)
        self.radio_button_layout.addWidget(self.radio_button_L,2,1,1,1)
        self.radio_button_layout.addWidget(self.radio_button_M,2,2,1,1)
        self.radio_button_layout.addWidget(self.radio_button_N,2,3,1,1)
        self.radio_button_layout.addWidget(self.radio_button_O,2,4,1,1)
        
        self.radio_button_layout.addWidget(self.radio_button_P,3,0,1,1)
        self.radio_button_layout.addWidget(self.radio_button_Q,3,1,1,1)
        self.radio_button_layout.addWidget(self.radio_button_R,3,2,1,1)
        self.radio_button_layout.addWidget(self.radio_button_S,3,3,1,1)
        self.radio_button_layout.addWidget(self.radio_button_T,3,4,1,1)
        
        self.radio_button_layout.addWidget(self.radio_button_U,4,0,1,1)
        self.radio_button_layout.addWidget(self.radio_button_V,4,1,1,1)
        self.radio_button_layout.addWidget(self.radio_button_W,4,2,1,1)
        self.radio_button_layout.addWidget(self.radio_button_X,4,3,1,1)
        self.radio_button_layout.addWidget(self.radio_button_Y,4,4,1,1)
        
        self.radio_button_layout.addWidget(self.radio_button_Z,5,2,1,1)
        
        
    def add_radiobutton_to_list(self):
        self.radio_button_list.append(self.radio_button_A)
        self.radio_button_list.append(self.radio_button_B)
        self.radio_button_list.append(self.radio_button_C)
        self.radio_button_list.append(self.radio_button_D)
        
        self.radio_button_list.append(self.radio_button_E)
        self.radio_button_list.append(self.radio_button_F)
        self.radio_button_list.append(self.radio_button_G)
        self.radio_button_list.append(self.radio_button_H)
        
        self.radio_button_list.append(self.radio_button_I)
        self.radio_button_list.append(self.radio_button_J)
        self.radio_button_list.append(self.radio_button_K)
        self.radio_button_list.append(self.radio_button_L)
        
        self.radio_button_list.append(self.radio_button_M)
        self.radio_button_list.append(self.radio_button_N)
        self.radio_button_list.append(self.radio_button_O)
        self.radio_button_list.append(self.radio_button_P)
        
        self.radio_button_list.append(self.radio_button_Q)
        self.radio_button_list.append(self.radio_button_R)
        self.radio_button_list.append(self.radio_button_S)
        self.radio_button_list.append(self.radio_button_T)
        
        
        self.radio_button_list.append(self.radio_button_U)
        self.radio_button_list.append(self.radio_button_V)
        self.radio_button_list.append(self.radio_button_W)
        self.radio_button_list.append(self.radio_button_X)
        
        self.radio_button_list.append(self.radio_button_Y)
        self.radio_button_list.append(self.radio_button_Z)
        
        
    def terminer(self):
        choice = list()
        colors = list()
        limits = list()
        labels = list()
        for i in range(len(self.radio_button_list)):
            if self.radio_button_list[i].isChecked():
                choice.append(i)
                
        for i in range(len(choice)):
            a = self.stackbutton_list[choice[i]].get_data()
            labels.append(a[0])
            limits.append(a[1])
            colors.append(a[2])
            
        #print(["ELVIS KOM SCRYKRU",choice,labels,colors,limits])
        
        
        self.data.emit([choice,
                        colors,
                        limits,
                        labels])
        self.close()
            
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MultipleColorsBarInfoReceiver()
    a.show()
    sys.exit(app.exec())      
        
    