######################################################
###### Solve a King Sudoku
###### You cannot have the same number twice within a King's move
######################################################

# INPUT SUDOKU GRID HERE
nil_1 = ' ------------------------- '
row_1 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
row_2 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
row_3 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
nil_2 = ' ------------------------- '
row_4 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
row_5 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
row_6 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
nil_3 = ' ------------------------- '
row_7 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
row_8 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
row_9 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
nil_4 = ' ------------------------- '

sudoku_grid , possible_numbers = [], [ f'{integer}' for integer in range(10)]

for index in range(9):
    this_row = eval('row_' + str(index + 1) )
    text = list(this_row)
    add_this_grid = []
    for each_entry in text:
        if each_entry in possible_numbers: add_this_grid.append(int(each_entry))
    sudoku_grid.append(add_this_grid)

king_sudoku = True

# Backtracking function
def possible_movement(x,y,n):
    global sudoku_grid

    # Sudoku rule 1: Check whether whether N has appeared in that row
    for i in range(9):
        if sudoku_grid[y][i] == n:
            return False
    
    # Sudoku rule 2: Check whether whether N has appeared in that column
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

    # Custom sudoku rule: King Sudoku 
    if king_sudoku:
        knight_move = [ [x + 1, y + 1], [x + 1 , y - 1] , [x - 1, y + 1], [x - 1, y - 1], 
                       [x + 1, y + 1], [x + 1 , y - 1] , [x - 1, y + 1], [x - 1, y - 1] ]
        for element in knight_move:
            if element[0] in [0,1,2,3,4,5,6,7,8]:
                    if element[1] in [0,1,2,3,4,5,6,7,8]:
                        if sudoku_grid[ element[1] ][ element[0] ] == n:
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
