"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    count_empty_cells = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY : count_empty_cells += 1
    
    if count_empty_cells == 0 : 
        return None
    elif count_empty_cells % 2 == 1: 
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY : actions.add((i,j))

    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    board_copy = copy.deepcopy(board)

    if board_copy[action[0]][action[1]] != EMPTY:
        raise Exception('Invalid Move: Cell is not empty')
    
    board_copy[action[0]][action[1]] = player(board)
    
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    winning_arrangements = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]]

    winner = None
    for arr in winning_arrangements:
        winner = get_cell_value(board, arr[0])
        if get_cell_value(board, arr[1]) != winner or get_cell_value(board, arr[2]) != winner:
            winner = None
        else:
            return winner
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    sum_empty_cells = sum(row.count(EMPTY) for row in board)

    if winner(board) != None or sum_empty_cells == 0:
        return True

    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # score = 0
    win = winner(board)

    if win == X: return 1
    if win == O: return -1

    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError


def get_cell_value(board, coordinates):
    """
    Returns the value in a cell of the board, based on a coordinates tuple (i,j).
    """
    #Improvement Add Checks on coordinates

    return board[coordinates[0]][coordinates[1]]