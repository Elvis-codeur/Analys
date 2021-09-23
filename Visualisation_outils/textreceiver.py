#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:11:34 2020

@author: elvis
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

from Visualisation_outils.buttons import *
from Visualisation_outils.m_parser import *

class TextReceiver(QWidget):
    finish = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.text_receiver = QLineEdit()
        self.font_receiver = FontButton()
        self.color_receiver = ColorButton()
        self.button_finish = QPushButton("Terminer")
        self.layout_principale = QVBoxLayout()
        
        self.init_UI()
        self.button_finish.clicked.connect(self.finish)

    def get_data(self):
        
        return (self.font_receiver.font_(),
                self.color_receiver.color_(),
                self.font_receiver.font_size_(),
                self.text_receiver.text())
        
    def init_UI(self):
        text_receiver_layout = QFormLayout()
        text_receiver_layout.addRow("Texte",self.text_receiver)
        
        font_and_color_layout = QHBoxLayout()
        
        font_receiver_layout = QFormLayout()
        font_receiver_layout.addRow("POlice",self.font_receiver)
        
        color_receiver_layout = QFormLayout()
        color_receiver_layout.addRow("Couleur",self.color_receiver)
        
        font_and_color_layout.addLayout(color_receiver_layout)
        font_and_color_layout.addLayout(font_receiver_layout)
        
        self.layout_principale.addLayout(text_receiver_layout)
        self.layout_principale.addLayout(font_and_color_layout)
        self.layout_principale.addWidget(self.button_finish)
        
        self.setLayout(self.layout_principale)
        
        
        
class FinalTextReceiver(QWidget):
    send_info = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.text_widget = TextReceiver()
        self.annoation_widget = TextReceiver()
        
        self.tab_widget = QTabWidget()
        
        self.init_UI()
        self.text_widget.finish.connect(self.send_data_t)
        self.annoation_widget.finish.connect(self.send_data_a)
        
    def send_data_t(self):
        self.send_info.emit([1,list(self.text_widget.get_data())])
        self.close()
        
    def send_data_a(self):
        self.send_info.emit([2,
                             list(self.annoation_widget.get_data()),
                             [self.x_receiver.text(),
                              self.y_receiver.text()]])
        self.close()
        
        
    def init_UI(self):     
        self.layout_principale = QVBoxLayout()
        w = QWidget()
        self.x_receiver = QLineEdit()
        self.y_receiver = QLineEdit()
        
        self.x_receiver.setText("0.9")
        self.y_receiver.setText("0.9")
        
        x_receiver_layout = QFormLayout()
        x_receiver_layout.addRow("Abscisse",self.x_receiver)
        
        y_receiver_layout = QFormLayout()
        y_receiver_layout.addRow("Ordonnée",self.y_receiver)
        
        receiver_layout = QHBoxLayout()
        receiver_layout.addLayout(x_receiver_layout)
        receiver_layout.addLayout(y_receiver_layout)
        
        w_layout = QVBoxLayout()
        w_layout.addWidget(self.annoation_widget)
        w_layout.addLayout(receiver_layout)
        
        w.setLayout(w_layout)
        
        
        self.tab_widget.addTab(self.text_widget,"Texte")
        self.tab_widget.addTab(w,"Annotation")
        
        self.layout_principale.addWidget(self.tab_widget)
        self.setLayout(self.layout_principale)
        
        
class StackTextReceiver(QWidget):
    finish = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.text = ""
        self.font = ()
        self.color = "yellow"
        self.text_receiver = QLineEdit()
        self.begin_receiver = QSpinBox()
        self.end_receiver = QSpinBox()
        self.color_receiver = ColorButton()
        self.finish_button = QPushButton("Terminer")
        
        self.finish_button.clicked.connect(self.t)
        
        self.init_UI()
        
    def t(self):
        self.finish.emit()
        self.close()
        
    def init_UI(self):
        # Setting
        self.begin_receiver.setMaximum(10000000)
        self.begin_receiver.setMinimum(1)
        self.end_receiver.setMaximum(100000000)
        self.end_receiver.setMinimum(1)
        text_receiver_layout = QFormLayout()
        text_receiver_layout.addRow("Texte",self.text_receiver)
        color_receiver_layout = QFormLayout()
        color_receiver_layout.addRow("Couleur",self.color_receiver)
        
        limits_receiver_layout = QFormLayout()
        
        begin_layout = QFormLayout()
        begin_layout.addRow("Début",self.begin_receiver)
        
        end_layout = QFormLayout()
        end_layout.addRow("Fin",self.end_receiver)
        
        limits_layout = QHBoxLayout()
        limits_layout.addLayout(begin_layout)
        limits_layout.addLayout(end_layout)
        limits_receiver_layout.addRow("Limites",limits_layout)

        
        self.layout_principale = QVBoxLayout()
        self.layout_principale.addLayout(text_receiver_layout)
        self.layout_principale.addLayout(color_receiver_layout)
        self.layout_principale.addLayout(limits_receiver_layout)
        self.layout_principale.addWidget(self.finish_button)
        
        self.setLayout(self.layout_principale)
        
    def data(self):
        self.text = self.text_receiver.text()
        self.font = (int(self.begin_receiver.text()),int(self.end_receiver.text()))
        self.color = self.color_receiver.color_()
        
        return self.text,self.font,self.color
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = StackTextReceiver()
    w.show()
    sys.exit(app.exec())
        
        
        