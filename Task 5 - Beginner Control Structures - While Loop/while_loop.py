# Display welcome statement along with instructions.
print("---------- Mean Average Calculator ----------")
print(
    "\n"
    "This program will calculate the average of a series of numbers you enter."
    "\n\n"
    "Enter '-1' when you are ready to calculate the average."
    "\n\n"
    "----------------------------------------"
    "\n\n"
    )

# Create a list to store the user's numbers..
list_of_numbers = []

# The while-loop prompts the user to continually enter numbers until they enter -1.
while True:
    # The try-except block will verify whether the user has enter a valid value.
    try:
        # User's entries have been typecast as floats. 
        user_number = float(input("Please enter a number: "))
        print()
        # Checks if user has entered -1 to break the loop
        if user_number == -1:
            break
        # Adds user's entry to list_of_numbers.
        list_of_numbers.append(user_number)
    # ValueError handles any non-numerical value or empty entries.
    except ValueError:
        print("\nInvalid entry.\n")

# Present the data gathered and calculated mean average to the user.
print("----------------------------------------")
print(f"Numbers entered: {list_of_numbers}\n")

print(f"Number of entries: {len(list_of_numbers)}\n")

print(f"Total sum: {sum(list_of_numbers)}\n")

print(f"Average: {(sum(list_of_numbers) / len(list_of_numbers)):.2f}")
print("----------------------------------------")