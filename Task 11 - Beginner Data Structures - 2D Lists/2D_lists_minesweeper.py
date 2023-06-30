"""
Minesweeper Grid Checker

This script contains a function that takes a 2D list representing a 
Minesweeper game grid.

"-" represents an empty cell, "#" represents a mine.

A new grid will be generated that identifies the number of mines adjacent to 
an empty cell while retaining the position of each mine.
"""

def minesweeper(grid):
    """
    This function takes a Minesweeper grid as input, and generates a new grid
    that shows the number of mines adjacent to each square.

    Args:
        grid (list): A 2D list representing the Minesweeper game grid.
        Each cell in the grid is either a "-" (empty) or a "#" (mine).

    Returns:
        list: A 2D list with the same dimensions as the input, where each cell
        is either a "#" (indicating a mine) or a digit (indicating the number 
        of adjacent mines).
    """
    # Determine the number of rows and columns in the input grid.
    rows = len(grid)
    columns = len(grid[0])
    # Empty list to hold output grid.
    result_grid = []
    # Iterates over each row of the input grid using enumerate() to keep track
    # of the row index and its corresponding cells.
    for row, row_cells in enumerate(grid):
        # Empty list to hold rows of output grid.
        result_row = []
        # Iterates over each column of the input grid using enumerate() to 
        # keep track of the column index and its corresponding cell.
        for column, cell in enumerate(row_cells):
            # If current cell of input grid is a mine, adds "#" to current row
            # in output row list.
            if cell == "#":
                result_row.append("#")
        
            else:
                # Counter starts at 0.
                mine_count = 0
                # Iterates over the cells adjacent to the current cell in the
                # input grid, counting the number of mines.
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        # Ensures cells are within the boundaries of the 
                        # input grid.
                        if 0 <= row + i < rows and 0 <= column + j < columns:
                            # Increments the counter if an adjacent cell
                            # contains a mine.
                            if grid[row + i][column + j] == "#":
                                mine_count += 1
                # Adds mine count to current row of the output grid.
                result_row.append(str(mine_count))
        # Adds the current row to the output grid.
        result_grid.append(result_row)
    # Returns output grid.
    return result_grid

# Input grid.
grid = [
    ["-", "-", "-", "#", "#"],  
    ["-", "#", "-", "-", "-"], 
    ["-", "-", "#", "-", "-"], 
    ["-", "#", "#", "-", "-"], 
    ["-", "-", "-", "#", "#"], 
    ["-", "-", "-", "-", "-"], 
    ["-", "-", "#", "-", "-"], 
    ["-", "#", "-", "-", "-"], 
    ["-", "-", "-", "-", "#"], 
    ["-", "#", "#", "-", "-"]
    ]
# Calls function to iterate over input grid.
result_grid = minesweeper(grid)
# Displays grid row by row for easier readability.
for row in result_grid:
    print(row)