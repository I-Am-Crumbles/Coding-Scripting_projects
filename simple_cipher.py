# Use python to create a script that decodes a sample cipher
# INPUT : We are going to the starbucks, time meow. Attack on titan is pretty insane. At 0530, the BN run will start. Dawn is my favorite dish soap, it's totally dope.
# Expected Output: We Attack At Dawn

#!/usr/bin/python3
import sys

def solve(file):
    #defines the function and it's parameters
    with open(file, "r") as f:
        # opens the file to be read and sets it to a variable "f"
        plain_text = []
        #an empty list to be used later

        cipher_text = True
        # a variable to be used later that has been set to true

        for line in f:
            # for loop to itterate through the file
            for i in line.split():
                # for loop to itterate through each line item converted into a list
                if cipher_text:
                    # if statement to check the variable is still true
                    plain_text.append(i)
                    # appends the word found int he for loop to a new string
                    cipher_text = False
                    # sets the variable to false so only the one word gets appended
                if "." in i:
                    # we are looking for words that come after a period so this checks if the for loop ever finds a period
                    cipher_text = True
                    # it will set the variable back to true so we can append the world that will follow the period
        return " ".join(plain_text)
    # converts the plain_text list into a string and returns it

    

def main():
    # defining main function to call the cli input as the parameter of the above function
    print(solve(sys.argv[1]))
    #calls the solve function and passes the cli input as a parameter and prints the returned results

main()
#calls the main function that starts the script
