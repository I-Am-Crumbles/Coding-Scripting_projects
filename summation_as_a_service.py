#Write a program, which takes two distinct integers separated by space as input and prints the sum of all the integers between them, including the two given numbers. 
#Note that the numbers can appear in either order.

#!/usr/bin/python3
import sys

def solve(file):
    with open(file, "r") as f:
        for line in f:
           # print(line)
           # print((type(line)))
            result = 0
            numbers = line.rstrip().split()
            numbers = (int(numbers[0]), int(numbers[1]))
            x = sorted(numbers)


            for num  in range(x[0], x[1]):
                result += num
            result += x[1]
            print(result)
        
    
def main():
    solve(sys.argv[1])

main()
