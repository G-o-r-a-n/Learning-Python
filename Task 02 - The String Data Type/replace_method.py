# Define 'sentence' variable
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

# Alter the variable 'sentence' using 'replace()' function to remove the
# unwanted characters and display to user.
print(sentence.replace('!', ' '))
print()

# Alter the variable 'sentence' using '.replace()' and '.upper()' methods
# in conjunction to remove the unwanted characters, capitalise the string and
# display to user.
print(sentence.replace('!', ' ').upper())
print()

# Alter the variable 'sentence' using '.replace()' and '[start:end:steps]'
# method in conjunction to remove the unwanted characters, reverse the string
# and display to user.
print(sentence.replace('!', ' ')[::-1])