''' https://brilliant.org/daily-problems/757/
2020-07-21 10:52:57
'''
from numpy import array
from itertools import product
from math import prod

grid_size = 4

kenken_grid = [ [0 for index in range(grid_size)] for rows in range(grid_size) ]

def addition_function(addition_entries, desired_sum):
    if sum(addition_entries) == desired_sum: return True
    else: return False

def multiplication_function(multiplication_entries, desired_product):
    if prod(multiplication_entries) == desired_product: return True
    else: return False

def subtraction_function(subtraction_entries, desired_reduction):
    if abs(subtraction_entries[0] - subtraction_entries[1] ) == desired_reduction: return True
    else: return False

def division_function(divided_entries, desired_ratio):
    if divided_entries[0] / divided_entries[1] == desired_ratio: return True
    elif divided_entries[1] / divided_entries[0] == desired_ratio: return True
    else: return False

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
    if ( subtraction_function([kenken_grid[0][3], kenken_grid[1][3]], 1) ):
        if ( subtraction_function([kenken_grid[2][3], kenken_grid[3][3]], 1) ):
            if ( addition_function([kenken_grid[3][0], kenken_grid[3][1], kenken_grid[3][2]], 9) ):   

                if (multiplication_function([ kenken_grid[0][0], kenken_grid[0][1], kenken_grid[0][2], kenken_grid[1][0], kenken_grid[1][1] , kenken_grid[2][0] ], 64)):

                    print(array(kenken_grid), '\n')
                    
                    diagonal_sum = sum( kenken_grid[k][k] for k in range(0, 3 + 1))
                    print(f"The diagonal sum is {diagonal_sum}.")

solve_this_kenken()

# Output:
# [[2 1 4 3]
#  [1 2 3 4]
#  [4 3 1 2]
#  [3 4 2 1]]

# The diagonal sum is 6.
