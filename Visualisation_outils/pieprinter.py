# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:29:44 2020

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

from locals.datasfile import *
from Visualisation_outils.m_parser import *
from Visualisation_outils.plothelper import *
from Visualisation_outils.textreceiver import *

from State.global_state import SOFTWARE_NAME
#################### PLOT PRINTER #############################

class PiePrinter(QWidget):
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
        
        fonction_receiver_layout = QFormLayout()
        fonction_receiver_layout.addRow("f(x) = ",self.fonction_receiver)
        fonction_layout = QHBoxLayout()
        fonction_layout.addLayout(fonction_receiver_layout)
        fonction_layout.addWidget(self.fonction_receiver_ok)
        
        ###########################
        # Pour les annotations
        self.helper = PlotingHelp()
        
        toolbar_layout = QHBoxLayout()
        toolbar_layout.addWidget(self.toolbar)
        toolbar_layout.addWidget(self.toolbar_button)
        
        self.layout_principale.addLayout(toolbar_layout)
        self.layout_principale.addWidget(self.canvas)
        #self.layout_principale.addLayout(fonction_layout)
        self.setLayout(self.layout_principale)
        
        # CONNECTIONS
        self.helper.send_info.connect(self.modification)
        self.toolbar_button.clicked.connect(self.helper.show)
        self.fonction_receiver_ok.clicked.connect(self.play_fonc)
        
        """
        self.ax.plot([1,2,3,4,12,8,4,7,8,4,5,9,85,7,8,4,7,7,7,4,5,412,1,0,31,4,7,7,7])
        self.ax.set_xlabel("fils de david")
        self.ax.set_ylabel("JESUS CHRIST")
        self.ax.set_title("Gloire")
        """
        text_cid = self.canvas.mpl_connect("button_press_event",self.ann)
        self.text_receiver.send_info.connect(self.text)
        
        self.setWindowTitle("Diagramme circulaire")
        self.setWindowIcon(QIcon("analys.png"))
    
    
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
            
                
    
    def clear(self):
        self.ax.clear()
        
    
    def pie(self,information):
        print(information) 
        
        if information[0] == 1:
            # On utilise les limits
            
            for i in range(len(information[1])):
                if information[2][2][i][0] != information[2][2][i][1]:
                    if type(is_only_number(self.datas[information[1][i]][information[2][2][i][0]:
                                                                         information[2][2][i][1]-1])) == bool:
                        
                        self.datas[information[1][i]][information[2][2][i][0]:
                                    information[2][2][i][1]-1] = \
                            to_number(self.datas[information[1][i]][information[2][2][i][0]:
                                                                         information[2][2][i][1]-1])
                                
                    elif type(is_only_number(self.datas[information[1][i]][information[2][2][i][0]:
                                                                         information[2][2][i][1]-1])) == tuple:
                        QMessageBox.information(self,"Information","La case " +
                                            str(is_only_number(self.datas[information[1][i]][information[2][2][i][0]:
                                                                         information[2][2][i][1]])[1]) + " de la colonne "
                                            +TABLES_NAMES[information[1][i]]+ "contient un caractère non numérique")        
                
                else:
                    if type(is_only_number(self.datas[information[1][i]])) == bool:
                        
                        self.datas[information[1][i]] = to_number(self.datas[information[1][i]])
                                
                    elif type(is_only_number(self.datas[information[1][i]])) == tuple:
                        QMessageBox.information(self,"Information","La case " +
                                            str(is_only_number(self.datas[information[1][i]])[1]) + " de la colonne "
                                            +TABLES_NAMES[information[1][i]]+ "contient un caractère non numérique")    
                
            final_data = []
            for i in range(len(information[1])):
                if information[2][2][i][0] != information[2][2][i][1]:
                    
                    final_data.append(self.datas[information[1][i]][information[2][2][i][0]:
                                                                         information[2][2][i][1]-1])
                else:
                    final_data.append(self.datas[information[1][i]])
               
            x =[]
            for i in range(len(final_data)):
                x.append(mean(final_data[i]))
                
                
            self.ax.pie(x,
                        labels = information[2][0],
                        colors = information[2][1],
                        startangle= 90,
                        shadow = True,
                        autopct="%1.1f%%"
                        )
            
            self.ax.set_title(information[3][0]+ "                      |Created with "+SOFTWARE_NAME)
            self.ax.set_xlabel(information[3][1])
            self.ax.set_ylabel(information[3][2])
            
            self.ax.legend()
            self.canvas.draw()
            plt.legend()
            
            
                                
                    
            
                
        
        
                
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
    a = PiePrinter()
    a.show()
    sys.exit(app.exec())