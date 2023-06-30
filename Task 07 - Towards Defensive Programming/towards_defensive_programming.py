"""
Simple Calculator

This script gives the user two options.

1). It can take two numbers from a user and perform basic arithmetic, multiple
times if necessary, writing each equation to a new user-created file.

2). Open and read an existing file of equations.

"""

################################## Functions #################################

def calculate(num_1, num_2, operator):
    """
    Calculate the result of the arithmetic operation between two numbers.
    
    Args:
    num_1 (float or int): The first number in the operation.
    num_2 (float or int): The second number in the operation.
    operator (str): The arithmetic operation symbol (+, -, *, /).
    
    Returns:
    float or int: The result of the arithmetic operation.
    """    
    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "*":
        return num_1 * num_2
    elif operator == "/":
        return num_1 / num_2
    
def float_conversion(numerical_value):
    """
    Convert the input number to an integer if it has no decimal part, 
    otherwise return it as a float.
    
    Args:
    value (str): A numerical value in string format from user input.
    
    Returns:
    float or int: The converted numerical value.
    """
    numerical_value = float(numerical_value)
    if numerical_value.is_integer():
        return int(numerical_value)
    else:
        return numerical_value

############################# Simple Calculator ##############################

# Different calulcation types are compiled into a dictionary
operators_dict = {
    "Addition" : "+" ,
    "Subtraction" : "-" ,
    "Multiplication" : "*" ,
    "Division" : "/"
}

# Welcome message and instructions for user
print(
    "\n\nWelcome to the GitHub Calculator.\n\n"
    "Option 1 - Enter equations and write each equation to a new .txt file.\n\n"
    "Option 2 - Open an existing .txt file of equations and read your "
    "previously saved equations.\n\n"
    )
# User chooses whther to open and read an existing file or write equations to 
# a new file.
while True:
    option = input("Please enter 1 or 2 to proceed with the appropriate option: ")

    if option == "1":
        filename = input(
            "\n\nPlease enter the name you would like to assign to your new file: "
            )
        print(
            "\n\n"
            "This calculator can use the following 4 basic arithmetic operators:"
            "\n\n"
            )
        
        # Iterates through the dictionary and displays the options to the user
        for operation, symbol in operators_dict.items():
            print(f"{operation}: {symbol}\n")
        # Control booleans for subsequent while-loop set.
        first_run = True
        restart_calculator = False
        break
    
    elif option == "2":
        # Control booleans for subsequent while-loop set.
        first_run = False
        restart_calculator = False
        open_new_file = True
        break
    # Loop continues until users enters a valid command.
    else:
        print("\n\nCommand not recognised.\n\n")

# Using the OR operator to ensure this code block runs if its the user's first time or 
# if they are making further calculations.
while first_run or restart_calculator:
    while True:
        # Prompts the user to enter a symbol that matches the desired operator.
        operator = input(
            "\nPlease enter the symbol that matches your desired calculation: "
            )        
        # Checks the dictionary values to ensure a valid operator has been entered.
        if operator not in operators_dict.values():
            print("\n\nCommand not recognised.\n")
        # Breaks out of loop upon valid operator entry.
        else:
            break
    
    while True:
        try:
            # Prompts user for the first number they want to pass through the 
            # calculator.
            num_1 = input("\n\nPlease enter the first numerical value: ")
            num_1 = float_conversion(num_1)
            break
        # Raises exception if user enters a non-numerical value. 
        # Loop continues until a valid numerical value is entered.
        except ValueError:
            print("\n\nYou have not entered a numerical value.")

    while True:
        try:
            # Prompts user for the second number they want to pass through the 
            # calculator.
            num_2 = input("\n\nPlease enter the second numerical value: ")
            num_2 = float_conversion(num_2)
            # Pre-empts a potential zero division error 
            # User will be prompted again to enter a valid number for division.
            if operator == "/" and num_2 == 0:
                print("\n\nYou can't divide by zero.")
                continue
            break
        # Raises exception if user enters a non-numerical value. 
        # Loop continues until a valid numerical value is entered.
        except ValueError:
            print("\n\nYou have not entered a numerical value.")

    # Passes values into calculate() function and returns the result.
    result = calculate(num_1, num_2, operator)
    # Passes {result} into float_conversion function and returns correct formatting.
    result = float_conversion(result)
    #{equation} stores the users input in the optimal format for our file-reading 
    # section.
    equation = f"\n{num_1} {operator} {num_2} = {result}\n"
    # Displays the equation and result within the terminal
    print(equation)
    
    # Creates and opens a file in append mode to write the equations to the file.
    with open(f"{filename}.txt", "a") as equations_file:
        equations_file.write(equation)
    
    while True:
        # User is prompted to run another calculation if they wish.
        restart_calculator = input(
            "Would you like to run another calculation? (Y / N): "
            )
        # If yes, boolean values are updated to ensure the loop runs again.
        if restart_calculator.lower() == "y":
            first_run = False
            restart_calculator = True
            break
        # If no, boolean values are updated to ensure the loop does not run again.
        elif restart_calculator.lower() == "n":
            first_run = False
            restart_calculator = False
            open_new_file = True
            print(f"\n\nYour equations have been saved as {filename}.txt.\n\n")
            break
        # Loop continues until users enters a valid command.
        else:
            print("\n\nCommand not recognised.\n\n")

while open_new_file:
    # If user chose option 2, the calculation code block above is skipped.
    # User is immediately prompted to open an existing file instead.
    if option == "2":
        while True:
            # Prompts user to enter the filename.
            new_filename = input(
                "\n\nPlease enter the .txt filename you are trying to open: "
                )
            try:
                # Opens file in read mode.
                with open (f"{new_filename}.txt", "r") as new_equations_file:
                    # Iterates through each line in file.
                    for line in new_equations_file:
                        print(line)
                        open_new_file = False
                break
            except FileNotFoundError:
                print("\n\nFile does not exist.")
    # Runs if the user chose option 1, and this prompt appears after 
    # calculations have been made.
    else:
        open_file = input(
            "Would you like to open and read from an existing file "
            "(Y/N): "
            )
        # Checks user's choice whether to open a new file.
        if open_file.lower() == "y":
            # Prompts user to enter the filename.
            new_filename = input(
                "\n\nPlease enter the .txt filename you are trying to open: "
                )
            # Attempts to open the file the user will specifiy.
            try:
                # Opens file in read mode.
                with open (f"{new_filename}.txt", "r") as new_equations_file:
                    for line in new_equations_file:
                        print(line)
                        open_new_file = False
            except FileNotFoundError:
                print("\n\nFile does not exist.\n\n")
        # If no, loop is broken.
        elif open_file.lower() == "n":
            open_new_file = False
        
        else:
            print("\n\nCommand not recognised.\n\n")

# End message.
print("\n\n***** Thank you for using the GitHub Calculator. *****\n\n")