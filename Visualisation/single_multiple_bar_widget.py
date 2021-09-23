# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 14:55:59 2021

@author: Elvis
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Visualisation_outils.multicolors_bar_button import *

class SingleBarInfoReceiver(QScrollArea):
    send_info = pyqtSignal(list)
    def __init__(self):
        self.i = 0
        super().__init__()
        
        self.element_list = []
        
        self.layout_principale = QVBoxLayout()
        self.add_button = QPushButton("Ajouter")
        self.button_layout = QVBoxLayout()
        self.manage()
    def manage(self):
        self.add_button.clicked.connect(self.add_element)
        self.layout_principale.addLayout(self.button_layout)
        self.layout_principale.addWidget(self.add_button)
        self.setLayout(self.layout_principale)
        
    def add_element(self):
        a = MultipleColorBarButton()
        self.element_list.append(a)
        self.button_layout.addWidget(self.element_list[self.i])
        self.i = self.i + 1
        del a
        
    def collect_info(self):
        info = []
        # On envoie les informations dans le sens inverse de celui de réception
        i = len(self.element_list)-1
        for u in range(len(self.element_list)):
            info.append(self.element_list[i-u].get_data())
            
        self.send_info.emit(info)
        #print(info)
    def manage_(self):
        for i in range(len(self.element_list)):
            self.button_layout.removeWidget(self.element_list[i])
            self.element_list[i].close()
            
        self.element_list = []
        self.i = 0
            
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w =  SingleBarInfoReceiver()
    w.show();
    sys.exit(app.exec_())
        
        