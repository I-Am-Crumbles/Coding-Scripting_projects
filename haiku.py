#Someone dropped our cyber haiku dictionary and the order in which they were stored is all messed up. 
#Can you fix the order dictionary and print them out in the right order? The name of your helper function(s) and parameter(s) is/are up to you.

#!/usr/bin/env python3

#!/usr/bin/env python3
### IMPORT STATEMENTS ###
import sys
import ast
#imports Abstract Syntax Tree - 

### HELPER FUNCTIONS (IF NECESSARY) ###
def haiku_fixer(poem):
  # defining the functions and it's parameters 
  haiku_dict = ast.literal_eval(poem.read())
  # The file fed to the program in this challenge is sort of formated like a dictionary. Here I am using abstract syntax tree to open and read the file, then take it's best guess
  # as to what the file contains and saving that as a variable (in this case it formatted the file and saved it as dictionary under the variable haiku_dict
  x_dict = {}
  # empty dictionary for later use
  list_string = []
  # empty list for later use
  result = ""
  # empty string to store results later
  for key in haiku_dict:
    #iterates through my dictionary i created on line 15 and pulls out the keys
    x_dict[int(key)] = haiku_dict[key]
    # adds the key to my empty dictionary as an integger
  haiku_length = len(haiku_dict)
  # saves the length of the dictionary created in line 15 as a variable
  for num in range(1, haiku_length):
    # iterates through a range of numbers 1 and the length of the dictionary 
    result += haiku_dict[str(num)]
    # adds each word found in the haiku dictionary to a string called result
    
    if haiku_dict[str(num)] != "\n" and num != haiku_length -1:
      result += " "
      # converts new line characters found while iterating through the haiku dictionary to spaces ( there were random ones mixed in from converting the file that needed to be cleaned up)
    elif haiku_dict[str(num)]== "\n":
      result = result.rstrip() + "\n"
      # strips any new line characters found at the end of each line
   
  
### MAIN FUNCTION ###
def main():
  file_name = sys.argv[1]
  # saves the argument passed after the function is called in the command line to a variable called file_name
  with open(file_name) as f:
    # opens the file and saves it as a variable called f
    haiku_fixer(f)
    # calls the helper function with the open file as a parameter
  f.close
  # closes the file since we are done with it
### DUNDER CHECK ###
if __name__ == "__main__":
  main()
  # main statement being called to make the whole script run
