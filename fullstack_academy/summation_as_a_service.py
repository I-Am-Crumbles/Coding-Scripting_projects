#Write a program, which takes two distinct integers separated by space as input and prints the sum of all the integers between them, including the two given numbers. 
#Note that the numbers can appear in either order.

#!/usr/bin/python3
import sys

def solve(file):
    # defines the function and it's parameters
    with open(file, "r") as f:
        # opens the file passed in the cli to be read as a variable called "f"
        for line in f:
            # for loop to itterate through the open file
            result = 0
            # sets a variable called result to 0 to be used later
            numbers = line.rstrip().split()
            # strips any new line characters from each object found in the for loop and convers them into a list
            numbers = (int(numbers[0]), int(numbers[1]))
            # converts the strings in the numbers_list into integers
            x = sorted(numbers)
            # sorts the numbers in the list and saves them as a new variable


            for num  in range(x[0], x[1]):
                # for loop that goes through a range of the 2 numbers
                result += num
                # adds each number it finds in the above for loop 
            result += x[1]
            # range is non inclusive so we have to add the final number in a the end
            print(result)
            # prints the result which would be the sum of the range of the two numbers in each line of the file
        
    
def main():
    # main function to set the file being called in the cli as the parameter of the above function
    solve(sys.argv[1])
    # sets the paramter of the solve function as the file input in the cli

main()
# calls the main function that will start the entire script
