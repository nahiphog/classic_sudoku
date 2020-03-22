x_sudoku = True

# Backtracking function
def possible_movement(x,y,n):
    global sudoku_grid

    # Sudoku rule 1: Check whether whether N has appeared in that column
    for i in range(9):
        if sudoku_grid[y][i] == n:
            return False
    
    # Sudoku rule 2: Check whether whether N has appeared in that row
    for i in range(9):
        if sudoku_grid[i][x] == n:
            return False
    
    # Sudoku rule 3: Check whether N has appeared in that 3x3 block
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku_grid[y0 + i][x0 + j] == n:
                return False

    # Custom sudoku rule (1): X-sudoku: Check whether the cell is in one of the diagonals. If yes, check whether N has has appeared in its respective diagonal(s)
    if x_sudoku:
        # Check whether its in the main diagonal
        if (x == y):
            diagonal_list = [ sudoku_grid[position][position] for position in range(0, 8 + 1) ]
            if n in diagonal_list:
                return False
        # Check whether its in the main diagonal
        if (x + y == 8):
            anti_diagonal_list = [ sudoku_grid[position][8 - position] for position in range(0,8 + 1) ]
            if n in anti_diagonal_list:
                return False
            
    return True
