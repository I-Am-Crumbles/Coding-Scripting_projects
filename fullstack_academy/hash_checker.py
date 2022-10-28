#!/usr/bin/env python3
# crunch bang to tell the script 
from hashlib import md5
#This script was created to solve a CTF challenge while learning python3 and hashing. The goal was to brute force decode the last 3 digits of a flag that was hashed using md5. Since there are only 1000 possible options it was relatively simple.
flag_hash = "0a3a4cce269fee850e2ae01a1ca461f8"


for num in range(1000):
# The goal was to brute force test all possible options for the last 3 digits of the flag being somewhere between 000 and 999 since range is non inclusive I went with 1000 

    
    padded_num = f'{num:03}'
    # the numerice string in the flag consists of 3 numbers so I padded it with 0 
    
    flag = "FS{cabbage-wait_that's_not_right_" + padded_num + "}"
    # format the flag string with each padded num
    
    guess = md5(flag.encode())
    #calculate the hash of the flag string

   
    if guess.hexdigest() == flag_hash:
        print(flag)
         # test to see if the hashes match
