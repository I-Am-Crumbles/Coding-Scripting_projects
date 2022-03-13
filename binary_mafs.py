# Create a python script that reads a file with several binary numbers on each line and adds them up and returns a correct sum in base10

#!/usr/bin/python3
import sys
import binascii
#imported library for ascii code representations

def solve(file):
    #defining the function and it's parameters
    with open(file, "r") as f:
        #opens the file passed through the command line as a variable labeled "f"
        for line in f:
            #iterates through the now open file
            number_list = []
            #empty list variable for later use
            new_line = line.strip().split()
            #creates a new variable that strips the new line characters from the file and asigns it's content to a list
            for char in new_line:
                #iterates through the newly created list
                char = int(char, 2)
                # converts each item in the list from a string to an integer in base 2
                char.to_bytes((char.bit_length() + 7) // 8, 'big').decode()
                # this converts each binary number into it's ascii encoded version
                number_list.append(char)
                # appends the newley ascii encoded character (in this case an integer in base 10) to my empty list variable
            print(sum(number_list))
            #prints the sum of all of the list items 
                
    

def main():
    solve(sys.argv[1])
    # calls the arguement passed after the script in the command line to the function (should be a file containing a lines of binary numbers)


main()
# calls the main functions which runs the rest of the script
