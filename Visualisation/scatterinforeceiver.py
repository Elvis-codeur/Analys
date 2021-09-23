# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:12:52 2020

@author: Elvis
"""

line_styles = ['-', '--', '-.', ':', 'None', 'solid', 'dashed', 'dashdot', 'dotted']
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
from Visualisation_outils.scatterprinter import *

# Permet de créer de nouvelle fenêtre quand on utilise nouveau

class ScatterInfoReceiver_1(QWidget):
    send_info = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.tab_combobox = QComboBox()
        self.tab_groupBox = QGroupBox("Colonnes et labels")
        self.x_label_receiver = QLineEdit()
        self.y_label_receiver = QLineEdit()
        self.data_label_receiver = QLineEdit()
        self.title_receiver = QLineEdit()
        
        # Pour les limites
        self.limit_line_box_1 = QSpinBox()
        self.limit_line_box_1.setRange(1,1000000000)
        self.limit_line_box_1_layout = QFormLayout()
        
        self.limit_line_box_2 = QSpinBox()
        self.limit_line_box_2.setRange(1,1000000000)
        self.limit_line_box_2_layout = QFormLayout()
        
        self.limit_layout = QHBoxLayout()
        
        
        self.other_groupBox = QGroupBox("Couleurs et Autres")
        self.final_button = QPushButton("Terminer")
        self.new_radiobutton = QRadioButton("Nouveau")
        self.color_push_button = ColorButton()
        self.line_width_box = QSpinBox()
        self.markers_combobox = QComboBox()
        
        self.layout_principale = QVBoxLayout()
        
        self.init_UI()
        
        
    def init_UI(self):
        self.tab_combobox.addItems(TABLES_NAMES)
        self.line_width_box.setValue(0)
        self.markers_combobox.addItems(markers)
        layout1 = QFormLayout()
        
        # Limite
        self.limit_line_box_1_layout.addRow("Début",self.limit_line_box_1)
        self.limit_line_box_2_layout.addRow("Fin",self.limit_line_box_2)
        self.limit_layout.addLayout(self.limit_line_box_1_layout)
        self.limit_layout.addLayout(self.limit_line_box_2_layout)
        
        
        layout1.addRow("Colonnes",self.tab_combobox)
        layout1.addRow("Limites",self.limit_layout)
        layout1.addRow("Label en abscisse",self.x_label_receiver)
        layout1.addRow("Label en ordonnée",self.y_label_receiver)
        layout1.addRow("Label des donnée",self.data_label_receiver)
        layout1.addRow("Titre",self.title_receiver)
        
        self.tab_groupBox.setLayout(layout1)
        
        layout2 = QGridLayout()
        #color
        color_push_button_layout = QFormLayout()
        color_push_button_layout.addRow("Couleur",self.color_push_button)
        layout2.addLayout(color_push_button_layout,0,0,1,3)
        
        # bar width
        line_width_box_layout = QFormLayout()
        line_width_box_layout.addRow("Taille des lignes",self.line_width_box)
        layout2.addLayout(line_width_box_layout,0,3,1,3)
        
        #Orientation
        markers_combobox_layout = QFormLayout()
        markers_combobox_layout.addRow("Markers",self.markers_combobox)
        layout2.addLayout(markers_combobox_layout,1,0,1,6)
        
        
        
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
        
        self.setGeometry(200,200,650,400)
        
        
        self.final_button.clicked.connect(self.terminer)
        
    def terminer(self):
        if self.new_radiobutton.isChecked():
            self.send_info.emit([2,[get_tab_pos(self.tab_combobox.currentText())],
                                               [self.title_receiver.text(),
                                                self.data_label_receiver.text(),
                                                self.x_label_receiver.text(),
                                                self.y_label_receiver.text()],
                    
                                               [self.color_push_button.color_(),
                                                self.markers_combobox.currentText(),
                                                self.line_width_box.text()],
                                               [self.limit_line_box_1.text(),
                                                self.limit_line_box_2.text()]])
        else:
            self.send_info.emit([1,[get_tab_pos(self.tab_combobox.currentText())],
                                               [self.title_receiver.text(),
                                                self.data_label_receiver.text(),
                                                self.x_label_receiver.text(),
                                                self.y_label_receiver.text()],
                                             
                                                [self.color_push_button.color_(),
                                                self.markers_combobox.currentText(),
                                                self.line_width_box.text()],
                                               [self.limit_line_box_1.text(),
                                                self.limit_line_box_2.text()]])
            
        
class ScatterInfoReceiver_2(QWidget):
    send_info = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.tab_combobox1 = QComboBox()
        self.tab_combobox2 = QComboBox()
        self.tab_groupBox = QGroupBox("Colonnes et labels")
        self.x_label_receiver = QLineEdit()
        self.y_label_receiver = QLineEdit()
        self.data_label_receiver = QLineEdit()
        self.title_receiver = QLineEdit()
        
        # Pour la première colonne
        self.limit_line_box_1 = QSpinBox()
        self.limit_line_box_1.setRange(1,1000000000)
        self.limit_line_box_1_layout = QFormLayout()
        
        self.limit_line_box_2 = QSpinBox()
        self.limit_line_box_2.setRange(1,1000000000)
        self.limit_line_box_2_layout = QFormLayout()
        self.limit_layout = QHBoxLayout()
        
        # Pour la second colonne
        self.limit_line_box_1_ = QSpinBox()
        self.limit_line_box_1_.setRange(1,1000000000)
        self.limit_line_box_1_layout_ = QFormLayout()
        
        self.limit_line_box_2_ = QSpinBox()
        self.limit_line_box_2_.setRange(1,1000000000)
        self.limit_line_box_2_layout_ = QFormLayout()
        self.limit_layout_ = QHBoxLayout()
        
        
        self.other_groupBox = QGroupBox("Couleurs et Autres")
        self.new_radiobutton = QRadioButton("Nouveau")
        self.final_button = QPushButton("Terminer")
        self.markers_combobox = QComboBox()
        self.color_push_button = ColorButton()

        self.line_width_box = QSpinBox()
        self.marker_size_box = QSpinBox()
        
        self.layout_principale = QVBoxLayout()
        
        self.init_UI()
        
        
    def init_UI(self):
        # Setting
        self.tab_combobox1.addItems(TABLES_NAMES)
        self.tab_combobox2.addItems(TABLES_NAMES)
        self.markers_combobox.addItems(markers)
        self.line_width_box.setValue(0)
        layout1 = QFormLayout()
        
        
        # Les limites
        
        self.limit_line_box_1_layout.addRow("Début",self.limit_line_box_1)
        self.limit_line_box_2_layout.addRow("Fin",self.limit_line_box_2)
        self.limit_layout.addLayout(self.limit_line_box_1_layout)
        self.limit_layout.addLayout(self.limit_line_box_2_layout)
        
        self.limit_line_box_1_layout_.addRow("Début",self.limit_line_box_1_)
        self.limit_line_box_2_layout_.addRow("Fin",self.limit_line_box_2_)
        self.limit_layout_.addLayout(self.limit_line_box_1_layout_)
        self.limit_layout_.addLayout(self.limit_line_box_2_layout_)
        
        tab_layout = QHBoxLayout()
        tab_layout.addWidget(self.tab_combobox1)
        tab_layout.addWidget(self.tab_combobox2)
        
        limit_final_layout = QHBoxLayout()
        limit_final_layout.addLayout(self.limit_layout)
        limit_final_layout.addLayout(self.limit_layout_)
        
        layout1.addRow("Colonnes",tab_layout)
        layout1.addRow("Limites",limit_final_layout)
        layout1.addRow("Label en abscisse",self.x_label_receiver)
        layout1.addRow("Label en ordonnée",self.y_label_receiver)
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
        
        #Orientation
        markers_combobox_layout = QFormLayout()
        markers_combobox_layout.addRow("Markers",self.markers_combobox)
        layout2.addLayout(markers_combobox_layout,1,0,1,6)
        
        
        
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
        
        self.setGeometry(200,200,650,400)
        
        
        self.final_button.clicked.connect(self.terminer)
        
    def terminer(self):
        if self.new_radiobutton.isChecked():
            
            self.send_info.emit([2,[get_tab_pos(self.tab_combobox1.currentText()),
                                get_tab_pos(self.tab_combobox2.currentText())],
                                               [self.title_receiver.text(),
                                                self.data_label_receiver.text(),
                                                self.x_label_receiver.text(),
                                                self.y_label_receiver.text()],
                                             
                                               
                                                [self.color_push_button.color_(),
                                                self.markers_combobox.currentText(),
                                                self.line_width_box.text()],
                                                [[self.limit_line_box_1.text(),
                                                  self.limit_line_box_2.text()],
                                                 [self.limit_line_box_1_.text(),
                                                  self.limit_line_box_2_.text()]]])
        else:
             self.send_info.emit([1,[get_tab_pos(self.tab_combobox1.currentText()),
                                get_tab_pos(self.tab_combobox2.currentText())],
                                               [self.title_receiver.text(),
                                                self.data_label_receiver.text(),
                                                self.x_label_receiver.text(),
                                                self.y_label_receiver.text()],
                                             
                                                [self.color_push_button.color_(),
                                                self.markers_combobox.currentText(),
                                                self.line_width_box.text()],
                                                [[self.limit_line_box_1.text(),
                                                  self.limit_line_box_2.text()],
                                                 [self.limit_line_box_1_.text(),
                                                  self.limit_line_box_2_.text()]]])
            
        
        
        
        
class ScatterInfoReceiver(QWidget):
    def __init__(self):
        super().__init__()
        
        self.one_list_data_receiver = ScatterInfoReceiver_1()
        self.double_list_data_receiver = ScatterInfoReceiver_2()
        self.tab_widget = QTabWidget()
        self.datas = list()
        
        
        self.init_UI()
        
    def init_UI(self):
        self.setWindowIcon(QIcon("analys.png"))
        self.setWindowTitle("Fenêtre de renseignement du nuage de points")
        
        self.tab_widget.addTab(self.one_list_data_receiver,"Une Liste")
        self.tab_widget.addTab(self.double_list_data_receiver,"Deux liste")
        
        self.layout_principale = QVBoxLayout()
        self.layout_principale.addWidget(self.tab_widget)
        
        self.setGeometry(150,150,540,450)
        
        # Printer 
        self.scatter_printer = ScatterPrinter()
        self.a = ScatterPrinter()
        
        self.one_list_data_receiver.send_info.connect(self.bar)
        self.double_list_data_receiver.send_info.connect(self.bar)
        
        self.setLayout(self.layout_principale)
        
    def bar(self,information):
        if information[0] == 1:
            self.scatter_printer.scatter(information)
            self.scatter_printer.show()
            
        elif information[0] == 2:
            information[0] = 1
            self.a.clear()
            self.a.set_datas(self.datas)
            self.a.scatter(information)
            self.a.show()
            
            """
            code = ""
            code =  "a"+str(I)+ " = ScatterPrinter() \n"
            code = code + "a"+str(I)+".set_datas(self.datas)\n"
            code = code + "a"+str(I)+".scatter(information)\n"
            code = code + "a"+str(I)+".show()\n"
            exec(compile(code,"débug.txt","exec"))
            """
        
    def set_printer_data(self,data):
        self.datas = data
        self.scatter_printer.set_datas(data)
        
        
        
        
        
        
    
            
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ScatterInfoReceiver()
    w.show()
    sys.exit(app.exec())
        
        
    