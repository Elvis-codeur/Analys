# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:21:59 2021

@author: Elvis
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

class DocumentationShower(QWebEngineView):
    def __init__(self):
        super().__init__()
        
        self.text = str()
        
    def open(self,addresse):
        f = open(addresse,"r")
        self.text = f.read()
        self.setHtml(self.text)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = DocumentationShower()
    s = "D:\\ANALYS\\ANALYS 1.0.0\\French\\Analys\\documentation\\web work\\Analys\\Analys_visualisation_documentation\\visualisation_analys_documentation.html"
    a.open(s)
    a.show()
    sys.exit(app.exec())
    