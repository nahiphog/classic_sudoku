empty_grid = [
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

#######################

# Input Sudoku grid here
raw_sudoku_grid_01 = ' ------------------------- '
raw_sudoku_grid_02 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
raw_sudoku_grid_03 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
raw_sudoku_grid_04 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
raw_sudoku_grid_05 = ' ------------------------- '
raw_sudoku_grid_06 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
raw_sudoku_grid_07 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
raw_sudoku_grid_08 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
raw_sudoku_grid_09 = ' ------------------------- '
raw_sudoku_grid_10 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
raw_sudoku_grid_11 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
raw_sudoku_grid_12 = ' | 0 0 0 | 0 0 0 | 0 0 0 | '
raw_sudoku_grid_13 = ' ------------------------- '

text = raw_sudoku_grid_02.split()

relevant_rows = [ raw_sudoku_grid_02, raw_sudoku_grid_03, raw_sudoku_grid_04, 
                 raw_sudoku_grid_06, raw_sudoku_grid_07, raw_sudoku_grid_08, 
                 raw_sudoku_grid_10, raw_sudoku_grid_11, raw_sudoku_grid_12 ]

sudoku_grid = []

possible_numbers = [ f'{integer}' for integer in range(10)]
for element in relevant_rows:
    text = list(element)
    add_this_grid = []
    for each_entry in text:
        if each_entry in possible_numbers :
            add_this_grid.append(int(each_entry))
    sudoku_grid.append(add_this_grid)
