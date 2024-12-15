# copy over your a1_partd.py file here

#    Main Author(s): Mohdeep Singh
#    Main Reviewer(s): Ayush Patel, Archi Mukeshbhai Kakadiya 


import copy
from a1_partc import Queue


def get_overflow_list(grid):
    """ Identifies which cells in the grid are overflowing.

This function goes through each cell in the grid and checks if its value (ignoring the sign) is equal to or larger than the number of neighboring cells. If it is, that cell is added to a list of overflowing cells.

It takes a 2D grid (a list of lists) with integers as input.

The function returns a list of (i, j) coordinates for the overflowing cells. If no cells are overflowing, it returns None. """
    max_row, max_col = len(grid), len(grid[0])
    overflow_list = []

    for i in range(max_row):
        for j in range(max_col):
            # Determine number of neighbors based on the position of the cell
            if (i == 0 or i == max_row - 1) and (j == 0 or j == max_col - 1):
                neighbors = 2  # Corner cells
            elif i == 0 or i == max_row - 1 or j == 0 or j == max_col - 1:
                neighbors = 3  # Edge cells
            else:
                neighbors = 4  # Internal cells
            
            if abs(grid[i][j]) >= neighbors:
                overflow_list.append((i, j))    
                
    return overflow_list if overflow_list else None


def overflow(grid, a_queue, grid_count=0):
    """
    Handles the overflow process and updates the grid accordingly.
    
    This function perform an overflow process. 
    The function recursively updates the grid and adds the new grids to the queue until 
    no further overflow can occur.
    
    grid: A 2D grid where each cell contains an integer.
    a_queue: A queue to store each state of the grid during the overflow process.
    grid_count: A counter to track the number of grid states processed.
    
    It returns the total number of grid states processed during the overflow process.
    """    
    overflow_list = get_overflow_list(grid)
    
    if overflow_list and not is_all_same_sign(grid):
        overflowing_sign = grid[overflow_list[0][0]][overflow_list[0][1]] // abs(grid[overflow_list[0][0]][overflow_list[0][1]])

        # Overflowing cells distribute their value to neighbors and become 0
        for (x, y) in overflow_list:
            grid[x][y] = 0
        
        for (x, y) in overflow_list:
            for (i, j) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if (i in range(len(grid)) and j in range(len(grid[0]))):
                    grid[i][j] = (abs(grid[i][j]) + 1) * overflowing_sign
        
        # Add the new grid state to the queue
        a_queue.enqueue(copy.deepcopy(grid))
        grid_count += 1

        # Continue the overflow process if there are still overflowing cells
        if get_overflow_list(grid):
            grid_count += overflow(grid, a_queue)
        
    return grid_count
                                     

def is_all_same_sign(grid):
    """
    Determines if all non-zero elements in the grid have the same sign.
    
    This function checks each cell in the grid and returns True if all non-zero
    cells have the same sign, and False otherwise.
    
    grid: A 2D grid where each cell contains an integer.
    
    It returns True if all non-zero cells have the same sign, and False otherwise.
    """    
    sign = None
    same_sign = True

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if sign and grid[i][j] != 0:
                if sign != grid[i][j] // abs(grid[i][j]):
                    same_sign = False
                    break
            if grid[i][j] != 0:
                sign = grid[i][j] // abs(grid[i][j])
            
    return same_sign