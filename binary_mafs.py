# Create a python script that reads a file with several binary numbers on each line and adds them up and returns a correct sum in base10

#!/usr/bin/python3
import sys
import binascii

def solve(file):
    with open(file, "r") as f:
        for line in f:
            number_list = []
            new_line = line.strip().split()
            for char in new_line:
                char = int(char, 2)
                char.to_bytes((char.bit_length() + 7) // 8, 'big').decode()
                number_list.append(char)
            print(sum(number_list))   
                
    

def main():
    solve(sys.argv[1])


main()
