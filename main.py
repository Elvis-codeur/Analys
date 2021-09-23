# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 19:59:16 2020

@author: Elvis
"""

    
from fenprincipale import fenPrincipale
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

if __name__ == "__main__":
    #print(sys.argv)
    if len(sys.argv) > 1:
        
        app = QApplication(sys.argv)
        fen = fenPrincipale()
        fen.open(argv[1])
        fen.showMaximized()
        sys.exit(app.exec())
        
    else:
        app = QApplication(sys.argv)
        fen = fenPrincipale()
        #fen.open("x.wdata")
        fen.showMaximized()
        sys.exit(app.exec())
