#!/usr/bin/python3
# Crunch bang that tells the system where to find python, may need to be edited for personal use.
import socket
# imports the socket library which allows python to send data to webservers when the socket is connected

def running(site):
  # Defining the function "running" that takes the website you want to check as a parameter)
    try:
      #Try tells python to test a block of code for errors
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # creates a variable "sock" that is set to an INET streaming socket (IP based socket/linux internet socket)
        sock.connect((site, 80))
        # attempts to connect the INET streaming socket to the website paramater on port 80)
        return True
        # if the socket was able to connect the function will return true
    except:
    #If anything in the try block of code fails except will catch and handle it
        return False
        # if the try block of code does fail except will now tell the function to return False

if __name__ == "__main__":
  #Dunder check to prevent the next part of the script from running when it shouldn't
    while True:
      #checks if the dunder check passed and if it did proceeds to the next part of the script
        site = input('Website to check: ')
        # sets the site variable the "running" functions uses as a paramater to input from the user. Also includes a printed message to tell the user what to input
        if running(f'{site}'):
        # checks if the running function returned True and if it did it will proceed to the print statement
            print(f"{site} is running!")
            #converts the "site" variable to a string and prints a statement telling the user that the website they entered was running
        else:
        #if the "running" function returned false due to user error or the website being down then it will generate the below print statement telling the user there was a problem
            print(f'There is a problem with {site}!')
            # converts the "site" variable to a string and prints it in a message telling the user there was a problem with the website they entered
        if input("Would you like to check another website(Y/N)? ") in {'n', 'N'}:
        # checks if there was user input on the script, if there was it will ask the user if they want to check another website, if the enter Y the script will allow them to input another website
            break
            #if the user entered "N" in the above check the script will end itself. 
