# -*- coding: utf-8 -*-
"""
Created on Mon May 31 07:37:06 2021

@author: Elvis
"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from editor.surligneur import Surligneur

class Editor(QTextEdit):
    nameChanged = pyqtSignal(str)
    editor_send_code = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.surligneur = Surligneur(self.document())
        
        self.code = ""
        self.filename = "unknown"
        
        self.init_UI()
    
        
    def init_UI(self):
        font = QFont("DejaVu Sans Mono")
        font.setPixelSize(15)
        self.setFont(font)
        self.textChanged.connect(self.update_code)
        
    def update_code(self):
        self.code = self.document().toPlainText()
        
    def save(self):
        if self.hasFocus():
            self.code = self.document().toPlainText()
            f = QFileDialog(self)
            name = f.getSaveFileName(self)
            if(len(name) >1):
                name = name[0]
                
                file = open(name,"w",encoding = "utf-8")
                file.write(self.code)
                file.close()
                
    def open_(self):
        if self.hasFocus():
            
            f = QFileDialog(self)
            name = f.getOpenFileName(self)
            if(len(name) > 1):
                name = name[0]
                file = open(name,"r",encoding = "utf-8")
                self.code = file.read()
                self.setText(self.code)
                file.close()
                self.filename = QFileInfo(name[0]).baseName()
                self.nameChanged.emit(self.filename)
        
         
    def execute(self):
        compiled = ""
        comp_error = ""
        executed = ""
        if self.hasFocus():
            self.code = self.document().toPlainText()
            self.editor_send_code.emit(self.code)
            print("editor ok")            
            """
            self.code = self.document().toPlainText()
            #print(code)
            try:
                compiled = compile(self.code,"error.txt","exec")
            except:
                print("error")
            
            try:
                executed = exec(compiled)
            except:
                print("error")
            """
                    
                
                
            
            
                
                    
                    
                
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Editor()
    w.show()
    sys.exit(app.exec_())