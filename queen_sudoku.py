######################################################
###### Solve a Queen Sudoku
###### You cannot have the 9 appear twice in a Queen's move
######################################################

# INSERT SUDOKU GRID HERE
sudoku_grid = [
[0, 8, 0, 7, 0, 0, 0, 0, 2],
[0, 0, 0, 0, 2, 8, 0, 4, 0],
[0, 0, 6, 0, 0, 0, 0, 0, 8],
[0, 0, 0, 0, 4, 0, 0, 0, 1],
[0, 1, 0, 0, 5, 0, 0, 3, 0],
[2, 0, 0, 0, 7, 0, 0, 0, 0],
[7, 0, 0, 0, 0, 0, 3, 0, 0],
[0, 3, 0, 6, 9, 0, 0, 0, 0],
[6, 0, 0, 0, 0, 7, 0, 1, 0]
]

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

queen_sudoku = True

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

    # Custom sudoku rule: Queen Sudoku 
    if queen_sudoku:
        if n == 9:
            queen_move = [ ]
            # North-west direction
            x0 = x
            y0 = y
            while (x0 >=0) and (y0 >0):
                x0 -= 1
                y0 -= 1
                if (x_0 >= 0) and (y0 >= 0):
                    queen_move.append( [x0, y0] )
            # North-east direction
            x0 = x
            y0 = y
            while (x0 >=0) and (y0 >0):
                x0 += 1
                y0 -= 1
                if (x_0 >= 0) and (y0 >= 0):
                    queen_move.append( [x0, y0] )
            # South-west direction
            x0 = x
            y0 = y
            while (x0 >=0) and (y0 >0):
                x0 -= 1
                y0 += 1
                if (x_0 >= 0) and (y0 >= 0):
                    queen_move.append( [x0, y0] )
            # South-east direction
            x0 = x
            y0 = y
            while (x0 >=0) and (y0 >0):
                x0 += 1
                y0 += 1
                if (x_0 >= 0) and (y0 >= 0):
                    queen_move.append( [x0, y0] )

            for element in queen_move:
                if element[0] in [0,1,2,3,4,5,6,7,8]:
                        if element[1] in [0,1,2,3,4,5,6,7,8]:
                            if sudoku_grid[ element[1] ][ element[0] ] == n:
                                return False

    return True


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
