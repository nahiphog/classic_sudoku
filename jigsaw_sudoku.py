# INPUT JIGSAW SUDOKU VALUES HERE
nil_1 = ' ----------------------- '
row_1 = ' | _ _ _ _ _ _ _ _ _ | '
row_2 = ' | _ _ _ _ _ _ _ _ _ | '
row_3 = ' | _ _ _ _ _ _ _ _ _ | '
row_4 = ' | _ _ _ _ _ _ _ _ _ | '
row_5 = ' | _ _ _ _ _ _ _ _ _ | '
row_6 = ' | _ _ _ _ _ _ _ _ _ | '
row_7 = ' | _ _ _ _ _ _ _ _ _ | '
row_8 = ' | _ _ _ _ _ _ _ _ _ | '
row_9 = ' | _ _ _ _ _ _ _ _ _ | '
nil_2 = ' ----------------------- '

sudoku_grid = [] ; possible_numbers =  [ f'{integer}' for integer in range(10)]

for index in range(9): # Construct the sudoku grid
    this_row = eval('row_' + str(index + 1) )
    text = list(this_row)
    add_this_grid = []
    for each_entry in text:
        if each_entry == '_': add_this_grid.append(0)
        elif each_entry in possible_numbers: add_this_grid.append(int(each_entry))
    sudoku_grid.append(add_this_grid)

############ INPUT JIGSAW GRIDS HERE
jigsaw_input = [
    # 1:
    [11,12,21,22,23,24,31,34,35],
    # 2:
    [13,14,15,16,17,18,19,25,26],
    # 3:
    [27,28,29,36,37,38,39,47,49],
    # 4:
    [32,41,42,51,52,61,71,81,91],
    # 5:
    [33,43,44,45,46,55,56,65,66],
    # 6:
    [48,57,58,59,67,77,87,86,85],
    # 7:
    [53,54,62,63,64,72,82,83,92],
    # 8:
    [73,74,75,76,93,94,95,96,84],
    # 9:
    [68,69,78,79,88,89,98,99,97]
]
 
jigsaw_readables = [] 
for element in jigsaw_input:
    convert_to_grid_positions = [] ; this_jigsaw = []

    for item in element:
        read_this = list(str(item))

        this_position = 'sudoku_grid'
        for item in read_this:
            this_position += '[' + str(int(item) - 1) + ']'
        
        this_jigsaw.append(this_position)
    
    jigsaw_readables.append(this_jigsaw)

# Backtracking function
def possible_movement(x,y,n):
    global sudoku_grid, jigsaw_readables

    # Jigsaw rules
    read_these_jigsaws = []

    for this_very_jigsaw in jigsaw_readables:
        add_this_jigsaw = []
        for item in this_very_jigsaw:
            if eval(item) == 0: continue
            else: add_this_jigsaw.append(eval(item))
        
        read_these_jigsaws.append(add_this_jigsaw)
    
    # Jigsaw rule: All the numbers inside each Jigsaw grid must be distinct
    for this_very_jigsaw in read_these_jigsaws:
        for integer in range(1,9 + 1):
            if this_very_jigsaw.count(integer) > 1: return False


    # Sudoku rule 1: Check whether whether N has appeared in that column
    for i in range(9):
        if sudoku_grid[y][i] == n:
            return False
    
    # Sudoku rule 2: Check whether whether N has appeared in that row
    for i in range(9):
        if sudoku_grid[i][x] == n:
            return False
    return True

def print_jigsaw_result():
    print("")
    row_number = 0
    print("---------------------")
    for row in sudoku_grid:
        print("|", end = ' ')
        column_number = 0
        for item in row:
            print(item, end=' ')
            column_number += 1
        print("|", end = ' ')
        print("")
        row_number += 1
    print("---------------------")

# Satisfied conditions?
all_integers_grids = []
for item in jigsaw_input:
    for integer in item: all_integers_grids.append(integer)

verified_conditions = True
for integer_check in range(11, 99 + 1):
    if integer_check % 10 == 0: continue
    else:
        if integer_check not in all_integers_grids:
            print("Not a valid Jigsaw grid")
            verified_conditions = False
            break

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

    print_jigsaw_result()

if verified_conditions == True: 
    solve_this_sudoku()
