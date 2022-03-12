# Use python to create a script that decodes a sample cipher
# INPUT : We are going to the starbucks, time meow. Attack on titan is pretty insane. At 0530, the BN run will start. Dawn is my favorite dish soap, it's totally dope.
# Expected Output: We Attack At Dawn

#!/usr/bin/python3
import sys

def solve(file):
    with open(file, "r") as f:
        plain_text = []

        cipher_text = True

        for line in f:
           # print(line)
            for i in line.split():
               # print(i)
                if cipher_text:
                   # print("hello")
                    plain_text.append(i)
                   # print(plain_text)
                    cipher_text = False
                if "." in i:
                    cipher_text = True
        return " ".join(plain_text)        

    

def main():
    print(solve(sys.argv[1]))

main()
