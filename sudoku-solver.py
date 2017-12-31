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

    
def keep_valid(board, sq_filled):
    '''
    listofboards key -> listofboards
    check each board units to see if it is valid
    '''
    filled = fill_square(board)
    to_remove = []
    
    for i in range(0, len(filled)): #iterating through list of dict
        peers_board = build_peers(filled[i])
        current_board = filled[i]
        for k in current_board.keys(): #dict
            if k == sq_filled and current_board[k] in peers_board[k]: #if current square empty, next board
                to_remove.append(current_board)
    
    for i in to_remove:
        filled.remove(i)
                 
    return filled
                            
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

def solve(grid):
    '''
    grid is string with values of 0-9, 0 meaning empty square on sudoku board
    '''
    
    board = make_board(grid)
    
    branch = keep_valid(board, sq_filled)
    
    while len(branch) > 0:
    
        if len(branch) == 1:
            print(branch)
        
        else:
            for i in branch:
                b = fill_square(i)
                new_branch = keep_valid(b[0], b[1])
                if len(new_branch) == 1:
                    print(new_branch)

    return "No solution"
        
       
