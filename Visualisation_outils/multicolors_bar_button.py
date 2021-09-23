# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 15:52:12 2021

@author: Elvis
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .multicolors_bar_info_receiver import *
import sys
        
class MultipleColorBarButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.info_receiver = MultipleColorsBarInfoReceiver()
        self.data = list()
        self.color = "yellow"
        self.manage()
        
    def set_data(self,data):
        print(data)
        self.data = data
        self.color = data[1][0]
        
    def get_data(self):
        return self.data
        
    def manage(self):
        self.clicked.connect(self.info_receiver.show)
        self.info_receiver.data.connect(self.set_data)
         
    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(self.color))
        size = self.size()
        painter.drawRect(0,0,size.width(),size.height())
        painter.end()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MultipleColorBarButton()
    w.show()
    sys.exit(app.exec())