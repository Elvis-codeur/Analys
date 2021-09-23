# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 02:02:59 2021

@author: Elvis
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class VisualisationChooseButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.image_name = ""
        self.painter = QPainter()
        #self.manage()
        
        
    def set_image(self,name):
        self.image_name = name
        
        info  = QFileInfo(self.image_name)
        
        if info.exists():
            
            self.reader =  QImageReader(self.image_name)
            self.image = self.reader.read()
            #print(self.image.size().height())
            self.setMinimumSize(QSize(340,340))
            #self.setGeometry(150,150,self.image.size().width(),self.image.size().height())
        else:
            print("Fichier introuvable")
        
        
    def paintEvent(self,event):
        pen = QPen(QColor(200,56,128))
        brush = QBrush(QColor(100,100,0))
        
        self.painter.begin(self)
        self.painter.setPen(pen)
        self.painter.setBrush(brush)
        #self.painter.drawRect(QRect(0,0,self.size().width(),self.size().height()))
        self.painter.drawImage(QRectF(10,10,300,300),self.image)
        self.painter.end()
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = VisualisationChooseButton()
    w.set_image("imgs/circulaire.jpg")
    w.show()
    sys.exit(app.exec())
        
        