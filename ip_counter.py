## You are asked to take a look at an apache log file and count the occurrences of each unique ip address in the file to see where the traffic is coming from. 
#In terms of sorting, just sort them in lexicograhical order (sort the IP strings). The name of your helper function(s) and parameter(s) is/are up to you. 

#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys
import re
import json


### HELPER FUNCTIONS (IF NECESSARY) ###
def ip_counter(testfile):
  #key_values = {}
  ip_list = []
  ip_dict = {}
  final_list = ""
  pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  for i in testfile:
    ip_list.append(pattern.search(i)[0])
  for i in ip_list: ip_dict[i] = ip_dict.get(i,0) +1
  for key, value in sorted(ip_dict.items()):
    final_list = str(key) + ' - '+ str(value)
    print(final_list)
  
  #[print(key,'-',value) for key, value in ip_dict.items()]
  


### MAIN FUNCTION ###
def main():
  file_name = sys.argv[1]
  with open(file_name) as f:
   ip_counter(f)
  f.close   
  

### DUNDER CHECK ###
if __name__ == "__main__":
  main()
