# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:53:37 2020

@author: zahmed
"""

string = 'from coco cabana with coco channel'
cnt = Counter()
for x in string.split(' '):
    cnt[x] +=1
print('number of times coco shows up in the string = {}'.format(cnt['coco']))
cnt

string_vocab = []
for x in string.split(" "):
    string_vocab.append(x)
print(string_vocab)

string_dict = {}
for i,w in enumerate(string_vocab):
    print(w, i)
    string_dict[w] = i   
string_dict

mirror = np.arange(0,6,1)
ms = list(zip(string_vocab, mirror))
print(ms)
for w,n in ms:
    print(w, n)
    
ex_dict = {}
for w,n in enumerate(ms):
    ex_dict[w] = n
ex_dict[0]