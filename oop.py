# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 08:48:01 2020

@author: zahmed
"""

class mathy:
    
    one = 1
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def adder(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1-self.num2
    def raiser (self):
        return int(self + self.one)

mathy(10,4).adder()    