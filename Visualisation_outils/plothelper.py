# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:55:14 2020

@author: elvis
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import PyQt5.Qt as Qt
import sys

from Visualisation_outils.buttons import *
line_styles = ['-', '--', '-.', ':', 'None', 'solid', 'dashed', 'dashdot', 'dotted']
class PlotingHelp(QWidget):
    send_info = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.x_groupbox = QGroupBox("Abscisse")
        self.x_rotation_slider = QSlider(Qt.Horizontal)
        self.x_color_button = ColorButton()
        
        self.y_groupbox = QGroupBox("Ordonnée")
        self.y_rotation_slider = QSlider(Qt.Horizontal)
        self.y_color_button = ColorButton()
        
        self.left_slider = QSlider(Qt.Horizontal)
        self.right_slider = QSlider(Qt.Horizontal)
        self.top_slider = QSlider(Qt.Horizontal)
        self.bottom_slider = QSlider(Qt.Horizontal)
        
        self.adjust_groupbox = QGroupBox("Limites")
        
        self.grid_groupBox = QGroupBox("Grille")
        self.grid_state = QRadioButton("Oui")
        self.grid_color_button = ColorButton()
        self.grid_lines_style_combobox = QComboBox()
        self.grid_line_width_slider = QSlider(Qt.Horizontal)
        
        self.init_UI()
        
    def send_data_1(self):
        self.send_data(0)
        
    def send_data(self,value):
        if self.grid_state.isChecked():    
            self.send_info.emit([2,
                                 [self.grid_lines_style_combobox.currentText(),
                                  self.grid_line_width_slider.value(),
                                  self.grid_color_button.color_()],
                                 
                                 [self.right_slider.value()/100,
                                  self.left_slider.value()/100,
                                  self.top_slider.value()/100,
                                  self.bottom_slider.value()/100],
                                 
                                 [self.x_rotation_slider.value(),
                                  self.y_rotation_slider.value(),
                                  self.x_color_button.color_(),
                                  self.y_color_button.color_()]])
        else:
            self.send_info.emit([1,
                                 [self.grid_lines_style_combobox.currentText(),
                                  self.grid_line_width_slider.value()],
                                 
                                 [self.right_slider.value()/100,
                                  self.left_slider.value()/100,
                                  self.top_slider.value()/100,
                                  self.bottom_slider.value()/100],
                                 
                                 [self.x_rotation_slider.value(),
                                  self.y_rotation_slider.value(),
                                  self.x_color_button.color_(),
                                  self.y_color_button.color_()]])
            
        
    def init_UI(self):
        ## SETTING ###################
        self.x_rotation_slider.setRange(0,180)
        self.y_rotation_slider.setRange(0,180)
        self.left_slider.setRange(10,100)
        self.right_slider.setRange(10,100)
        self.right_slider.setValue(95)
        self.top_slider.setRange(10,100)
        self.top_slider.setValue(95)
        self.bottom_slider.setRange(10,100)
        self.grid_line_width_slider.setRange(1,25)
        self.grid_lines_style_combobox.addItems(line_styles)
        
        ##############################
        
        # CONNECTIONS #
        self.x_rotation_slider.valueChanged.connect(self.send_data)
        self.y_rotation_slider.valueChanged.connect(self.send_data)
        self.x_color_button.color_choosed.connect(self.send_data)
        self.y_color_button.color_choosed.connect(self.send_data)
        self.left_slider.valueChanged.connect(self.send_data)
        self.right_slider.valueChanged.connect(self.send_data)
        self.top_slider.valueChanged.connect(self.send_data)
        self.bottom_slider.valueChanged.connect(self.send_data)
        self.grid_line_width_slider.valueChanged.connect(self.send_data)
        self.grid_lines_style_combobox.currentTextChanged.connect(self.send_data)
        self.grid_color_button.color_choosed.connect(self.send_data)
        self.grid_state.pressed.connect(self.send_data_1)
        ###############
        
        self.layout_principal = QVBoxLayout()
        
        # ABSCISSE
        x_rotation_slider_layout = QFormLayout()
        x_rotation_slider_layout.addRow("Rotation des labels en abscisse",self.x_rotation_slider)
        x_color_button_layout = QFormLayout()
        x_color_button_layout.addRow("Couleur",self.x_color_button)
        
        x_group_layout = QVBoxLayout()
        x_group_layout.addLayout(x_rotation_slider_layout)
        x_group_layout.addLayout(x_color_button_layout)
        self.x_groupbox.setLayout(x_group_layout)
        
        #ORDONNEE
        y_rotation_slider_layout = QFormLayout()
        y_rotation_slider_layout.addRow("Rotation des labels en ordonée",self.y_rotation_slider)
        y_color_button_layout = QFormLayout()
        y_color_button_layout.addRow("Couleur",self.y_color_button)
    
        y_group_layout = QVBoxLayout()
        y_group_layout.addLayout(y_rotation_slider_layout)
        y_group_layout.addLayout(y_color_button_layout)
        self.y_groupbox.setLayout(y_group_layout)
        
        # LIMITES 
        
        left_slider_layout = QFormLayout()
        left_slider_layout.addRow("Limite à gauche : ",self.left_slider)
        
        right_slider_layout = QFormLayout()
        right_slider_layout.addRow("Limite à droite : ",self.right_slider)
        
        top_slider_layout = QFormLayout()
        top_slider_layout.addRow("Limite en haut : ",self.top_slider)
        
        bottom_slider_layout = QFormLayout()
        bottom_slider_layout.addRow("Limite en bas : ",self.bottom_slider)
        
        adjust_groupbox_layout = QVBoxLayout()
        adjust_groupbox_layout.addLayout(left_slider_layout)
        adjust_groupbox_layout.addLayout(right_slider_layout)
        adjust_groupbox_layout.addLayout(top_slider_layout)
        adjust_groupbox_layout.addLayout(bottom_slider_layout)
        
        self.adjust_groupbox.setLayout(adjust_groupbox_layout)
        
        # GRILLE
        grid_color_button_layout = QFormLayout()
        grid_color_button_layout.addRow("Couleur",self.grid_color_button)
        
        # STYLE 
        grid_lines_style_combobox_layout = QFormLayout()
        grid_lines_style_combobox_layout.addRow("Style",self.grid_lines_style_combobox)
        # WIDTH
        grid_line_width_slider_layout = QFormLayout()
        grid_line_width_slider_layout.addRow("Epaisseur",self.grid_line_width_slider)
        
        
        grid_groupBox_layout = QVBoxLayout()
        grid_groupBox_layout.addWidget(self.grid_state)
        grid_groupBox_layout.addLayout(grid_color_button_layout)
        grid_groupBox_layout.addLayout(grid_lines_style_combobox_layout)
        grid_groupBox_layout.addLayout(grid_line_width_slider_layout)
        self.grid_groupBox.setLayout(grid_groupBox_layout)
        
        
        self.layout_principal.addWidget(self.x_groupbox)
        self.layout_principal.addWidget(self.y_groupbox)
        self.layout_principal.addWidget(self.adjust_groupbox)
        self.layout_principal.addWidget(self.grid_groupBox)

        self.setLayout(self.layout_principal)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = PlotingHelp()
    a.show()
    sys.exit(app.exec())        
        
        