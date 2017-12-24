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

def build_peers(board):
    '''
    board -> dictionary of board with values as a list of peers
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

    
def keep_valid(board):
    '''
    listofboards -> listofboards
    check each board units to see if it is valid
    '''
    filled = fill_square(board)
    
    peers_board = {}
    for i in range(0, (len(filled))): #iterating through list of dict
        peers_board = build_peers(filled[i])
        current_board = filled[i]
        for k in current_board.keys(): #dict
            if current_board[k] != 0 and current_board[k] in peers_board[k]:
                del filled[i]
        
    return filled
                        
def generate_possible_boards(filled):
    '''
    produce list of possible boards, keeps only valid boards
    '''
    
    return keep_valid(filled)
    
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
    rows = 'ABCDEFGHI'
    cols = '123456789'
    squares = cross(rows, cols)
    
    board = make_board(grid)
    
    generate_possible_boards(board)
            


sudoku_grid_easy2 = [2, 7, 4, 0, 9, 1, 0, 0, 5, 
                     1, 0, 0, 5, 0, 0, 0, 9, 0,
                     6, 0, 0, 0, 0, 3, 2, 8, 0,
                     0, 0, 1, 9, 0, 0, 0, 0, 8,
                     0, 0, 5, 1, 0, 0, 6, 0, 0,
                     7, 0, 0, 0, 8, 0, 0, 0, 3,
                     4, 0, 2, 0, 0, 0, 0, 0, 9,
                     0, 0, 0, 0, 0, 0, 0, 7, 0,
                     8, 0, 0, 3, 4, 9, 0, 0, 0]

for i in range(len(sudoku_grid_easy2)):
    sudoku_grid_easy2[i] = str(sudoku_grid_easy2[i])
    
B1 = ''.join(sudoku_grid_easy2)

B1_filled = make_board(B1)

print(keep_valid(B1_filled))

