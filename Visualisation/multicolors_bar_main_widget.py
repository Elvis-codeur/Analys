# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 14:25:52 2021

@author: Elvis
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Visualisation.single_multiple_bar_widget import *
from Visualisation_outils.multicolors_bar_printer import *
import sys

class MulticolorsBarMainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.toolbar = self.addToolBar("")
        self.bar_number_receiver = QSpinBox()
        self.new_button = QPushButton("Nouveau")
        self.ok_button = QPushButton("ok")
        self.widget_list = []
        
        self.layout_principale = QHBoxLayout()
        #self.layout_principale_ = QHBoxLayout()
        
        self.tab_groupbox = QGroupBox("Labels")
        self.other_layout = QVBoxLayout()
        
        self.widget_principale = QScrollArea()
        
        # Pour les informatoins supplémentaire
        self.tab_groupbox = QGroupBox("Colonnes et labels")
        self.x_label_receiver = QLineEdit()
        self.y_label_receiver = QLineEdit()
        self.title_receiver = QLineEdit()
        self.new_radio_button = QRadioButton("Nouveau")
        
        self.final_button = QPushButton("Terminer")
        self.new_radiobutton = QRadioButton("Nouveau")
        
        # Pour les buttons de réception
        self.info_receiver_layout = QHBoxLayout()
        
        # Pour le graphique
        self.printer = MulticolorBarPrinter()
        self.a = MulticolorBarPrinter()
        self.init_UI()
        self.setGeometry(500,100,800,300)
            
        
    def init_UI(self):
        
        
        font = QFont("Consolas")
        font.setPointSize(18)
        self.bar_number_receiver.setFont(font)
        self.new_button.setMinimumSize(QSize(300,30))
        self.ok_button.setMinimumSize(QSize(300,30))
        #self.toolbar.addWidget(self.bar_number_receiver)
        
        self.bar_info_receiver_layout = QHBoxLayout()
        self.bar_info_receiver_area = QScrollArea()
        
        self.new_button.setFont(font)
        self.toolbar.addWidget(self.new_button)
        
        self.ok_button.setFont(font)
        self.toolbar.addWidget(self.ok_button)
        
        self.w = SingleBarInfoReceiver()
        self.info_receiver_layout.addWidget(self.w)
        self.widget_list.append(self.w)
        
        # CONNECTION
        self.new_button.clicked.connect(self.w.manage_)
        self.ok_button.clicked.connect(self.w.collect_info)
        self.w.send_info.connect(self.multicolorbar)
        
        
        layout1 = QFormLayout()
        layout1.addRow("Label en abscisse",self.x_label_receiver)
        layout1.addRow("Label en ordonnée",self.y_label_receiver)
        layout1.addRow("Titre",self.title_receiver)
        
        layout2 = QVBoxLayout()
        layout2.addLayout(layout1)
        layout2.addWidget(self.new_radio_button)
        
        self.tab_groupbox.setLayout(layout2)
        self.other_layout.addWidget(self.tab_groupbox)
        self.layout_principale.addLayout(self.info_receiver_layout)
        self.layout_principale.addWidget(self.tab_groupbox)
        
        self.widget_principale.setLayout(self.layout_principale)
        self.setCentralWidget(self.widget_principale)
        
    def set_printer_data(self,data):
        self.printer.set_printer_data(data)
        self.a.set_printer_data(data)
        
        
    def multicolorbar(self,information):
        if self.new_radio_button.isChecked():
            information.append([self.title_receiver.text(),
                            self.x_label_receiver.text(),
                            self.y_label_receiver.text()
                            ])
            
            self.a.clear()
            print("\n\n\n",information)
            self.a.multicolor_bar(information)
        else:
            information.append([self.title_receiver.text(),
                            self.x_label_receiver.text(),
                            self.y_label_receiver.text()
                            ])
            
            print("\n\n\n",information)
            self.printer.multicolor_bar(information)
        
    def closeEvent(self,event):
        self.printer.close()
        
    
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MulticolorsBarMainWidget()
    a.show()
    sys.exit(app.exec_())
    
        