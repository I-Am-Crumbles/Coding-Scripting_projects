#While taking a college programming class, your instructor just taught you about ordinal values. 
#You need to take the sample file and add up the total sum of ordinal values of characters upper and lowercase, but not anything else.


#!/usr/bin/python3
import sys

def solve(file):
    # defining the function and it's parameter
    bad_characters = [" ", ".", "!", "?", "'",",","-", "\n", "/"]
    # list of characters that I don't want counted to be referenced later
    new_file = open(file, "r")
    # opens the file passed in the cli to be read and saves it as a varialbe "new_file"
    new_file = new_file.read()
    # converts the open file into a string and updates the variable to be set to that string
    new_file2 = new_file.strip()
    # creates a new varialbe that has the new line characters stripped out of the original string
    for char in new_file2:
        # for loop to itterate through the string that has no new line characters
        if char in bad_characters:
            # checks any character it finds against the list of ones I do not want to count
            new_file2 = new_file2.replace(char, "")
            # if it finds a character in the bad_character list this will delete it and update the variable
    print(sum(ord(i) for i in new_file2))
    # print statement that will display the sum of the ordinal value of each character found in a for loop that itterates through the new_file2 string

def main():
    # main function to set the parameter being passed to the solve function as a file passed in from the command line
    solve(sys.argv[1])
    #sets the parameter of the solve function to the file passed from the command line

main()
# calls the main function to start the above script
