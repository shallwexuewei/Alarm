'''
Created on 2015-11-26

@author: Xuewei (Harvey) Wu
'''


from PyQt4.QtGui import *
from PyQt4.QtCore import * 
from Timer import Timer

class MainView(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.label = QLabel("Alarm!", self)
        
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        
        self.timer = Timer()
        
        self.add_button_timer(10)
        
        self.add_button("&Quit", SLOT("quit()"))
        
        self.setLayout(self.layout)
        
    def add_button_timer(self, m):
        button = QPushButton("%dmin"%m, self)
        button.clicked.connect(lambda: self.timer.reset(m))
        self.layout.addWidget(button)
        
        
    def add_button(self, msg, slot):
        button = QPushButton(msg, self)
        self.connect(button, SIGNAL("clicked()"), QCoreApplication.instance(), slot)
        self.layout.addWidget(button)