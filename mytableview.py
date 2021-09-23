# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:46:09 2020

@author: elvis
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyTableView(QTableView):
    def __init__(self):
        super().__init__()