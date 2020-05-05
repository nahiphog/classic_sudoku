from numpy import array

grid_size = 4

kenken_grid = [ [0 for index in range(grid_size)] for rows in range(grid_size) ]

# Backtracking function
def possible_movement(x,y,n):
    global kenken_grid
    # Kenken rule 1: Check whether whether N has appeared in that column
    for i in range(grid_size):
        if kenken_grid[y][i] == n: return False
    
    # Kenken rule 2: Check whether whether N has appeared in that row
    for i in range(grid_size):
        if kenken_grid[i][x] == n: return False
    return True

def solve_this_kenken():
    global kenken_grid
    for y in range(0, grid_size):
        for x in range(0, grid_size):
            if kenken_grid[y][x] == 0:
                for n in range(1,grid_size + 1):
                    if possible_movement(x,y,n):
                        kenken_grid[y][x] = n
                        solve_this_kenken()
                        kenken_grid[y][x] = 0
                return


    # Show solution if answer is satisfied:

    if (kenken_grid[0][0] + kenken_grid[0][1] + kenken_grid[1][0] == 10):
        if ( kenken_grid[0][2] + kenken_grid[0][3] + kenken_grid[1][3] == 5):
            if ( kenken_grid[1][1] + kenken_grid[1][2] + kenken_grid[2][1] + kenken_grid[2][2] == 10):
                if ( kenken_grid[2][0] + kenken_grid[3][0] + kenken_grid[3][1] == 6):
                    if ( kenken_grid[2][3] + kenken_grid[3][2] + kenken_grid[3][3] == 9):
                        print(array(kenken_grid))

solve_this_kenken()

# Output:

# [[2 4 1 3]
#  [4 3 2 1]
#  [3 1 4 2]
#  [1 2 3 4]]
