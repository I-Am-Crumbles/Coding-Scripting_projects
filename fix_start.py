#Write a function called fix_start with a parameter called word, which represents a string passed in from the command line. Your fix_start function should take in a string, 
#and return a string where all occurrences of its first char have been changed to *, except do not change the first char itself.

#!/usr/bin/env python3
#crunch bang tells the terminal where to find the program to run the script

### IMPORT STATEMENTS ###
import sys
#import to pull from the first line argument  later




### HELPER FUNCTIONS (IF NECESSARY) ###
def fix_start(word):
  #defining the function and it's parameters
  new_word = word.lower()
  #need to convert the string to lowercase so that uppercase letters still get checked against
  for char in new_word:
    #basic for loop to pull each character from my lower case word
    if char == new_word[0]:
      # if statement to check for the charactter ever matches the first letter of the lowercaseword
      word = word[0] + word[1:].replace(char, "*")
      #final statement to combine the new word, pull from word[0] to obtain the potential upper case letter, then concatenate that first letter with the rest of the word, replacing all instaces of the first character with *
  return(word)
#return statement


### MAIN FUNCTION ###
def main():
  #defining the main function to reference the first line of the command line 
  arg_1 = sys.argv[1]
  # setting the first argument in the command line as a variable
  print(fix_start(arg_1))
  #print statment so everything shows up on the terminal
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()
  #calling the main function so that it makes everything run
