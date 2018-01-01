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
            

#examples

#sudoku_grid_easy =  [2, 7, 4, 0, 9, 1, 0, 0, 5, 
                    # 1, 0, 0, 5, 0, 0, 0, 9, 0,
                    # 6, 0, 0, 0, 0, 3, 2, 8, 0,
                    # 0, 0, 1, 9, 0, 0, 0, 0, 8,
                    # 0, 0, 5, 1, 0, 0, 6, 0, 0,
                    # 7, 0, 0, 0, 8, 0, 0, 0, 3,
                    # 4, 0, 2, 0, 0, 0, 0, 0, 9,
                    # 0, 0, 0, 0, 0, 0, 0, 7, 0,
                    # 8, 0, 0, 3, 4, 9, 0, 0, 0]

sudoku_grid_easy = make_board(B1)
B1_filled = make_board(sudoku_grid_easy)

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

#print(solve(B2_filled).values())
#produces
#'5', '3', '9', '1', '6', '4', '8', '7', '2', '8', '1', '2', '7', '5', '3', '6', '9', '4', '6', '7', '4', '9', '2', '8', '3', '1', '5', '2', '9', '6', '4', '1', '7', '5', '8', '3', '1', '8', '7', '2', '3', '5', '9', '4', '6', '3', '4', '5', '8', '9', '6', '1', '2', '7', '9', '2', '3', '5', '4', '1', '7', '6', '8', '7', '6', '1', '3', '8', '2', '4', '5', '9', '4', '5', '8', '6', '7', '9', '2', '3', '1'

#sudoku_grid_impossible = 
sudoku_grid_impossible = '123456780000000002000000003000000004000000005000000006000000007000000008000000009'
B3_filled = make_board(sudoku_grid_impossible)

#print(solve(B3_filled)) no solution
