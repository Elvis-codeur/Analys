# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:38:32 2020

@author: elvis
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import urllib.request
import urllib3
import shutil

class html_widget(QWidget):
    finish = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        self.url_line_edit = QLineEdit()
        self.finish_button = QPushButton("Terminer")
        self.save_line_edit = QLineEdit()
        self.save_button = QPushButton("...")
        self.url_group_box = QGroupBox("Internet")
        self.save_group_box = QGroupBox("Enregistrer")
        
        self.data = str()
        
        self.init_UI()
        
    def get_directory(self):
        file_name = QFileDialog.getExistingDirectory(self)
        self.save_line_edit.setText(str(file_name))
        
        
    def init_UI(self):
        url_form_layout = QFormLayout()
        url_form_layout.addRow("Url",self.url_line_edit)
        self.url_group_box.setLayout(url_form_layout)
        
        save_form_layout = QFormLayout()
        
        save_layout = QHBoxLayout()
        
        save_form_layout.addRow("Dossier",self.save_line_edit)
        save_layout.addLayout(save_form_layout)
        save_layout.addWidget(self.save_button)
        
        self.save_group_box.setLayout(save_layout)
        
        self.setMinimumSize(QSize(500,100))
        
        self.layout_principale = QVBoxLayout()
        self.layout_principale.addWidget(self.url_group_box)
        self.layout_principale.addWidget(self.save_group_box)
        self.layout_principale.addWidget(self.finish_button)
        self.setLayout(self.layout_principale)
        
        self.finish_button.clicked.connect(self.finish)
        self.save_button.clicked.connect(self.get_directory)
        
        
    def get_filename(self,text):
        i = len(text)-1
        while i > 0:
            if text[i] == "/":
                return text[i+1:len(text)]
            i = i-1
                
        

    def finish(self):
        try:
            
            url = self.url_line_edit.text()
           
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            a = 0
            file_name = self.get_filename(url)
            if self.save_line_edit.text() == "":    
                a = urllib.request.urlretrieve(url,file_name)
            else:
                a = urllib.request.urlretrieve(url,self.save_line_edit.text()+"/"+file_name)
                
                
            QMessageBox.information(self,"Information","Teminé") 
        except Exception as e:
            QMessageBox.information(self,"Information",str(e))            
            
        if self.save_line_edit.text() != "":
            f = open(self.url_line_edit.text(),"w")
            f.write(self.data)
            f.close()
            self.finish.emit()
        else:
            self.finish.emit()
            
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = html_widget()
    w.show()
    print(w.get_filename("https://ec.ccm2.net/codes-sources.commentcamarche.net/source/download/103163-1995731-pierre-feuille-ciseaux.zip"))
    sys.exit(app.exec())
        

        

 
"""
 
            url = "http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId=4S18"
            # url = "http://python.developpez.com/outils/PythonZope/images/cpython.gif"
 
 
            http = urllib3.PoolManager()
            with http.request('GET', url, preload_content=False) as r, open("image.gif", 'wb') as sortie:    
                shutil.copyfileobj(r, sortie)
                
                
                https://ec.ccm2.net/codes-sources.commentcamarche.net/source/download/103163-1995731-pierre-feuille-ciseaux.zip
"""

# now, with the below headers, we defined ourselves as a simpleton who is
# still using internet explorer.
#url = "http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId=4S18"
#req = urllib.request.Request(url, headers = headers)
