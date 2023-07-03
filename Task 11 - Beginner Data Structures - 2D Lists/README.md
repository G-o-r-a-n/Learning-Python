# Task 11 - Beginner Data Structures - 2D Lists

This Python script creates a new grid from an input grid for a minesweeper game. The input grid consists of '-' and '#', where each '#' represents a mine, and each '-' represents a mine-free spot. The generated grid replaces each '-' with a digit, indicating the number of mines immediately adjacent to the spot (horizontally, vertically, and diagonally).

## Objective:

The main objectives of this task are:

1. Create a function that takes a grid of '#' and '-', where each hash ('#') represents a mine and each dash ('-') represents a mine-free spot.
1. Return a grid where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot (horizontally, vertically, and diagonally).
1. Handle boundary conditions effectively to prevent index errors.

The Python script that accomplishes this can be found in the file: [2D_lists_minesweeper.py](https://github.com/G-o-r-a-n/Learning-Python/blob/main/Task%2011%20-%20Beginner%20Data%20Structures%20-%202D%20Lists/2D_lists_minesweeper.py).

## Code Explained:

The script executes the following steps:

- **Define Function**: The `minesweeper(grid)` function is defined to iterate over the input grid and generate a new grid that shows the number of mines adjacent to each square.
- **Handle Boundary Conditions**: The function has provisions to handle the edges of the grid and prevent index out-of-range errors by ensuring cells are within the boundaries of the input grid.
- **Calculate Adjacent Mines**: The function counts the number of mines in the cells adjacent to the current cell in the input grid and includes the count in the output grid.
- **Generate Output Grid**: The function creates a new grid, where each '-' is replaced by a digit, indicating the number of mines immediately adjacent to the spot. Mines are preserved as '#' in the output grid.

## Usage:

To use this script, you need to define your 2D grid input and call the `minesweeper(grid)` function. After calling the function, it prints the output grid row by row for easier readability.

``` 
python 2D_lists_minesweeper.py
```

### Note:

This script is a part of a task series aimed at enhancing proficiency in handling 2D lists in Python. It provides a simple, practical example of how 2D lists can be processed and manipulated for a specific use case (in this case, a minesweeper game).