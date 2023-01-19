# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 19:06:35 2022

@author: melik
"""


def lava(array):
    p=0
    new=[]
    counter=0
    total=0
    str=''
    
    for x in range (max(array)):
        for y in range (10):
            if array[y]<max(array)-p:
                new.append('-')
            if array[y]>=max(array)-p:
                new.append("w")
        p=p+1
       
    for z in new:
        str=str+z
        counter=counter+1
        if counter%10==0:
            total=total+int(str.rfind('w')-str.index('w')-(str.count('w')-2)-1)
            str=''
    return total
print(lava([5 ,3 ,4 ,3 ,6 ,8 ,0 ,8 ,5 ,7]))



#exampleplane
'-----w-w--'
'-----w-w-w'
'----ww-w-w'
'w---ww-www'
'w-wwww-www'
'wwwwww-www'
'wwwwww-www'
'wwwwww-www'

        
        
    