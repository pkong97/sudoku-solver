
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 15:27:24 2017

@author: patri
"""
def cross(A, B):
    '''
    Produces cross product of elements in A and B
    '''
    return [a + b for a in A for b in B]

rows = 'ABCDEFGHI'
cols = '123456789'
squares = cross(rows, cols)

unitlist = ([cross(rows, c) for c in cols] + # list of columns
            [cross(r, cols) for r in rows] + # list of rows
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]) #list of boxes
        
unit = dict((k, [u for u in unitlist if k in u]) 
            for k in squares)
                              

peers = dict ((s, set(sum(unit[s],[]))-set([s])) # dictionary with key:value pairs as square:(list of peers) 
              for s in squares)

def solve(grid):
    '''
    grid is string with values of 0-9, 0 meaning empty square on sudoku board
    '''
    rows = 'ABCDEFGHI'
    cols = '123456789'
    squares = cross(rows, cols)
    
    def make_board(grid):
        '''
        produce dict with key: squares
                   values: char
        '''
        #build list of values, zip with squares, then turn into dict
        char = [c for c in grid if c in cols or c in '0.']
        board = dict(zip(squares, char))
        assert len(board) == 81
        return board
    
    def generate_possible_boards(board):
        '''
        produce list of possible boards, keeps only valid boards
        '''
        filled = fill_square(board)
        
        return keep_valid(filled)
        
        def keep_valid(board):
            '''
            listofboards -> listofboards
            check each board units to see if it is valid
            '''
            
    
            def fill_square(board):
                '''
                take board and produce a list of new boards with 
                first blank spot filled with integers from 1 to 9
                '''
                listofboards = []
                copyboard = board.copy()
                tick = 9
                for i in copyboard.keys():
                    if copyboard[i] == '0':
                        for n in range(1, 10):
                            copyboard[i] = n
                            listofboards.append(copyboard)
                            copyboard = board.copy()
                            tick -= 1
                        if tick == 0:
                            break
                
                return listofboards

