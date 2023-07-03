# Task 07 - Towards Defensive Programming

This application is a robust calculator that performs basic arithmetic operations on two numbers entered by the user. It includes options to write equations to a text file and read from an existing file. The program employs defensive programming to handle unexpected events and user inputs.

## Objective: Calculator with Input/Output File Operation

The program performs the following:

1. Gives the user the option to perform basic arithmetic operations on two numbers, or to read equations from a file.
1. If the user chooses to perform operations:
    - The user is prompted to enter two numbers and an arithmetic operator.
    - The result of the operation is displayed and written to a text file specified by the user.
    - The user can choose to perform another operation, which will be appended to the same file, or finish and print the saved equations from the file.
1. If the user chooses to read from a file:
    - The user is prompted to input the file name.
    - If the file exists, the equations in the file are displayed.
    - If the file does not exist, the user is prompted again to enter the file name.

The Python script that accomplishes this can be found in the file: [towards_defensive_programming.py](https://github.com/G-o-r-a-n/Learning-Python/blob/main/Task%2007%20-%20Towards%20Defensive%20Programming/towards_defensive_programming.py).