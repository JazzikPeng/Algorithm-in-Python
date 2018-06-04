#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 17:38:52 2017

@author: zhejianpeng
"""
answer = 'ab'
secret = ['a','a']
input_board = ['aabbbbbb','aabbbbbb','bbbbbbbb','bbbbbbbb','bbbbbbbb','bbbbbbbb','bbbbbbbb','bbbbbbbb']
board = []
for i in input_board:
    board.append(list(i))
# count = number of solution
# char need to find
sol = ''
counter = 0

# declare a matrix keep in track which point is vistied
notVisited = [[True for x in y] for y in board]
print(notVisited)

def solve(x,y, sol, counter,n): #x,y position, c is the elementes your looking for 
    if sol==answer:
        print('solved')
        print(sol)
        n+=1
        global counter
        counter = 0
        sol=''
    else:
        for i in range(x,len(board)):
            for j in range(y,len(board)):
                if board[i][j] == secret[counter]: # if that space is correct char arr[i][j] 
                    print('HERE')
                    sol +=board[i][j]
                    counter+=1
                    notVisited[i][j] = False
                    if solve(i,j,sol, counter,n) and notVisited[i][j]:
                        return True
                    else:
                        notVisited[i][j] = True
    print('no solution')
        
solve(0,0,sol, 0,0)
