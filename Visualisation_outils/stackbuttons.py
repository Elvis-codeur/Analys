# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:22:14 2020

@author: Elvis
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Visualisation_outils.textreceiver import *

class StackButton(QPushButton):
    def __init__(self,name = str):
        self.name = name
        self.color = "yellow"
        self.data = tuple()
        super().__init__()
        self.data_receiver = StackTextReceiver()
        
        self.clicked.connect(self.text_receiver_show)
        self.data_receiver.finish.connect(self.set_data)
        
        self.data_receiver.finish.connect(self.set_data)
        
        self.setText(self.name)
        
    def set_data(self):
        self.data = self.data_receiver.data()
        self.color = self.data[2]
        
    def get_data(self):
        return self.data
        
    def text_receiver_show(self):
        self.data_receiver.show()
        
    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(self.color))
        size = self.size()
        painter.drawRect(0,0,size.width(),size.height())
        
        painter.setPen(QPen(QColor(0,0,0)))
        painter.setBrush(QBrush(QColor(0,0,0)))
        size = self.size()
        font = QFont("New Courrier")
        font.setPixelSize(20)
        painter.setFont(font)
        painter.drawText(0, 0, size.width(),size.height(),1,self.name)
        
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = StackButton("Tab_A")
    w.show()
    sys.exit(app.exec())
        