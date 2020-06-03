######################################################
###### Solve any KenKen by backtracking
######################################################
from numpy import prod

kenken_size = 3

# INPUT KENKEN GRID HERE
kenken_grid = [ [0 for _ in range(kenken_size)] for index in range(kenken_size)] 

# Input operator, output, cells involved (row number followed by column number)
kenken_cages = [
    [  '/' , 3, [11, 12] ],
    [ '-' , 1, [13, 23] ],
    [ '-', 1, [21, 31] ],
    [ '-', 1, [32, 33] ]
]

valid_kenken_grid = True
for element in kenken_cages:
    if element[0] == '-' or element[0] == '/':
        if not(len(element[2]) == 2):
            print("Not a valid Kenken grid.")
            valid_kenken_grid = False
            break

# Backtracking function
def possible_movement(x,y,n):
    global kenken_grid

    # Kenken rule 1: Check whether whether N has appeared in that row
    for i in range(kenken_size):
        if kenken_grid[y][i] == n: return False
    
    # Kenken rule 2: Check whether whether N has appeared in that column
    for i in range(kenken_size):
        if kenken_grid[i][x] == n: return False

    # Kenken rules 3: Check whether the rules are satisfied
    for element in kenken_cages:
        this_operator = element[0] ; this_resultant = element[1] ; these_cells = element[2]

        readable_cells = []
        for item in these_cells:
            this_string = 'kenken_grid'

            this_row_number = item // 10 - 1 ; this_column_number = item % 10 - 1

            this_string += '[' + str(this_row_number) + '][' + str(this_column_number) + ']'

            readable_cells.append(eval(this_string))

        # We need to make sure all the cells in this cage is fulfilled
        if 0 not in readable_cells:
            if this_operator == '+':
                if not( sum(readable_cells) == this_resultant):
                    return False

            if this_operator == '-':
                if ( (readable_cells[0] - readable_cells[1]) == this_resultant) and not( (readable_cells[1] - readable_cells[0]) == this_resultant): 
                    return False

            if this_operator == '*':
                if not( prod(readable_cells) == this_resultant):
                    return False
            
            if this_operator == "/":
                if not( (readable_cells[0] / readable_cells[1]) == this_resultant) and ( not( (readable_cells[1] / readable_cells[0]) == this_resultant) ):
                    return False
           
    return True

def print_nice_result():
    def horizontal_bar_length():
        length = 3 + (kenken_size * 2)
        for integer in range(length): print("-", end='')
        print("")
    print("")

    def print_vertical_bar(): print("|", end = ' ')

    horizontal_bar_length()
    for row in kenken_grid:
        print_vertical_bar()
        for item in row:
            print(item, end=' ')
        print_vertical_bar()
        print("")
    horizontal_bar_length()

def solve_this_kenken():
    global kenken_grid
    for y in range(0, kenken_size):
        for x in range(0, kenken_size):
            if kenken_grid[y][x] == 0:
                for n in range(1,kenken_size+1):
                    if possible_movement(x,y,n):
                        kenken_grid[y][x] = n
                        solve_this_kenken()
                        kenken_grid[y][x] = 0
                return

    print_nice_result()

if valid_kenken_grid == True: solve_this_kenken()
