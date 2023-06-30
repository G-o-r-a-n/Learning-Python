# This script will print a series of asterisks, increasing line by line.

# The for-loop iterates over a range of numbers, starting from 1 and going up
# to (but not including) 6.
for count in range(1, 6):
    # The string "*" is multiplied by the count, and will print out an
    # increasing number of "*" per iterastion.
    print("*" * count)