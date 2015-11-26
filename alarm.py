'''
Created on 2015-11-26

@author: Xuewei (Harvey) Wu
'''
from MainView import MainView
import sys

from PyQt4.QtGui import *

app = QApplication(sys.argv)
mw = MainView()
mw.show()
sys.exit(app.exec_()) 