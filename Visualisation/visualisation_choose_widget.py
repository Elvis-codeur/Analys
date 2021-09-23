# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:05:15 2021

@author: Elvis
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from Visualisation_outils.visualisation_choose_button import *

#Pour les info_receiver

from .barinforeceiver import *
from .scatterinforeceiver import *
from .plotinforeceiver import *
from .stackinforeceiver import *
from .multiplebarinforeceiver import *
from .multiplebarinforeceiver3d import *
from .barinforeceiver3d import *
from .barinforeceiver import *
from .boxplotinforeceiver import *
from .pieinforeceiver import *
"""

from barinforeceiver import *
from scatterinforeceiver import *
from plotinforeceiver import *
from stackinforeceiver import *
from multiplebarinforeceiver import *
from multiplebarinforeceiver3d import *
from barinforeceiver3d import *
from barinforeceiver import *
from boxplotinforeceiver import *
from pieinforeceiver import *
"""

image_path = ["imgs/circulaire.jpg",
              "imgs/diagramme_a_bande_multiple.png",
              "imgs/diagramme_a_bande_multiple_3d.png",
              "imgs/diagramme_a_moustache.png",
              "imgs/diagramme_en_bande.png",
              "imgs/diagramme_en_bande_3d.png",
              "imgs/diagramme_linéaire_example.png",
              "imgs/nuages_de_points.png",
              "imgs/nuages_diagramme_en_couche.png"
              ]

class VisualisationChooseWidget(QMainWindow):
    send_ploting_information = pyqtSignal(dict)
    def __init__(self):
        
        circulaire_choosed = pyqtSignal()
        bande_multiple_choosed = pyqtSignal()
        bande_multiple_3D_choosed = pyqtSignal()
        moustache_choosed = pyqtSignal()
        bande_choosed = pyqtSignal()
        bande_3D_choosed = pyqtSignal()
        lineaire_choosed = pyqtSignal()
        nuage_choosed = pyqtSignal()
        couche_choosed = pyqtSignal()
        
        super().__init__()
        self.data = []
        self.button_list = []
        self.signal_list = []
        self.layout_principale = QGridLayout()
        self.info_receiver_list = []
        
        self.signal_list.append(circulaire_choosed)
        self.signal_list.append(bande_multiple_choosed)
        self.signal_list.append(bande_multiple_3D_choosed)
        self.signal_list.append(moustache_choosed)
        self.signal_list.append(bande_choosed)
        self.signal_list.append(bande_3D_choosed)
        self.signal_list.append(lineaire_choosed)
        self.signal_list.append(nuage_choosed)
        self.signal_list.append(couche_choosed)
        
        # Info receiver
        # LES WIDGETS DE RECEPTION D'INFORMATION
        self.plot_info = PlotInfoReceiver()
        self.bar_info = BarInfoReceiver()
        self.scatter_info = ScatterInfoReceiver()
        self.stack_info = StackInfoReceiver()
        self.pie_info = PieInfoReceiver()
        self.multiplebar_info = MultipleBarInfoReceiver()
        self.boxplot_info = BoxPlotInfoReceiver()
        self.bar3d_info = BarInfoReceiver_3d()
        self.multiplebar3d_info = MultipleBarInfoReceiver_3d()
        
        self.info_receiver_list.append(self.pie_info)
        self.info_receiver_list.append(self.multiplebar_info)
        self.info_receiver_list.append(self.multiplebar3d_info)
        self.info_receiver_list.append(self.boxplot_info)
        self.info_receiver_list.append(self.bar_info)
        self.info_receiver_list.append(self.bar3d_info)
        self.info_receiver_list.append(self.plot_info)
        self.info_receiver_list.append(self.scatter_info)
        self.info_receiver_list.append(self.stack_info)
        self.info_receiver_list.append(self.pie_info)
        
        
        self.manage()
        self.make_connection()
        self.setGeometry(120,100,900,700)
        
        
    def make_connection(self):
        self.plot_info.info_receiver_send_ploting_info.connect(self.visualisation_choose_relay)
        
    def visualisation_choose_relay(self,dic):
        self.send_ploting_information.emit(dic)
        print("emited-- 3")
        
    
    def set_printer_data(self,data):
        self.data = data
        
        self.bar3d_info.set_printer_data(data)
        self.bar_info.set_printer_data(data)
        self.multiplebar3d_info.set_printer_data(data)
        self.multiplebar_info.set_printer_data(data)
        self.boxplot_info.set_printer_data(data)
        self.stack_info.set_printer_data(data)
        self.pie_info.set_printer_data(data)
        self.scatter_info.set_printer_data(data)
        self.plot_info.set_printer_data(data)
        
        
    def manage(self):
        
        r = 0
        for i in range(3):
            for u in range(3):
                a = VisualisationChooseButton()
                a.set_image(image_path[r])
                self.layout_principale.addWidget(a,i,u,1,1)
                self.button_list.append(a)
                self.button_list[r].clicked.connect(self.info_receiver_list[r].show)
                r = r + 1
                
        w = QScrollArea()
        w.setLayout(self.layout_principale)
        self.setCentralWidget(w)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = VisualisationChooseWidget()
    w.show()
    sys.exit(app.exec())
    
            
        