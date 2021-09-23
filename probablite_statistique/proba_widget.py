# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:30:45 2020

@author: Elvis
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure
from matplotlib.backend_bases import Event
from matplotlib.backend_bases import MouseButton 
import matplotlib.pyplot as plt
import numpy as np

#################### PLOT PRINTER #############################
from locals.datasfile import *
from Visualisation_outils.m_parser import *
from Visualisation_outils.plothelper import *
from Visualisation_outils.textreceiver import *

# Liste des fonctions de probalité proposées
fonc_list = [["Exponentielle","Normale","Logistique","Cauchy","Gamma","Weibul",
             "LogNormale","Student","Chi-Squared","F-Distribution"],["Binomial","Pascal","Poisson","Hypergeometric"]]
fonc_list[0].sort()
fonc_list[1].sort()
print(fonc_list)

import proba_calcul


class ProbaWidget(QWidget):
    def __init__(self):
        self.datas = []
        super().__init__()
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas,self)
        self.toolbar_button = QPushButton(QIcon("100(18).png"),"")
        self.toolbar_button.setFixedSize(35,35)
        
        #FONCTION 
        self.fonction_receiver = QLineEdit()
        self.fonction_receiver_ok = QPushButton(QIcon("ok.png"),"")
        
        
        ########
        self.ax = self.figure.add_subplot(111)
        
        # ANNOTATION
        self.text_receiver = FinalTextReceiver()
        self.text_tuple = tuple()
        self.press = None
        self.annotation_first_press = None
        self.annoation_second_press = None
        
        self.layout_principale = QVBoxLayout()
        
        
        # Pour les fonctions 
        
        
    
        
        
        
        # POUR LES PROBALITES
        self.finish_button = QPushButton("Terminer...")
        self.bar_button = QPushButton(QIcon("_bar"),"")
        self.plot_button = QPushButton(QIcon("_plot"),"")
        self.new_button = QPushButton("New")
        self.fill_button = QPushButton("Fill")
        self.fill_button.setCheckable(True)
        self.new_button.setCheckable(True)
        self.bar_button.setCheckable(True)
        self.plot_button.setCheckable(True)
        # Le nom de l'ancienne fonction
        self.old_fonction_name = ""
        # Le combobox
        self.fonc_combobox = QComboBox()
        
        # Exponentiel
        self.expo_widget = QWidget()
        
        
        # Normal
        self.normal_widget = QWidget()
        
        # Lognormal
        self.lognormal_widget = QWidget()
        
        self.cauchy_widget = QWidget()
        
        self.weibull_widget = QWidget()
        
        self.gamma_widget = QWidget()
        
        self.logistic_widget = QWidget()
        
        self.student_widget = QWidget()
        
        self.kisca_widget = QWidget()
        
        self.fdist_widget = QWidget()
        
        self.binomial_widget = QWidget()
        
        self.pascal_widget = QWidget()
        
        
        self.poisson_widget = QWidget()
        
        self.hypergeo_widget = QWidget()
        
        ###########################
        # Pour les annotations
        self.helper = PlotingHelp()
        
        self.bar_button.setFixedSize(35,35)
        self.plot_button.setFixedSize(35,35)
        self.new_button.setFixedSize(35,35)
        self.fill_button.setFixedSize(35,35)
        
        self.toolbar_layout = QHBoxLayout()
        self.toolbar_layout.addWidget(self.toolbar)
        self.toolbar_layout.addWidget(self.fill_button)
        self.toolbar_layout.addWidget(self.new_button)
        self.toolbar_layout.addWidget(self.bar_button)
        self.toolbar_layout.addWidget(self.plot_button)
        self.toolbar_layout.addWidget(self.toolbar_button)
        
        
        # CONNECTIONS
        self.helper.send_info.connect(self.modification)
        self.toolbar_button.clicked.connect(self.helper.show)
        self.fonction_receiver_ok.clicked.connect(self.play_fonc)
        
        text_cid = self.canvas.mpl_connect("button_press_event",self.ann)
        self.text_receiver.send_info.connect(self.text)
        self.fonc_combobox.currentTextChanged.connect(self.manage)
        self.finish_button.clicked.connect(self.calculate)
        
        self.setWindowTitle("Probabilité")
        
        self.init_UI()
        
        
    def calculate(self):
        if self.fonc_combobox.currentText() == "Exponentielle":
            self.expo_calcul()
            
        
    def manage(self,text):
        if text == "Exponentielle":
             
             a = self.layout_principale.takeAt(3).widget()
             a.close()
             print("x")
             self.layout_principale.insertWidget(3,self.expo_widget)
             self.expo_widget.show()
             
        elif text == "Normale":
             a = self.layout_principale.takeAt(3).widget()
             a.close()
             print("x")
             self.layout_principale.insertWidget(3,self.normal_widget)
             self.normal_widget.show()
             
             
        
    def normal_manage(self):
        nu_layout = QFormLayout()
        self.nu_receiver = QLineEdit()
        nu_layout.addRow("nu",self.nu_receiver)
        
        sigma_layout = QFormLayout()
        self.sigma_receiver = QLineEdit()
        sigma_layout.addRow("sigma",self.sigma_receiver)
        
        
        font = QFont("Consolas")
        font.setPixelSize(15)
        
        
        
        self.normal_debut_receiver = QLineEdit()
        self.normal_fin_receiver = QLineEdit()
        
        # Setting sizes
        self.nu_receiver.setFixedSize(80,20)
        self.normal_debut_receiver.setFixedSize(80,20)
        self.normal_fin_receiver.setFixedSize(80,20)
        self.sigma_receiver.setFixedSize(80,20)
        
        # Setting fonts
        self.nu_receiver.setFont(font)
        self.normal_debut_receiver.setFont(font)
        self.normal_fin_receiver.setFont(font)
        self.sigma_receiver.setFont(font)
        
        limits_layout = QHBoxLayout()
        
        debut_layout = QFormLayout()
        debut_layout.addRow("Début",self.normal_debut_receiver)
        
        fin_layout = QFormLayout()
        fin_layout.addRow("Fin",self.normal_fin_receiver)
        
        limits_layout.addLayout(debut_layout)
        limits_layout.addLayout(fin_layout)
        
        #Result
        self.normal_result_lineedit = QLineEdit()
        result_layout = QFormLayout()
        result_layout.addRow("Résultat",self.normal_result_lineedit)
        
        variable_layout = QHBoxLayout()
        variable_layout.addLayout(nu_layout)
        variable_layout.addLayout(sigma_layout)
        variable_layout.addStretch(100)
        
        expo_layout = QVBoxLayout()
        expo_layout.addLayout(variable_layout)
        expo_layout.addLayout(limits_layout)
        expo_layout.addLayout(result_layout)
        
        self.normal_widget.setLayout(expo_layout)
             
             
        
    def exponential_manage(self):
        lambda_layout = QFormLayout()
        self.lambda_receiver = QLineEdit()
        lambda_layout.addRow("lambda",self.lambda_receiver)
        
        font = QFont("Consolas")
        font.setPixelSize(15)
        
        self.lambda_receiver.setFixedSize(80,20)
        
        self.expo_debut_receiver = QLineEdit()
        self.expo_fin_receiver = QLineEdit()
        
        self.expo_debut_receiver.setFixedSize(80,20)
        self.expo_fin_receiver.setFixedSize(80,20)
        
        self.lambda_receiver.setFont(font)
        self.expo_debut_receiver.setFont(font)
        self.expo_fin_receiver.setFont(font)
        
        limits_layout = QHBoxLayout()
        
        debut_layout = QFormLayout()
        debut_layout.addRow("Début",self.expo_debut_receiver)
        
        fin_layout = QFormLayout()
        fin_layout.addRow("Fin",self.expo_fin_receiver)
        
        limits_layout.addLayout(debut_layout)
        limits_layout.addLayout(fin_layout)
        
        #Result
        self.expo_result_lineedit = QLineEdit()
        self.expo_result_lineedit.setFont(font)
        result_layout = QFormLayout()
        result_layout.addRow("Résultat",self.expo_result_lineedit)
        
        expo_layout = QVBoxLayout()
        expo_layout.addLayout(lambda_layout)
        expo_layout.addLayout(limits_layout)
        expo_layout.addLayout(result_layout)
        
        self.expo_widget.setLayout(expo_layout)
    
    def expo_calcul(self):
        lamb = float(self.lambda_receiver.text())
        x1 = float(self.expo_debut_receiver.text())
        x2 = float(self.expo_fin_receiver.text())
        self.expo_result_lineedit.setText("P("+self.expo_debut_receiver.text()+" < x <"
                                          +self.expo_fin_receiver.text()+" ) = "+
                                          str(proba_calcul.expo_proba(lamb,x1,x2)))
        a = np.arange(x1,x2,abs(x1-x2)/1000)
        b = proba_calcul.expo_dist(lamb,x1,x2)
        
        if self.new_button.isChecked():
            self.ax.clear()
        
        if self.plot_button.isChecked():
            self.ax.plot(a,b)
            self.canvas.draw()
            
        if self.bar_button.isChecked():
            self.ax.bar(a,b)
            self.canvas.draw()
            
        if self.fill_button.isChecked():
            self.ax.fill(x1,x2)
            
        
    def init_UI(self):
        self.exponential_manage()
        self.normal_manage()
        
        font = QFont("Consolas")  #"MS Shell Dlg 2"
        font.setPixelSize(17)
        self.fonc_combobox.setFont(font)
        self.fonc_combobox.addItems(fonc_list[0])
        self.fonc_combobox.insertSeparator(11)
        self.fonc_combobox.addItems(fonc_list[1])
        
        
        fonction_receiver_layout = QFormLayout()
        fonction_receiver_layout.addRow("f(x) = ",self.fonction_receiver)
        fonction_layout = QHBoxLayout()
        fonction_layout.addLayout(fonction_receiver_layout)
        fonction_layout.addWidget(self.fonction_receiver_ok)
        
        self.layout_principale.addLayout(self.toolbar_layout)
        self.layout_principale.addWidget(self.canvas)
        
        self.layout_principale.addWidget(self.fonc_combobox)
        
        self.layout_principale.addWidget(self.expo_widget)
        
        self.layout_principale.addLayout(fonction_layout)
        self.layout_principale.addWidget(self.finish_button)
        self.setLayout(self.layout_principale)
    
    def play_fonc(self):
        """ plot(expression,labels) """
        if self.fonction_receiver.text() != "":
            
            fonc,arg = get_fonc_and_arg(self.fonction_receiver.text())
            arg = get_arguments(arg)
            print(arg)
            if fonc == "plot":
        
                code = str()
                code = code + "from numpy import *\n"
                code = code + "limits = self.ax.axis()\n"
                code = code + "x = arange(limits[0],limits[1],abs((limits[0]-limits[1]))/1000)\n"
                code = code +"self.ax.plot(x,"+str(arg[0])+",label = '"+str(arg[1])+"')\n"
                code = code +"self.ax.legend()\n"
                code = code +"self.canvas.draw()"
                
                try:
                    c = compile(code,"débug.txt","exec")
                    
                    try:
                        
                        exec(c)
                    
                    except Exception as e:
                    
                        QMessageBox.information(self,"information",str(e))
                       
                except Exception as e:
                    QMessageBox.information(self,"information",str(e))
                    
            else:
                QMessageBox.information(self,"information","la fonction adéquate à mettre ici est  plot")
            
                print(code)
        
    def text(self,info):
        print(info)
        
        if info[0] == 1:
            
            """
            [type d'annoation : text  ou annotation,[famille,couleur,point_size,text à afficher]]
         
             """
            dic = {
                 "family": info[1][0],
                 "color" : info[1][1],
                 "size" : info[1][2]
                 }
            
            self.ax.text(self.text_tuple[0],self.text_tuple[1],info[1][3],fontdict= dic)
            self.canvas.draw()
        else:
            dic = {
                 "family": info[1][0],
                 "color" : info[1][1],
                 "size" : info[1][2]
                 }
            self.ax.annotate(info[1][3],
                             xy = (self.text_tuple[0],self.text_tuple[1]),
                             xytext = (float(info[2][0]),float(info[2][1])),
                             textcoords = "axes fraction",
                             arrowprops = dict(facecolor = info[1][1],color = info[1][1]))
            self.canvas.draw()
            

    def ann(self,event):

        if event.button == MouseButton.RIGHT:
            self.text_receiver.show()
            self.text_tuple = (event.xdata,event.ydata)              
          
    def modification(self,tab):
        """[1ou 2 u pour  pas de grille et deux pour grille ,
        [grid_line_style,grid_line_width,grid_color],
        [right,left,top,bottom],[x,y,x_color,y_color]]
        """
        if tab [0] == 1:
            self.figure.subplots_adjust(left = tab[2][1],
                                right = tab[2][0],
                                top = tab[2][2],
                                bottom = tab[2][3])
            
            for labels in self.ax.get_xticklabels():
                labels.set_rotation(tab[3][0])
                labels.set_color(tab[3][2])
            
            for labels in self.ax.get_yticklabels():
                labels.set_rotation(tab[3][1])
                labels.set_color(tab[3][3])
                
            self.canvas.draw()
            
        elif tab[0] == 2:
            
            self.ax.grid(True,color = tab[1][2],linestyle = tab[1][0],linewidth = tab[1][1])
            
            self.figure.subplots_adjust(left = tab[2][1],
                                right = tab[2][0],
                                top = tab[2][2],
                                bottom = tab[2][3])
            
            for labels in self.ax.xaxis.get_ticklabels():
                labels.set_rotation(tab[3][0])
            
            for labels in self.ax.yaxis.get_ticklabels():
                labels.set_rotation(tab[3][1])
                
            self.canvas.draw()
            
                
                
        
    
    def plot(self,information):
        print(information)        
        if information[0] == 1:
            if len(information[1]) == 1:
                
                if is_only_number(self.datas[information[1][0]])[0]:
                    self.datas[information[1][0]] = to_number(self.datas[information[1][0]])
                    
                    
                self.ax.plot(self.datas[information[1][0]],
                                color = information[3][0],
                                marker = information[3][1],
                                linestyle = information[3][2],
                                linewidth= float(information[3][3]),
                                label = information[2][1])
                
                self.ax.set_title(information[2][0])
                self.ax.set_xlabel(information[2][2])
                self.ax.set_ylabel(information[2][3])
                                
                self.ax.legend()
                self.canvas.draw()
                plt.legend()
                self.show()
                
            elif len(information[1]) == 2:
                
                if is_only_number(self.datas[information[1][0]])[0]:
                    self.datas[information[1][0]] = to_number(self.datas[information[1][0]])
                    
                if is_only_number(self.datas[information[1][1]])[0]:
                    self.datas[information[1][1]] = to_number(self.datas[information[1][1]])
                        
                
                self.ax.plot(self.datas[information[1][0]],self.datas[information[1][1]],
                                color = information[3][0],
                                marker = information[3][1],
                                linestyle = information[3][2],
                                linewidth= float(information[3][3]),
                                label = information[2][1])
                
                self.ax.set_title(information[2][0])
                self.ax.set_xlabel(information[2][2])
                self.ax.set_ylabel(information[2][3])
                 
                self.ax.legend()
                self.canvas.draw()
                plt.legend()
                self.show()
        
        
                
    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)
        
    def on_press(self,event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.rect.axes: return

        contains, attrd = self.rect.contains(event)
        if not contains: return
        print('event contains', self.rect.xy)
        x0, y0 = self.rect.xy
        self.press = x0, y0, event.xdata, event.ydata
        
    def on_motion(self,event):
        'on motion we will move the rect if the mouse is over us'
        """
        if self.press is None: return
        if event.inaxes != self.rect.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        #print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
        """
        self.annoation_second_press = (event.xdata, event.ydata)
        self.text_receiver.show()
        
        
    def on_release(self,event):
        'on release we reset the press data'
        self.press = None
        self.rect.figure.canvas.draw()
    
    def set_datas(self,data):
        self.datas = data
        
    def closeEvent(self,event):
        self.helper.close()
        self.text_receiver.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = ProbaWidget()
    a.show()
    sys.exit(app.exec())