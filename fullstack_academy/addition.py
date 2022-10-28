# Write a function called simple_addition with a parameter called file, which represents an open file containing a list of numbers (both ints and floats), two on each line, 
# separated by exactly one space each. Your simple_addition function should add the two numbers together and print their sum (as a float).

#!/usr/bin/env python3
# crunch bang to tell the terminal where to find the program to run the script

### IMPORT STATEMENTS ###
import sys
#used later to reference the line argument our function will be calling as a parameter




### HELPER FUNCTIONS (IF NECESSARY) ###
def simple_addition(file):
  #define statement naming the function and it's parameter
  for line in file:
    #for loop that does the initial read through the file
    numbers = line.rstrip().split()
    #pulls the text from the file, strips new line characters and splits them into a list and asigns that list to a variable
    numbers = float(numbers[0]), float(numbers[1])
    #pulls the text from the list and converts it into floats then asigns them to a variable
    
    print(numbers[0] + numbers[1])
    #print statement that displays our result of the two numbers in the file added together




### MAIN FUNCTION ###
def main():
  #statement defining the main function which will call the helper fucntion when it runs
  file_name = sys.argv[1]
  # setting the first command line arguement as a variable
  open_file = open(file_name)
  #opening the file that will be the first command line argument
  simple_addition(open_file)
  #calling the function with the open file as a perameter
  open_file.close()
  #closes the file
  
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()
  #calls the main function to start the script
