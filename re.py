# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 19:57:41 2018

@author: zahmed
"""
import re

sentence = 'It is the end of our road. It is time for a new beinging. 89. \n So make sure to grab some coco butter and paranthas'
number = '379-7037'
sentence2='bat cat mat pat dat ccat'
pattern = re.compile('\d+.\d*')
matches = pattern.finditer(number)
print(matches)

for match in matches:
    print(match)