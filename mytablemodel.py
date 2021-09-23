# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyTableModel(QStandardItemModel):
    row_m_modified = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.set_headers()
        self.itemChanged.connect(self.increase_row)
       
        
        for i in range(10):
            a = list()
            for u in range(26):
                a.append(QStandardItem(""))
            self.insertRow(i,a)
            a.clear()
    def set_headers(self):
        headers = ["A","B","C","D","E","F","G",
                   "H","I","J","K","L","M",
                   "N","O","P","Q","R","S","T","U",
                   "V","W","X","Y","Z"]
        for i in range(len(headers)):
            self.setHorizontalHeaderItem(i,QStandardItem("Tab_"+headers[i]))
            
    def m_append_row(self):
        a = list()
        for i in range(26):
            a.append(QStandardItem(""))
        return a
            
    def increase_row(self,item):
        if item.row() == (self.rowCount() -1):
            self.appendRow(self.m_append_row())
        
            
    def clear(self):
        self.clear()
        self.set_headers()
        
        