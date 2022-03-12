#Create a script that checks the last 3 digits of a flag hash against a hexidecimal list.

#!/usr/bin/env python3

import hashlib

flag_hash = "a497453fe1eee3e0c4d44f2a74a1518744d247a1c6dd6c902a2b3367987f0e5d21fb1cbdd1af55ea78098be5a336ffaf06f19b8e5a5997e06d20ce00f9907424"
#The challenge provide the flag hashed with sha512

hex_decimal_list = []
# Variable set aside to be a list of hexidecimal digits to guess against later
x =""
# random variable to store an empty string for later user
for num in range(4096):
  #for loop to find each number in the range (4096 possible combinations for the last 3 digits of a hexadecimal number)
 hex_decimal_list.append(hex(num))
#converts each number in the for loop into a hex and the append that to a list
#print(hex_decimal_list) -- was just to check if my hex list was working correctly
  
for i in hex_decimal_list:
  #for loop iterating through list I just created above
  x = i[2:].zfill(3)
  # setting a string that uses 
  #print(x)


  #padded_num = {x:03}

  flag = "FS{hash-I_had_corned_beef_and_hash_" + x +"}"
  flag_upper = "FS{hash-I_had_corned_beef_and_hash_" + str(x.upper()) +"}"
  #print(flag_upper)

  guess_upper = hashlib.sha512(flag_upper.encode()).hexdigest()
  guess_lower = hashlib.sha512(flag.encode()).hexdigest()
  #print(guess)

  if guess_lower == flag_hash:
    print(flag)
  elif guess_upper == flag_hash:
    print(flag_upper)
