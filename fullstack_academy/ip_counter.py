## You are asked to take a look at an apache log file and count the occurrences of each unique ip address in the file to see where the traffic is coming from. 
#In terms of sorting, just sort them in lexicograhical order (sort the IP strings). The name of your helper function(s) and parameter(s) is/are up to you. 

#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys
import re
#importing regex module
import json
#importing json module


### HELPER FUNCTIONS (IF NECESSARY) ###
def ip_counter(testfile):
  #defining the function and it's parameters
  ip_list = []
  # empty list to store ip addresses 
  ip_dict = {}
  # empty dictionary that will be used to count each occurence of the ip address
  final_list = ""
  # empty string to store my final ouput
  pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  # variable that is regex compiled to look for four series of of 1 to 3 numbers followed by a period (essentially looking for ipv4 addresses)
  for i in testfile:
    # for loop to itterate through the parameter passed to the ip_counter function
    ip_list.append(pattern.search(i)[0])
    # appends every match of the regex pattern to a list
  for i in ip_list: ip_dict[i] = ip_dict.get(i,0) +1
    # converts the items in the ip_list to a dictionary
  for key, value in sorted(ip_dict.items()):
    # for loop that sorts the dictionary and pulls the keys and values out of it
    final_list = str(key) + ' - '+ str(value)
    # sets a variable that will display the ipv4 address and how many times it occurs in the file
    print(final_list)
    # prints the final_list variable so we can see the results
  
 
  


### MAIN FUNCTION ###
def main():
  # defining a function to open the file
  file_name = sys.argv[1]
  # setting the 2nd argument in the cli to a variable called "file_name"
  with open(file_name) as f:
    # opens the file passed in the 2nd argument as a variable "f"
   ip_counter(f)
  # calls the helper function with the open file as a parameter
  f.close   
  # closes the file since we are now done with it

### DUNDER CHECK ###
if __name__ == "__main__":
  main()
  #main function to start the script
