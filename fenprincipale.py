# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:21:29 2020

@author: elvis
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from tableviewwidget import *

# Module personnel

from locals.datasfile import *
from Visualisation.plotinforeceiver import *
from Visualisation.barinforeceiver import *
from Visualisation.multicolors_bar_main_widget import *
from Visualisation.scatterinforeceiver import *
from Visualisation.stackinforeceiver import *
from Visualisation.pieinforeceiver import *
from Visualisation.multiplebarinforeceiver import *
from Visualisation.boxplotinforeceiver import *
from Visualisation.barinforeceiver3d import *
from Visualisation.multiplebarinforeceiver3d import *
from Visualisation_outils.general_view import *

from State.global_state import SOFTWARE_VERSION_NAME

#
class fenPrincipale(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.tableviewwidget = TableViewWidget()
        
        self.layoutPrincipale = QVBoxLayout()
        
        self.widgetPrincipal = QWidget()
        self.layoutPrincipale.addWidget(self.tableviewwidget)
        self.widgetPrincipal.setLayout(self.layoutPrincipale)
        self.setCentralWidget(self.widgetPrincipal)
        
        # LES WIDGETS DE RECEPTION D'INFORMATION
        self.plot_info = PlotInfoReceiver()
        self.bar_info = BarInfoReceiver()
        self.multicolor_bar_info = MulticolorsBarMainWidget()
        self.scatter_info = ScatterInfoReceiver()
        self.stack_info = StackInfoReceiver()
        self.pie_info = PieInfoReceiver()
        self.multiplebar_info = MultipleBarInfoReceiver()
        self.boxplot_info = BoxPlotInfoReceiver()
        self.bar3d_info = BarInfoReceiver_3d()
        self.multiplebar3d_info = MultipleBarInfoReceiver_3d()
        self.general_info = GeneralPrinter()
        
        
        self.init_UI()
        
    def open(self,text):
        self.tableviewwidget.open_file_(text)
        
    def closeEvent(self,event):
        self.plot_info.close()
        self.bar_info.close()
        self.stack_info.close()
        self.scatter_info.close()
        self.pie_info.close()
        self.multiplebar_info.close()
        self.boxplot_info.close()
        self.bar3d_info.close()
        self.multiplebar3d_info.close()
        self.general_info.close()
        self.multicolor_bar_info.close()
        self.tableviewwidget.codeWidget.close()
        
        
    def init_UI(self):
        # Setting
        self.setWindowTitle(SOFTWARE_VERSION_NAME)
        self.setWindowIcon(QIcon("analys.png"))
        # Les fichiers
        self.menuFichier = self.menuBar().addMenu("Fichier")
        
        self.AouvrirFichier = QAction(QIcon("open.png"),"Ouvrir un fichier")
        self.AouvrirFichier.setShortcut(QKeySequence("Ctrl+O"))
        self.menuFichier.addAction(self.AouvrirFichier)
        
        self.Acopier = QAction(QIcon("copy.png"),"Copier")
        self.Acopier.setShortcut(QKeySequence("Ctrl+c"))
        self.Acopier.triggered.connect(self.tableviewwidget.copy)
        self.menuFichier.addAction(self.Acopier)
        
        
        self.Aenregistrer = QAction(QIcon("save.png"),"Enregistrer comme")
        self.Aenregistrer.setShortcut(QKeySequence("Ctrl+Shift+S"))
        self.menuFichier.addAction(self.Aenregistrer)
        
        # Enrégistrement
        self.Aenregistrer.triggered.connect(self.tableviewwidget.save_as)
        
        # Les exportations
        self.menuExport = self.menuFichier.addMenu(QIcon("export.png"),"Exporter")
        self.menuExport.addAction("Exporter : cvs",self.tableviewwidget.csv_export)
        self.menuExport.addAction("Exporter : excel",self.tableviewwidget.excel_export)
        self.menuExport.addAction("Exporter : html",self.tableviewwidget.html_export)
        
        self.menuExport.addAction("Exporter vers une base de donnée existante ",self.tableviewwidget.get_table_name)
        self.menuExport.addAction("Créer une nouvelle base de donnée",self.tableviewwidget.get_table_name2)
        
        # La visualisation
        self.menuVisualisation = self.menuBar().addMenu("Visualisation")
        
        #PLot
        self.Aplot = QAction("Diagramme linéaire")
        self.menuVisualisation.addAction(self.Aplot)
        self.Aplot.triggered.connect(self.tableviewwidget.update_local_data)
        self.tableviewwidget.send_data.connect(self.plot_info.set_printer_data)
        self.Aplot.triggered.connect(self.plot_info.show)
        
        # Bar
        self.ABar = QAction("Diagramme à bandes")
        self.menuVisualisation.addAction(self.ABar)
        self.ABar.triggered.connect(self.tableviewwidget.update_local_data)
        self.tableviewwidget.send_data.connect(self.bar_info.set_printer_data)
        self.ABar.triggered.connect(self.bar_info.show)
        
        # Multiplecolor
        self.Amulticolorbar = QAction("Diagramme à bandes multicolores")
        self.menuVisualisation.addAction(self.Amulticolorbar)
        self.Amulticolorbar.triggered.connect(self.tableviewwidget.update_local_data)
        self.tableviewwidget.send_data.connect(self.multicolor_bar_info.set_printer_data)
        self.Amulticolorbar.triggered.connect(self.multicolor_bar_info.show)
        
        # Scatter
        self.AScatter = QAction("Nuages de points")
        self.menuVisualisation.addAction(self.AScatter)
        self.AScatter.triggered.connect(self.tableviewwidget.update_local_data)
        self.tableviewwidget.send_data.connect(self.scatter_info.set_printer_data)
        self.AScatter.triggered.connect(self.scatter_info.show)
        # Stack 
        self.AStack = QAction("Diagramme à couche")
        self.menuVisualisation.addAction(self.AStack)
        self.AStack.triggered.connect(self.tableviewwidget.update_local_data)
        self.tableviewwidget.send_data.connect(self.stack_info.set_printer_data)
        self.AStack.triggered.connect(self.stack_info.show)
        
        # Pie
        self.APie = QAction("Diagramme circulaire")
        self.menuVisualisation.addAction(self.APie)
        self.APie.triggered.connect(self.tableviewwidget.update_local_data)
        self.tableviewwidget.send_data.connect(self.pie_info.set_printer_data)
        self.APie.triggered.connect(self.pie_info.show)
        
        # Multiplebar 
        self.AmBar = QAction("Diagramme à bandes multiples")
        self.menuVisualisation.addAction(self.AmBar)
        self.AmBar.triggered.connect(self.tableviewwidget.update_local_data)
        self.tableviewwidget.send_data.connect(self.multiplebar_info.set_printer_data)
        self.AmBar.triggered.connect(self.multiplebar_info.show)
        
        # Boxplot
        self.ABoxplot = QAction("Diagramme à moustache")
        self.menuVisualisation.addAction(self.ABoxplot)
        self.ABoxplot.triggered.connect(self.tableviewwidget.update_local_data)
        self.tableviewwidget.send_data.connect(self.boxplot_info.set_printer_data)
        self.ABoxplot.triggered.connect(self.boxplot_info.show)
        
        # Bar3d
        self.ABar3d = QAction("Diagramme à bandes en 3D")
        self.menuVisualisation.addAction(self.ABar3d)
        self.ABar3d.triggered.connect(self.tableviewwidget.update_local_data)
        self.tableviewwidget.send_data.connect(self.bar3d_info.set_printer_data)
        self.ABar3d.triggered.connect(self.bar3d_info.show)
        
        # Multiplebar 
        self.AmBar3d = QAction("Diagramme à bandes multiple en 3D")
        self.menuVisualisation.addAction(self.AmBar3d)
        self.AmBar3d.triggered.connect(self.tableviewwidget.update_local_data)
        self.tableviewwidget.send_data.connect(self.multiplebar3d_info.set_printer_data)
        self.AmBar3d.triggered.connect(self.multiplebar3d_info.show)
        
        
        # Multiplebar 
        """
        self.generalA = QAction("Graphique Generalisé")
        self.menuVisualisation.addAction(self.generalA)
        self.generalA.triggered.connect(self.tableviewwidget.update_local_data)
        self.tableviewwidget.send_data.connect(self.general_info.set_printer_data)
        self.generalA.triggered.connect(self.general_info.show)
        """
        
        self.AouvrirFichier.triggered.connect(self.tableviewwidget.open_file)
        
        
        
        self.menuCode = self.menuBar().addMenu("Programmation")
        self.coder = QAction(QIcon("coder.png"),"Coder")
        self.menuCode.addAction(self.coder)
        self.coder.triggered.connect(self.tableviewwidget.showcodewidget)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = fenPrincipale()
    w.show()
    sys.exit(app.exec())
    
    
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-250,250)

plt.plot(x^9+123*x^8-247*x^7+373*x^6-251*x^5-123*x^4+248*x^3-250*x^2+x+125)
plt.show()

"""
