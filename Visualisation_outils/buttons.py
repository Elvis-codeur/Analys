# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 00:37:43 2020

@author: elvis
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class ColorButton(QPushButton):
    color_choosed = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.color = "yellow"
        
        self.clicked.connect(self.get_color)
        
    def get_color(self):
        f = QColorDialog(self)
        
        color = f.getColor()
        self.color = color.name()
        self.color_choosed.emit(self.color)
        
    def color_(self):
        return self.color
        
    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(self.color))
        size = self.size()
        painter.drawRect(0,0,size.width(),size.height())
        painter.end()
        
class FontButton(QPushButton):
    font_choosed = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.font = "Consolas"
        self.font_size = 20
        self.clicked.connect(self.get_font)
        self.setGeometry(200,200,200,200)
        
    def get_font(self):
        f = QFontDialog(self)
        
        font = f.getFont(self)[0]
        self.font = font.family()
        self.font_size = font.pointSize()
        #print((self.font,self.font_size))
        self.font_choosed.emit(self.font)
        
    def font_(self):
        return self.font
    def font_size_(self):
        return self.font_size
        
    def paintEvent(self,event):
        
        painter = QPainter()
        painter.begin(self)
        f = QFont(self.font)
        f.setPointSize(self.font_size)
        painter.setFont(f)
        size = self.size()
        painter.drawText(0,0,size.width(),size.height(),1,self.font)
        painter.end()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ColorButton()
    w.show()
    sys.exit(app.exec())
        