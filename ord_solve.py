#While taking a college programming class, your instructor just taught you about ordinal values. 
#You need to take the sample file and add up the total sum of ordinal values of characters upper and lowercase, but not anything else.


#!/usr/bin/python3
import sys

def solve(file):
    bad_characters = [" ", ".", "!", "?", "'",",","-", "\n", "/"]
    new_file = open(file, "r")
    new_file = new_file.read()
    new_file2 = new_file.strip()
    for char in new_file2:
        if char in bad_characters:
            new_file2 = new_file2.replace(char, "")
    print(sum(ord(i) for i in new_file2))

def main():
    solve(sys.argv[1])

main()
