def solve(board):
    '''
    board is dictionary of a sudoku board
    keys are the coordinates of the squares
    values is a string of integers from 0-9, 0 indicates an empty square
    '''       
    filled = fill_square(board)
    
    branch = keep_valid(filled[0], filled[1])
    
    if len(branch) == 1 and '0' not in branch[0].values():
        return branch[0]
    else:
        return solve_lobd(branch)

def solve_lobd(branch):
    
    if len(branch) == 0:
        return "No solution"
    else:
        solved = solve(branch[len(branch) - 1])
        if solved != "No solution":
            return solved
        else:
            return solve_lobd(branch[:-1])
            
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

def fill_square(board):
    '''
    take board and produce a list of new boards with 
    first blank spot filled with integers from 1 to 9
    
    dictionary -> listof dictionary
    '''
    listofboards = []
    copyboard = board.copy()
    tick = 9
    sq_filled = ''
    for i in copyboard.keys():
        if copyboard[i] == '0':
            sq_filled = i
            for n in '123456789':
                copyboard[i] = n
                listofboards.append(copyboard)
                copyboard = board.copy()
                tick -= 1
            if tick == 0:
                break
                
    return listofboards, sq_filled

def build_peers(board):
    '''
    dictionary -> dictionary of board with values as a list of peers
    '''
    new_board = board.copy()
    new_board2 = board.copy()
    list_of_peers = []
    for i in peers.keys(): #listofpeers
        for v in peers[i]:
            list_of_peers.append(new_board2[v])
        new_board[i] = list_of_peers
        list_of_peers = []
    
    return new_board 

    
def keep_valid(lob, sq_filled):
    '''
    listofboards key -> listofboards
    check each board units to see if it is valid
    '''
    to_remove = []
    
    for i in range(0, len(lob)): #iterating through list of dict
        peers_board = build_peers(lob[i])
        current_board = lob[i]
        for k in current_board.keys(): #dict
            if k == sq_filled and current_board[k] in peers_board[k]: #if current square empty, next board
                to_remove.append(current_board)
    
    for i in to_remove:
        lob.remove(i)
                 
    return lob
                            
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
            

#EXAMPLES
#---------------------------------------------

#sudoku_grid_easy =  [2, 7, 4, 0, 9, 1, 0, 0, 5, 
                    # 1, 0, 0, 5, 0, 0, 0, 9, 0,
                    # 6, 0, 0, 0, 0, 3, 2, 8, 0,
                    # 0, 0, 1, 9, 0, 0, 0, 0, 8,
                    # 0, 0, 5, 1, 0, 0, 6, 0, 0,
                    # 7, 0, 0, 0, 8, 0, 0, 0, 3,
                    # 4, 0, 2, 0, 0, 0, 0, 0, 9,
                    # 0, 0, 0, 0, 0, 0, 0, 7, 0,
                    # 8, 0, 0, 3, 4, 9, 0, 0, 0]

sudoku_grid_easy = '274091005100500090600003280001900008005100600700080003402000009000000070800349000'
B1_filled = make_board(sudoku_grid_easy)

#print(solve(B1_filled))
#produces:

#{'A1': '2', 'A2': '7', 'A3': '4', 'A4': '8', 'A5': '9', 'A6': '1', 'A7': '3', 'A8': '6', 'A9': '5', 
# 'B1': '1', 'B2': '3', 'B3': '8', 'B4': '5', 'B5': '2', 'B6': '6', 'B7': '4', 'B8': '9', 'B9': '7', 
# 'C1': '6', 'C2': '5', 'C3': '9', 'C4': '4', 'C5': '7', 'C6': '3', 'C7': '2', 'C8': '8', 'C9': '1', 
# 'D1': '3', 'D2': '2', 'D3': '1', 'D4': '9', 'D5': '6', 'D6': '4', 'D7': '7', 'D8': '5', 'D9': '8', 
# 'E1': '9', 'E2': '8', 'E3': '5', 'E4': '1', 'E5': '3', 'E6': '7', 'E7': '6', 'E8': '4', 'E9': '2', 
# 'F1': '7', 'F2': '4', 'F3': '6', 'F4': '2', 'F5': '8', 'F6': '5', 'F7': '9', 'F8': '1', 'F9': '3', 
# 'G1': '4', 'G2': '6', 'G3': '2', 'G4': '7', 'G5': '5', 'G6': '8', 'G7': '1', 'G8': '3', 'G9': '9', 
# 'H1': '5', 'H2': '9', 'H3': '3', 'H4': '6', 'H5': '1', 'H6': '2', 'H7': '8', 'H8': '7', 'H9': '4', 
# 'I1': '8', 'I2': '1', 'I3': '7', 'I4': '3', 'I5': '4', 'I6': '9', 'I7': '5', 'I8': '2', 'I9': '6'}

#sudoku_grid_hard = [5, 0, 0, 0, 0, 4, 0, 7, 0,
                   # 0, 1, 0, 0, 5, 0, 6, 0, 0,
                   # 0, 0, 4, 9, 0, 0, 0, 0, 0,
                   # 0, 9, 0, 0, 0, 7, 5, 0, 0,
                   # 1, 8, 0, 2, 0, 0, 0, 0, 0,
                   # 0, 0, 0, 0, 0, 6, 0, 0, 0,
                   # 0, 0, 3, 0, 0, 0, 0, 0, 8,
                   # 0, 6, 0, 0, 8, 0, 0, 0, 9,
                   # 0, 0, 8, 0, 7, 0, 0, 3, 1]

sudoku_grid_hard = '500004070010050600004900000090007500180200000000006000003000008060080009008070031'
B2_filled = make_board(sudoku_grid_hard)

#print(solve(B2_filled))
#produces:

#{'A1': '5', 'A2': '3', 'A3': '9', 'A4': '1', 'A5': '6', 'A6': '4', 'A7': '8', 'A8': '7', 'A9': '2', 
# 'B1': '8', 'B2': '1', 'B3': '2', 'B4': '7', 'B5': '5', 'B6': '3', 'B7': '6', 'B8': '9', 'B9': '4', 
# 'C1': '6', 'C2': '7', 'C3': '4', 'C4': '9', 'C5': '2', 'C6': '8', 'C7': '3', 'C8': '1', 'C9': '5', 
# 'D1': '2', 'D2': '9', 'D3': '6', 'D4': '4', 'D5': '1', 'D6': '7', 'D7': '5', 'D8': '8', 'D9': '3', 
# 'E1': '1', 'E2': '8', 'E3': '7', 'E4': '2', 'E5': '3', 'E6': '5', 'E7': '9', 'E8': '4', 'E9': '6', 
# 'F1': '3', 'F2': '4', 'F3': '5', 'F4': '8', 'F5': '9', 'F6': '6', 'F7': '1', 'F8': '2', 'F9': '7', 
# 'G1': '9', 'G2': '2', 'G3': '3', 'G4': '5', 'G5': '4', 'G6': '1', 'G7': '7', 'G8': '6', 'G9': '8', 
# 'H1': '7', 'H2': '6', 'H3': '1', 'H4': '3', 'H5': '8', 'H6': '2', 'H7': '4', 'H8': '5', 'H9': '9', 
# 'I1': '4', 'I2': '5', 'I3': '8', 'I4': '6', 'I5': '7', 'I6': '9', 'I7': '2', 'I8': '3', 'I9': '1'}

#sudoku_grid_hardest = [0, 0, 5, 3, 0, 0, 0, 0, 0,
                      # 8, 0, 0, 0, 0, 0, 0, 2, 0,
                      # 0, 7, 0, 0, 1, 0, 5, 0, 0,
                      # 4, 0, 0, 0, 0, 5, 3, 0, 0,
                      # 0, 1, 0, 0, 7, 0, 0, 0, 6,
                      # 0, 0, 3, 2, 0, 0, 0, 8, 0,
                      # 0, 6, 0, 5, 0, 0, 0, 0, 9,
                      # 0, 0, 4, 0, 0, 0, 0, 3, 0,
                      # 0, 0, 0, 0, 0, 9, 7, 0, 0,]
sudoku_grid_hardest = '005300000800000020070010500400005300010070006003200080060500009004000030000009700'
B3_filled = make_board(sudoku_grid_hardest)

#print(solve(B3_filled))

#sudoku_grid_impossible = [1, 2, 3, 4, 5, 6, 7, 8, 0,
                         # 0, 0, 0, 0, 0, 0, 0, 0, 2,
                         # 0, 0, 0, 0, 0, 0, 0, 0, 3,
                         # 0, 0, 0, 0, 0, 0, 0, 0, 4,
                         # 0, 0, 0, 0, 0, 0, 0, 0, 5,
                         # 0, 0, 0, 0, 0, 0, 0, 0, 6,
                         # 0, 0, 0, 0, 0, 0, 0, 0, 7,
                         # 0, 0, 0, 0, 0, 0, 0, 0, 8,
                         # 0, 0, 0, 0, 0, 0, 0, 0, 9]
sudoku_grid_impossible = '123456780000000002000000003000000004000000005000000006000000007000000008000000009'
B4_filled = make_board(sudoku_grid_impossible)

#print(solve(B4_filled)) no solution
