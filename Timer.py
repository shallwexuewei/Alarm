'''
Created on 2015-11-26

@author: Xuewei (Harvey) Wu
'''

from PyQt4.QtCore import *

def min2ms(m):
    return m * 60 * 1000

class Timer(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.qtime = QTime()
        self.qtime.start()
        self.length = min2ms(30) # default value of time length is 30 min
    
    def reset(self, m):
        self.start = self.qtime.restart()
        self.length = min2ms(m)
    
    def reset10(self):
        self.reset(10)
        
    def timeout(self):
        if self.qtime.elapsed() < self.length:
            return False
        return True