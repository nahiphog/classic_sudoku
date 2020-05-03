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
row_1 = ' | _ _ _ | _ _ _ | _ _ _ | '
row_2 = ' | _ _ _ | _ _ _ | _ _ _ | '
row_3 = ' | _ _ _ | _ _ _ | _ _ _ | '
nil_2 = ' ------------------------- '
row_4 = ' | _ _ _ | _ _ _ | _ _ _ | '
row_5 = ' | _ _ _ | _ _ _ | _ _ _ | '
row_6 = ' | _ _ _ | _ _ _ | _ _ _ | '
nil_3 = ' ------------------------- '
row_7 = ' | _ _ _ | _ _ _ | _ _ _ | '
row_8 = ' | _ _ _ | _ _ _ | _ _ _ | '
row_9 = ' | _ _ _ | _ _ _ | _ _ _ | '
nil_4 = ' ------------------------- '

sudoku_grid , possible_numbers = [], [ f'{integer}' for integer in range(10)]

for index in range(9):
    this_row = eval('row_' + str(index + 1) )
    text = list(this_row)
    add_this_grid = []
    for each_entry in text:
        if each_entry == '_': add_this_grid.append(0)
        elif each_entry in possible_numbers: add_this_grid.append(int(each_entry))
    sudoku_grid.append(add_this_grid)
