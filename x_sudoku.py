######################################################
###### Solve a Knight Sudoku
###### The two longest diagonals must all contain the digits 1 to 9
######################################################

# INSERT SUDOKU GRID HERE
sudoku_grid = [
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]
]

knight_sudoku = True

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

    # Custom sudoku rule: X-sudoku
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

def print_nice_result():
    print("")
    row_number = 0
    print("-------------------------")
    for row in sudoku_grid:
        print("|" , end = ' ')
        column_number = 0
        for item in row:
            print(item, end=' ')
            column_number += 1
            if column_number % 3 == 0:
                print("|", end= ' ')
        print("")
        row_number += 1
        if row_number % 3 == 0:
            print("-------------------------")



def solve_this_sudoku():
    global sudoku_grid
    for y in range(0, 8 + 1):
        for x in range(0, 8 + 1):
            if sudoku_grid[y][x] == 0:
                for n in range(1,9+1):
                    if possible_movement(x,y,n):
                        sudoku_grid[y][x] = n
                        solve_this_sudoku()
                        sudoku_grid[y][x] = 0
                return

    print_nice_result()

solve_this_sudoku()
