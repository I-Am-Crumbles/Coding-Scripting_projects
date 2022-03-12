#!/usr/bin/env python3
#You've been ordered to print name tags for your friend's birthday party! You noticed that quite a few people seem to share the same name at this party so you're putting 
#together an organized list for your order. Given a list of names, write a helper function called birthday_party that returns the number of occurrences of each name
### IMPORT STATEMENTS ###
import sys

### HELPER FUNCTIONS (IF NECESSARY) ###
def birthday_party(names):
  #defining the name of the helper function and setting it's parameters
    name_list = []
    # empty list variable for later use
  name_dict = {}
  # empty dictionary variable for later use
  final_list = ""
  # empty string variable for later use
  for i in names:
    # for loop to iterate through the paramter the function is calling
    x = i.strip()
    # setting variable "x" to each iteration of the for loop but stripping any new line charaters in the string
    name_list.append(x)
    # appends the name (i) stripped of it's new line character to list variable set above
  for i in name_list: name_dict[i] = name_dict.get(i,0) +1
    # for loop to go through name_list and assign each name to the empty dictionary
  for key, value in name_dict.items():
    # for loop to separate the key and value of the dictionary created above
    final_list = str(key) + ' - '+ str(value)
    # formatting a final string that displays the each name on the list and how many times it appears
    print(final_list)
    # prints the final string

    
  
  
### MAIN FUNCTION ###
def main():
  #main functions to call the script
  file_name = sys.argv[1]
  # variable being set to whatever is the argument after the script in the shell command line
  open_file = open(file_name)
  # opens the file listed in the shell command line and saves it as a new variable
  return(birthday_party(open_file))
  # returns the main statement to run the birthday_party helper function with the open file as it's parameter


  
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()
  # calls the main function so that the whole script can run
