# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 09:46:23 2020

@author: Elvis
"""

line_styles = ['None','-', '--', '-.', ':', 'solid', 'dashed', 'dashdot', 'dotted']
markers = ['.',
           ','
           ,'o',
           'v',
           '^',  
           '<', 
           '>',  
           '1',  
           '2', 
           '3',  
           '4',  
           's', 
           'p',  
           '*',  
           'h',  
           'H',  
           '+',
           'x',  
           'D', 
           'd',
           '|',  
           '_']

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

from locals.datasfile import *
from Visualisation_outils.buttons import *
from Visualisation_outils.m_parser import *
from Visualisation_outils.barprinter3d import *

# Permet de créer de nouvelle fenêtre quand on utilise nouveau

class BarInfoReceiver_3d(QWidget):
    send_info = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.tab_combobox1 = QComboBox()
        self.tab_combobox2 = QComboBox()
        self.tab_combobox3 = QComboBox()
        self.tab_groupBox = QGroupBox("Colonnes et labels")
        self.x_label_receiver = QLineEdit()
        self.y_label_receiver = QLineEdit()
        self.z_label_receiver = QLineEdit()
        self.data_label_receiver = QLineEdit()
        self.title_receiver = QLineEdit()
        
        self.datas = list()
        
        # POur les limites
        self.limit_1_begin = QSpinBox()
        self.limit_1_begin.setRange(1,1000000000)
        self.limit_1_begin_layout = QFormLayout()
        
        self.limit_1_end = QSpinBox()
        self.limit_1_end.setRange(1,1000000000)
        self.limit_1_end_layout = QFormLayout()
        
        self.limit_1_layout = QHBoxLayout()
        
        self.limit_2_begin = QSpinBox()
        self.limit_2_begin.setRange(1,1000000000)
        self.limit_2_begin_layout = QFormLayout()
        
        self.limit_2_end = QSpinBox()
        self.limit_2_end.setRange(1,1000000000)
        self.limit_2_end_layout = QFormLayout()
        
        self.limit_2_layout = QHBoxLayout()
        
        self.limit_3_begin = QSpinBox()
        self.limit_3_begin.setRange(1,1000000000)
        self.limit_3_begin_layout = QFormLayout()
        
        self.limit_3_end = QSpinBox()
        self.limit_3_end.setRange(1,1000000000)
        self.limit_3_end_layout = QFormLayout()
        
        
        self.limit_3_layout = QHBoxLayout()
        
        
        self.other_groupBox = QGroupBox("Couleurs et Autres")
        self.new_radiobutton = QRadioButton("Nouveau")
        self.final_button = QPushButton("Terminer")
        self.orientation_combobox = QComboBox()
        self.color_push_button = ColorButton()

        self.line_width_box = QLineEdit()
        self.line_width_box.setText("0")
        self.marker_size_box = QSpinBox()
        
        self.layout_principale = QVBoxLayout()
        
        self.init_UI()
        
        
    def init_UI(self):
        self.setWindowIcon(QIcon("analys.png"))
        self.setWindowTitle("Fenêtre de renseignement du diagramme à bandes en trois dimensions")
        # Setting
        self.tab_combobox1.addItems(TABLES_NAMES)
        self.tab_combobox2.addItems(TABLES_NAMES)
        self.tab_combobox3.addItems(TABLES_NAMES)
        #self.orientation_combobox.addItems(['vertical', 'horizontal'])
        self.line_width_box.setText("0")
        layout1 = QFormLayout()
        
        tab_layout = QHBoxLayout()
        tab_layout.addWidget(self.tab_combobox1)
        tab_layout.addWidget(self.tab_combobox2)
        tab_layout.addWidget(self.tab_combobox3)
        
        # Pour les limites
        self.limit_1_begin_layout.addRow("Début",self.limit_1_begin)
        self.limit_1_end_layout.addRow("Fin",self.limit_1_end)
        self.limit_1_layout.addLayout(self.limit_1_begin_layout)
        self.limit_1_layout.addLayout(self.limit_1_end_layout)
        
        self.limit_2_begin_layout.addRow("Début",self.limit_2_begin)
        self.limit_2_end_layout.addRow("Fin",self.limit_2_end)
        self.limit_2_layout.addLayout(self.limit_2_begin_layout)
        self.limit_2_layout.addLayout(self.limit_2_end_layout)
        
        self.limit_3_begin_layout.addRow("Début",self.limit_3_begin)
        self.limit_3_end_layout.addRow("Fin",self.limit_3_end)
        self.limit_3_layout.addLayout(self.limit_3_begin_layout)
        self.limit_3_layout.addLayout(self.limit_3_end_layout)
        
        limit_layout = QHBoxLayout()
        limit_layout.addLayout(self.limit_1_layout)
        limit_layout.addLayout(self.limit_2_layout)
        limit_layout.addLayout(self.limit_3_layout)
        
        layout1.addRow("Colonnes",tab_layout)
        layout1.addRow("Limites",limit_layout)
        layout1.addRow("Label en abscisse",self.x_label_receiver)
        layout1.addRow("Label en ordonnée",self.y_label_receiver)
        layout1.addRow("Label en cote",self.z_label_receiver)
        layout1.addRow("Label des donnée",self.data_label_receiver)
        layout1.addRow("Titre",self.title_receiver)
        
        self.tab_groupBox.setLayout(layout1)
        
        layout2 = QGridLayout()
        
        color_push_button_layout = QFormLayout()
        color_push_button_layout.addRow("Couleur",self.color_push_button)
        layout2.addLayout(color_push_button_layout,0,0,1,3)
        
        # bar width
        line_width_box_layout = QFormLayout()
        line_width_box_layout.addRow("Taille des lignes",self.line_width_box)
        layout2.addLayout(line_width_box_layout,0,3,1,3)
        
        """
        #Orientation
        orientation_combobox_layout = QFormLayout()
        orientation_combobox_layout.addRow("Orientation",self.orientation_combobox)
        layout2.addLayout(orientation_combobox_layout,1,0,1,6)
        """
        
        
        
        """
        marker_size_box_layout = QFormLayout()
        marker_combobox_layout.addRow("Taille des markers",self.marker_size_box)
        layout2.addLayout(marker_combobox_layout,2,0,1,6)
        """
        
        self.other_groupBox.setLayout(layout2)
        
        self.layout_principale.addWidget(self.tab_groupBox)
        self.layout_principale.addWidget(self.other_groupBox)
        self.layout_principale.addWidget(self.new_radiobutton)
        self.layout_principale.addWidget(self.final_button)
        
        self.setLayout(self.layout_principale)
        
        self.setGeometry(125,125,600,450)
        
        
        self.final_button.clicked.connect(self.terminer)
        self.send_info.connect(self.bar_3d)
        self.a = Bar3DPrinter()
        self.bar_printer = Bar3DPrinter()
        
    def terminer(self):
        if self.new_radiobutton.isChecked():
            
            self.send_info.emit([2,[get_tab_pos(self.tab_combobox1.currentText()),
                                    get_tab_pos(self.tab_combobox2.currentText()),
                                    get_tab_pos(self.tab_combobox3.currentText())],
                                               [self.title_receiver.text(),
                                                self.data_label_receiver.text(),
                                                self.x_label_receiver.text(),
                                                self.y_label_receiver.text(),
                                                self.z_label_receiver.text()],
                                             
                                                [self.color_push_button.color_(),
                                                self.orientation_combobox.currentText(),
                                                self.line_width_box.text()],
                                                
                                                [[self.limit_1_begin.text(),
                                                  self.limit_1_end.text()],
                                                 [self.limit_2_begin.text(),
                                                  self.limit_2_end.text()],
                                                 [self.limit_3_begin.text(),
                                                  self.limit_3_end.text()]
                                                 ]])
        else:
             self.send_info.emit([1,[get_tab_pos(self.tab_combobox1.currentText()),
                                     get_tab_pos(self.tab_combobox2.currentText()),
                                     get_tab_pos(self.tab_combobox3.currentText())],
                                               [self.title_receiver.text(),
                                                self.data_label_receiver.text(),
                                                self.x_label_receiver.text(),
                                                self.y_label_receiver.text(),
                                                self.z_label_receiver.text()],
                                             
                                                [self.color_push_button.color_(),
                                                self.orientation_combobox.currentText(),
                                                self.line_width_box.text()],
                                                
                                                [[self.limit_1_begin.text(),
                                                  self.limit_1_end.text()],
                                                 [self.limit_2_begin.text(),
                                                  self.limit_2_end.text()],
                                                 [self.limit_3_begin.text(),
                                                  self.limit_3_end.text()]
                                                 ]])
            
    def bar_3d(self,information):
        print(information)
        if information[0] == 1:
            self.bar_printer.bar3d(information)
            self.bar_printer.show()
            
        elif information[0] == 2:
            information[0] = 1
            self.a.clear()
            self.a.set_datas(self.datas)
            self.a.bar3d(information)
            self.a.show()
            
        
    def set_printer_data(self,data):
        self.datas = data
        self.bar_printer.set_datas(data)
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = BarInfoReceiver_3d()
    w.show()
    sys.exit(app.exec())
        
        
    