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
