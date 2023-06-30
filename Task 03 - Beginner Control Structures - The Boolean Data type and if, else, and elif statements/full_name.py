# Ask user to input their name
name = input("Please enter your full name: ")
print()

# Check length of name using 'len' and display corresponding message
# depending on which condition is met.
if len(name) == 0:
    print("You haven't entered anything. Please enter your full name.\n\n")
    
elif len(name) <= 4:
    print(
        "You have entered less than 4 characters.\n\n"
        "Please make sure that you have entered your first name and surname.\n\n"
        )
    
elif len(name) > 35:
    print(
        "You have entered more than 35 characters.\n\n"
        "Please make sure that you have only entered your full name.\n\n"
        )
    
else:
    print(f"Thank you for entering your name: {name}")