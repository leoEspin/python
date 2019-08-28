#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:26:04 2019
Uses backtraking to fill an n x n chess board with n queens in a way that the queens
cannot attack each other. 
The progress of the solution is shown with an animation on the terminal, showing
the current status of the solution at each step. It finishes with an empty board
if a solution is not found

@author: Leonardo Espin
"""
class Board:
    os = __import__('os')
    platform= __import__('platform')
    time= __import__('time')
    
    def __init__(self,n:int):
        self.size=n
        self.board=[]
        currOS=self.platform.system()
        if currOS == 'Windows':
            self.os.system('cls')
        else:
            self.os.system('clear')
        #delay for screen output in seconds. Can be changed with setDelay
        self.delay=0.4 
        self.toString()
        
    def setDelay(self,secs):
        self.delay=secs
            
    def toString(self):
        '''
        Prints the current status of the chess board on the screen
        '''
        output=[]
        row=['*']+['-' for k in range(self.size)]+['*']
        hedge=[' ']+['*' for k in range(self.size)]+[' ']
        output.append(hedge)
        for i in range(self.size):
            output.append(row.copy())
        output.append(hedge)    
        #position queens in screen
        for tup in self.board:
            #flipping vertically (rows) for visual representation:
            output[self.size+1-tup[0]][tup[1]]='Q'
            
        self.time.sleep(self.delay)
        #position cursor at top left corner
        print("\033[1;1H")
        for i in range(self.size+2):
            #still have to join each row into single strings
            print(''.join(output[i]))
            
    def singlePosition(self,tup1:tuple,tup2:tuple)-> bool:
        '''
        Checks the validity of the placement of a single couple 
        of queens in the board
        '''
        if abs(tup1[0]-tup2[0]) == abs(tup1[1]-tup2[1]):
            #within a diagonal
            return False
        if tup1[0]-tup2[0]==0:
            #left or rigth of tup1
            return False
        if tup1[1]-tup2[1]==0:
            #up or down of tup1
            return False
        return True

    def validPosition(self,tupList,tup2:tuple)-> bool:
        '''
        Checks that the placement of the queen given in tup2
        is valid compared with all the queens listed in 
        tupList
        '''
        output=True
        n=len(tupList)
        i=0
        while i<n and output:
            output=output and self.singlePosition(tupList[i],tup2)
            i+=1
        return output
    
    def place(self,tup:tuple):
        self.board.append(tup)
        self.toString()
        
    def remove(self):
        self.board.pop()
        self.toString()
    
    def fillBoard(self,nextCol=1):
        '''
        Uses backtraking to fill the n x n board with n queens,
        at each call checking the validity of the newly placed
        queen, with respect to the previously placed queens
        '''
        if nextCol>self.size:#no left positions to fill
            self.toString()
            return True
        else:
            for k in range(self.size):#k is for rows
                #use property that just one queen per row to avoid
                #already filled rows
                if k in [tup[0]-1 for tup in self.board]:
                    pass
                else:
                    test=(k+1,nextCol)#shift k from index to board position
                    if self.validPosition(self.board,test):
                        self.place(test)                     
                        #use property that just one queen per column,
                        #so fill next column:
                        if self.fillBoard(nextCol+1):return True
                        self.remove()
                        
            return False    
               
#if executing as main program        
if __name__ == '__main__':        
    tmp=Board(8)
    tmp.fillBoard()
