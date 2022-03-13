# Santa has asked if you can help him parse his list naughty or nice list of people for his upcoming christmas delivery. 
#It looks as though the elves that were writing down the names of those naughty or nice didn't keep the same format. C
#an you give santa a total count of how many nice and how many naughty people are on his list? Name your helper function naughty_or_nice and your parameter santa_list. 

#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys


### HELPER FUNCTIONS (IF NECESSARY) ###
def naughty_or_nice(santa_list):
  # defines a function called and it's parameters
  goodlist = []
  # empty list variable for use later
  for x in santa_list:
    # itterates through the parameter passed to the function
    goodlist.append(x.split()[-1])
    # appends each name in the file to a new list
    good_count = {}
    # creates an empty dictionary
    for i in goodlist: good_count[i] = good_count.get(i,0)+1
      # itterates through goodlist and counts each occourence of good and bad
  return "Naughty list has " + str(good_count["bad"]) + " people!" + "\n" "Nice list has " + str(good_count["good"]) + " people!"
  # return statement that returns a string of how many naughty and how many nice people were listed in the file
  
    

### MAIN FUNCTION ###
def main():
  
  file_name = sys.argv[1]
  open_file = open(file_name)
  print(naughty_or_nice(open_file))
  

### DUNDER CHECK ###
if __name__ == "__main__":
  main()
