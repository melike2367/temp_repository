# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:30:49 2022

@author: melik
"""

import random
inp=int(input("enter N:"))
lst=[]
for x in range(0,inp):
    a=random.randint(0,9)
    lst.append(a)
print(lst)

for y in range(0,10):
    
    b=lst.count(y)
    print(str(y)+":"+b*'*')
