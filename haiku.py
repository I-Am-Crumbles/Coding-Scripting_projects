#Someone dropped our cyber haiku dictionary and the order in which they were stored is all messed up. 
#Can you fix the order dictionary and print them out in the right order? The name of your helper function(s) and parameter(s) is/are up to you.

#!/usr/bin/env python3

#!/usr/bin/env python3
### IMPORT STATEMENTS ###
import sys
import ast
### HELPER FUNCTIONS (IF NECESSARY) ###
def haiku_fixer(poem):
  haiku_dict = ast.literal_eval(poem.read())
  x_dict = {}
  list_string = []
  result = ""
  for key in haiku_dict:
    x_dict[int(key)] = haiku_dict[key]
  haiku_length = len(haiku_dict)
  for num in range(1, haiku_length):
    result += haiku_dict[str(num)]
    if haiku_dict[str(num)] != "\n" and num != haiku_length -1:
      result += " "
    elif haiku_dict[str(num)]== "\n":
      result = result.rstrip() + "\n"
   
  
### MAIN FUNCTION ###
def main():
  file_name = sys.argv[1]
  with open(file_name) as f:
    haiku_fixer(f)
  f.close
### DUNDER CHECK ###
if __name__ == "__main__":
  main()
