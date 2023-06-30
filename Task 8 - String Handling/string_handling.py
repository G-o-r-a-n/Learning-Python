"""
Word Wizard

This script provides a text alteration tool that allows users to input a sentence
and choose between two types of text alteration:

1. Alternating between uppercase and lowercase characters in the sentence.
2. Alternating between uppercase and lowercase words in the sentence.

The script runs in a loop, allowing users to perform multiple alterations without
restarting the program. Users can choose to exit the program at any time.
"""

def alternate_characters(original_sentence):
    """
    Alternate between uppercase and lowercase for every character in a 
    sentence.
    
    Args:
    original_sentence (str): The input sentence to be altered.
    
    Returns:
    str: The altered sentence with alternating uppercase and lowercase 
    characters.
    """
    # Empty string to collate our altered characters back into a sentence.
    altered_sentence = ""
    # For-loop will iterate over the length of the sentence using range() and len().
    for index in range(len(original_sentence)):
        # Checks if the current index is an even number.
        if index % 2 == 0:
            # Converts character to upper case if index is an even number.
            altered_sentence += original_sentence[index].upper()
        else:
            # Converts character to lower case if index is not an even number.
            # lower() is called to ensure alternate alterations if CAPS input.
            altered_sentence += original_sentence[index].lower()
    return altered_sentence

def alternate_words(original_sentence):
    """
    Alternate between uppercase and lowercase for every word in a sentence.
    
    Args:
    original_sentence (str): The input sentence to be altered.
    
    Returns:
    str: The altered sentence with alternating uppercase and lowercase words.
    """
    # Empty list to collate our altered words.
    altered_list = []
    # split() is called to break the user's sentence into a list of words.
    original_sentence = original_sentence.split()
    # For-loop will iterate over the length of the word list using range() and 
    # len().
    for index in range(len(original_sentence)):
        # Checks if the current index is an even number.
        if index % 2 == 0:
            # Word is converted to lowercase and appended to 'altered_list'.
            altered_list.append(original_sentence[index].lower())
        else:
            # Word is converted to uppercase and appended to 'altered_list'.
            altered_list.append(original_sentence[index].upper())
    # Words in 'altered_list' are joined together as a string with a space 
    # between each word.
    altered_list = " ".join(altered_list)
    return altered_list

def welcome_menu(first_time = True):
    """
    Display the welcome menu with alteration options for the user.
    
    Args:
    first_time (bool, optional): True if it's the user's first run, False 
    otherwise. Default is True.
    """
    # This if-statement block only displays welcome message the first time 
    # the script is run
    if first_time:
        print("\n\n***** Welcome to Word Wizard *****\n\n")
    
        print("This program can alter your sentence in the following ways: ")

    print(
        "\n\n1 - Alternate between uppercase and lowercase for every "
        "character in a sentence.\n\n"
        )
    
    print(
        "2 - Alternate between uppercase and lowercase for every word in a "
        "sentence.\n\n"
        )

def run_program_again(first_time, re_run):
    """
    Prompt the user if they want to run the program again.
    
    Args:
    first_time (bool): True if it's the user's first run, False otherwise.
    re_run (bool): True if the user wants to run the program again, 
    False otherwise.
    
    Returns:
    tuple: A tuple containing updated values of 'first_time' and 're_run'.
    """
    while not first_time and re_run:
        run_program_again = input(
            "Would you like to alter another sentence? Y / N: ").lower()
        
        if run_program_again == "y":
            first_time = False
            re_run = True
            return first_time, re_run
                
        elif run_program_again == "n":
            print("\n\n***** Thank you for using Word Wizard *****\n\n")
            first_time = False
            re_run = False
            return first_time, re_run
                
        else:
            print(
                "\n\nCommand not recognised. Enter only Y or N.\n\n"
                )
            continue


first_time = True
re_run = True

while first_time or re_run:
    
    welcome_menu(first_time)
    
    while True:
        alteration_type = input(
            "Please enter the alteration you would like to perform by "
            "entering 1 or 2: "
            )
        
        if alteration_type == "1":
        
            original_sentence = input(
                "\n\nPlease enter a sentence you would like to alter: "
                )
        
            altered_sentence = alternate_characters(original_sentence)
            print(f"\n\n{altered_sentence}\n\n")
        
            first_time = False
        
            first_time, re_run = run_program_again(first_time, re_run)
            
            break
    
        elif alteration_type == "2":
        
            original_sentence = input(
                "\n\nPlease enter a sentence you would like to alter: "
                )
        
            altered_sentence = alternate_words(original_sentence)
        
            print(f"\n\n{altered_sentence}\n\n")
        
            first_time = False
        
            first_time, re_run = run_program_again(first_time, re_run)
            
            break
        
        else:
            print("\n\nCommand not recognised. Enter only the number 1 or 2.\n\n")
            first_time = False
            continue