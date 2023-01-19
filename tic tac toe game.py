# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 18:39:01 2022

@author: melik
"""

lst=[['-','-','-'],['-','-','-'],['-','-','-']]
counter=0
while True:
    if counter==9:
        print('    0 1 2')
        print('---------') 
        for x in range(0,3):
            for y in range(0,3):
                if y==0:
                    print(x,"|",lst[x][y],end=' ')
                else:
                    print(lst[x][y],end=' ')
            print()
            
        print("It's a tie!")
        break
    
    print('    0 1 2')
    print('---------')
    for x in range(0,3):
        for y in range(0,3):
            if y==0:
                print(x,"|",lst[x][y],end=' ')
            else:
                print(lst[x][y],end=' ')
        print()
        
    row1=int(input('Player 1 - Please enter row number:'))
    column1=int(input('Player 1 - Please enter column number:'))
    
    if lst[row1][column1]=='-':
        counter=counter+1
        lst[row1][column1]='X'
    
    if lst[0][0]==lst[1][0]==lst[2][0]=='X' or lst[0][1]==lst[1][1]==lst[2][1]=='X' or lst[0][2]==lst[1][2]==lst[2][2]=='X' or lst[0][0]==lst[0][1]==lst[0][2]=='X' or lst[1][0]==lst[1][1]==lst[1][2]=='X' or lst[2][0]==lst[2][1]==lst[2][2]=='X' or lst[0][0]==lst[1][1]==lst[2][2]=='X' or lst[0][2]==lst[1][1]==lst[2][0]=='X' :
        print('    0 1 2')
        print('---------') 
        for x in range(0,3):
            for y in range(0,3):
                if y==0:
                    print(x,"|",lst[x][y],end=' ')
                else:
                    print(lst[x][y],end=' ')
            print()
        print('Player 1 wins!')
        break
    if counter==9:
        print('    0 1 2')
        print('---------') 
        for x in range(0,3):
            for y in range(0,3):
                if y==0:
                    print(x,"|",lst[x][y],end=' ')
                else:
                    print(lst[x][y],end=' ')
            print()
            
        print("It's a tie!")
        break
        
    print('    0 1 2')
    print('---------') 
    for x in range(0,3):
        for y in range(0,3):
            if y==0:
                print(x,"|",lst[x][y],end=' ')
            else:
                print(lst[x][y],end=' ')
        print()
    
    row2=int(input('Player 2 - Please enter row number:'))
    column2=int(input('Player 2 - Please enter column number:'))
    
    if lst[row2][column2]=='-':
        counter=counter+1
        lst[row2][column2]='O'
    
    if lst[0][0]==lst[1][0]==lst[2][0]=='O' or lst[0][1]==lst[1][1]==lst[2][1]=='O' or lst[0][2]==lst[1][2]==lst[2][2]=='O' or lst[0][0]==lst[0][1]==lst[0][2]=='O' or lst[1][0]==lst[1][1]==lst[1][2]=='O' or lst[2][0]==lst[2][1]==lst[2][2]=='O' or lst[0][0]==lst[1][1]==lst[2][2]=='O' or lst[0][2]==lst[1][1]==lst[2][0]=='O' :
        print('    0 1 2')
        print('---------') 
        for x in range(0,3):
            for y in range(0,3):
                if y==0:
                    print(x,"|",lst[x][y],end=' ')
                else:
                    print(lst[x][y],end=' ')
            print()
        print('Player 2 wins!')
        break
    