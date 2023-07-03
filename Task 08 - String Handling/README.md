# Task 08 - String Handling

This script, referred to as "Word Wizard", is a user-friendly text manipulation tool that offers two unique functionalities: alternating the casing of characters and words in a user-provided sentence. The program runs in an interactive loop, allowing users to perform several alterations without needing to restart the script. It ensures a seamless and continuous interaction with the user.

## Objective:

The goal of this task is to:

1. Create a program that reads in a string and makes each alternate character an UPPERCASE character and each other alternate character a lowercase character (e.g, the string “Hello World” would become “HeLlO WoRlD”).
1. Starting with the same string but making each alternative word lower and upper case (e.g. the string: “I am learning to code” would become “i AM learning TO code”). This program leverages Python's split and join functions.

## Code Explained:

The script contains the following functions:

- alternate_characters(original_sentence): This function accepts a string and alternates the case of every character in it, returning the modified string.
- alternate_words(original_sentence): This function accepts a string, alternates the case of every word in it, and returns the modified string.
- welcome_menu(first_time = True): This function displays the welcome menu with alteration options for the user. The first_time parameter checks whether it's the user's first time running the script.
- run_program_again(first_time, re_run): This function checks whether the user wants to run the program again, returning a tuple with updated values of 'first_time' and 're_run'.

Upon execution, the program prompts the user to choose an alteration type and input the sentence to be altered. Based on the user's choice, it applies the corresponding function (alternate_characters() or alternate_words()) to create the altered sentence.

Finally, the program queries the user on whether they want to continue altering sentences, thereby giving them an option to exit or continue running the script.

The Python script that accomplishes this can be found in the file: [string_handling.py](https://github.com/G-o-r-a-n/Learning-Python/blob/main/Task%2008%20-%20String%20Handling/string_handling.py).

## Usage:

To utilize this script, execute the Python file in your terminal. Follow the on-screen prompts to choose your preferred alterations and input your sentences. You can choose to continue altering sentences or exit the program as per the provided prompts.

```
python string_handling.py
```

### Note:

This script is part of a task series intended to enhance Python skills, specifically string handling and manipulation. It illustrates the use of Python's in-built functions to perform complex string manipulations and the concept of continuous interaction with users in a command-line application.