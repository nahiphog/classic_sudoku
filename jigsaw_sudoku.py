############################## NOT COMPLETE

# INPUT SUDOKU GRID HERE
nil_1 = ' --------------------- '
row_1 = ' | _ _ _ _ _ _ _ _ _ | '
row_2 = ' | _ _ _ _ _ _ _ _ _ | '
row_3 = ' | _ _ _ _ _ _ _ _ _ | '
row_4 = ' | _ _ _ _ _ _ _ _ _ | '
row_5 = ' | _ _ _ _ _ _ _ _ _ | '
row_6 = ' | _ _ _ _ _ _ _ _ _ | '
row_7 = ' | _ _ _ _ _ _ _ _ _ | '
row_8 = ' | _ _ _ _ _ _ _ _ _ | '
row_9 = ' | _ _ _ _ _ _ _ _ _ | '
nil_2 = ' --------------------- '

##################

sudoku_grid , possible_numbers = [], [ f'{integer}' for integer in range(10)]

for index in range(9):
    this_row = eval('row_' + str(index + 1) )
    text = list(this_row)
    add_this_grid = []
    for each_entry in text:
        if each_entry in possible_numbers: add_this_grid.append(int(each_entry))
    sudoku_grid.append(add_this_grid)

# print(sudoku_grid)

##################

jigsaw_grid_1 = [ 11, 12, 13, 21, 22, 23, 31, 32, 33]
jigsaw_grid_2 = [ 14, 15, 24, 34, 44, 41, 42, 43, 51]
jigsaw_grid_3 = [ 16,17,18,19, 25,26,27,28,37]
jigsaw_grid_4 = [29, 36, 38,39, 46, 47,48,49,58]
jigsaw_grid_5 = [35, 45,55, 53,54, 56,57,65,75]
jigsaw_grid_6 = [52, 61, 62,63,64,71,72, 74, 81]
jigsaw_grid_7 = [59,66,67,68,69,76,86,96,95]
jigsaw_grid_8 = [73,82,83,84,85,91,92,93,94]
jigsaw_grid_9 = [77,78,79,87,88,89,97,98,99]

jigsaw_grids_combined = []

def jigsaw_it():
    global jigsaw_grids_combined

    for grid_number in range(1, 9 + 1):
        this_grid = 'jigsaw_grid_' + str(grid_number)
        join_the_values = []

        for element in eval(this_grid):
            this_cell = str(element)
            this_string = 'sudoku_grid' + f'[{eval(this_cell[0]) - 1}]' + f'[{eval(this_cell[1]) - 1}]'
            join_the_values.append(eval(this_string))

        jigsaw_grids_combined.append(join_the_values)

# print(jigsaw_grids_combined)

# jigsaw_it()

# print(jigsaw_grids_combined)

# sudoku_grid[0][0] sudoku_grid[0][1] sudoku_grid[0][2] sudoku_grid[1][0] sudoku_grid[1][1] sudoku_grid[1][2] sudoku_grid[2][0] sudoku_grid[2][1] sudoku_grid[2][2]
# sudoku_grid[0][3] sudoku_grid[0][4] sudoku_grid[1][3] sudoku_grid[2][3] sudoku_grid[3][3] sudoku_grid[3][0] sudoku_grid[3][1] sudoku_grid[3][2] sudoku_grid[4][0]
# sudoku_grid[0][5] sudoku_grid[0][6] sudoku_grid[0][7] sudoku_grid[0][8] sudoku_grid[1][4] sudoku_grid[1][5] sudoku_grid[1][6] sudoku_grid[1][7] sudoku_grid[2][6]
# sudoku_grid[1][8] sudoku_grid[2][5] sudoku_grid[2][7] sudoku_grid[2][8] sudoku_grid[3][5] sudoku_grid[3][6] sudoku_grid[3][7] sudoku_grid[3][8] sudoku_grid[4][7]
# sudoku_grid[2][4] sudoku_grid[3][4] sudoku_grid[4][4] sudoku_grid[4][2] sudoku_grid[4][3] sudoku_grid[4][5] sudoku_grid[4][6] sudoku_grid[5][4] sudoku_grid[6][4]
# sudoku_grid[4][1] sudoku_grid[5][0] sudoku_grid[5][1] sudoku_grid[5][2] sudoku_grid[5][3] sudoku_grid[6][0] sudoku_grid[6][1] sudoku_grid[6][3] sudoku_grid[7][0]
# sudoku_grid[4][8] sudoku_grid[5][5] sudoku_grid[5][6] sudoku_grid[5][7] sudoku_grid[5][8] sudoku_grid[6][5] sudoku_grid[7][5] sudoku_grid[8][5] sudoku_grid[8][4]
# sudoku_grid[6][2] sudoku_grid[7][1] sudoku_grid[7][2] sudoku_grid[7][3] sudoku_grid[7][4] sudoku_grid[8][0] sudoku_grid[8][1] sudoku_grid[8][2] sudoku_grid[8][3]
# sudoku_grid[6][6] sudoku_grid[6][7] sudoku_grid[6][8] sudoku_grid[7][6] sudoku_grid[7][7] sudoku_grid[7][8] sudoku_grid[8][6] sudoku_grid[8][7] sudoku_grid[8][8]


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
    
    # # Sudoku rule 3: Check whether N has appeared in that 3x3 block
    # x0 = (x//3) * 3
    # y0 = (y//3) * 3
    # for i in range(0,3):
    #     for j in range(0,3):
    #         if sudoku_grid[y0 + i][x0 + j] == n:
    #             return False
            
    return True

def print_nice_result():
    global jigsaw_grids_combined
    print("")
    row_number = 0
    print("---------------------")
    for row in sudoku_grid:
        print("|" , end = ' ')
        column_number = 0
        for item in row:
            print(item, end=' ')
            column_number += 1
            # if column_number % 3 == 0:
            #     print("|", end= ' ')
        print("")
        row_number += 1
        # if row_number % 3 == 0:
    print("---------------------")


qqqqqqq = 0
def solve_this_sudoku():
    global sudoku_grid, jigsaw_grids_combined, qqqqqqq
    for y in range(0, 8 + 1):
        for x in range(0, 8 + 1):
            if sudoku_grid[y][x] == 0:
                for n in range(1,9+1):
                    if possible_movement(x,y,n):
                        sudoku_grid[y][x] = n
                        solve_this_sudoku()
                        sudoku_grid[y][x] = 0
                return

    qqqqqqq += 1

    print(qqqqqqq, end = '\t')
    # jigsaw_grids_combined = []
    # jigsaw_it()

    
    # all_lengths = [ len(set(element)) for element in jigsaw_grids_combined ]

    # if all_lengths.count(9) == 9: print_nice_result()

solve_this_sudoku()

print(qqqqqqq)
