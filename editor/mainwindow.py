# -*- coding: utf-8 -*-
"""
Created on Mon May 31 07:50:57 2021

@author: Elvis
"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from editor.editor import *
from State.global_state import SOFTWARE_VERSION_NAME



class EditorMainWindow(QMainWindow):
    mainwindow_send_code = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle(SOFTWARE_VERSION_NAME+" Code Editor")
        self.editor_list = []
        self.editor = Editor()
        self.tabwidget = QTabWidget()
        self.editor_list.append(self.editor)
        
        
        self.new = QAction(QIcon("new.png"),"Nouveau")
        self.open = QAction(QIcon("open.png"),"Ouvrir")
        self.save = QAction(QIcon("save.png"),"Sauvegarder")
        self.play = QAction(QIcon("play.png"),"Exécuter")
        
        self.editor_list.append(self.editor)
        
        self.tabwidget.addTab(self.editor,self.editor.filename)
        
        self.play.triggered.connect(self.editor.execute)
        self.save.triggered.connect(self.editor.save)
        self.open.triggered.connect(self.editor.open_)
        
        self.editor.editor_send_code.connect(self.mainwindow_send_code)
        
        
        self.init_UI()
        
    def addeditor(self):
        editor = Editor()
        self.editor_list.append(editor)
        
        self.tabwidget.addTab(editor,editor.filename)
        
        self.play.triggered.connect(editor.execute)
        self.save.triggered.connect(editor.save)
        self.open.triggered.connect(editor.open_)
        
        editor.editor_send_code.connect(self.mainwindow_send_code)
        
    def addeditor_whithcode(self,code):
        editor = Editor()
        self.editor_list.append(editor)
        editor.code = code
        editor.setText(code)
        
        self.tabwidget.addTab(editor,editor.filename)
        
        self.play.triggered.connect(editor.execute)
        self.save.triggered.connect(editor.save)
        self.open.triggered.connect(editor.open_)
        
        editor.editor_send_code.connect(self.mainwindow_send_code)
        
        
    def set_error_message(self,message):
        self.error_log.setText(self.error_log.toPlainText()+"\n\n\n>>>   "+message)
        
    def init_UI(self):
        self.menubar = self.menuBar()
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)
        
        
        self.new.setToolTip("Nouveau")
        self.new.setShortcut(QKeySequence("Ctrl+N"))
        
        
        self.open.setToolTip("Ouvrir")
        self.open.setShortcut(QKeySequence("Ctrl+O"))
        
        
        self.save.setToolTip("Sauvegarder")
        self.save.setShortcut(QKeySequence("Ctrl+S"))
        
        
        self.play.setToolTip("Exécuter")
        self.play.setShortcut(QKeySequence("Ctrl+P"))
        
        self.toolbar.addAction(self.new)
        self.toolbar.addAction(self.open)
        self.toolbar.addAction(self.save)
        self.toolbar.addAction(self.play)
        self.toolbar.setIconSize(QSize(60,60))
        
        self.mainmenu = QMenu("Fichier")
        self.menubar.addMenu(self.mainmenu)
        self.mainmenu.addAction(self.new)
        self.mainmenu.addAction(self.open)
        self.mainmenu.addAction(self.save)
        self.mainmenu.addAction(self.play)
        
        
        widget = QWidget()
        layout = QVBoxLayout()
        self.error_log = QTextEdit()
        
        layout.addWidget(self.tabwidget)
        layout.addWidget(self.error_log)
        widget.setLayout(layout)
        self.setCentralWidget(self.tabwidget)
        
        self.dockwidget = QDockWidget("Error Log")
        self.dockwidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.dockwidget.setWidget(self.error_log)
        self.addDockWidget(Qt.BottomDockWidgetArea,self.dockwidget)        
        
        self.new.triggered.connect(self.addeditor)
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = EditorMainWindow()
    w.show()
    sys.exit(app.exec_())