#!/usr/bin/python3

#import modules
import socket
import sys

#assigns the target host ip address and port to variables passed as a parameter by the command line
target_host = sys.argv[1]
target_port = sys.argv[2]

# creating a ipv4 socket ojbect using AF_INET and setting it to tcp type using SOCK.STREAM
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting to the cliet
client.connect((target_host,int(target_port)))

#send byte encoded GET request to the target
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive data from target host with max buffer of 4096 bytes
response = client.recv(4096)

#Decodes the received data from bytes to a string, prints it, then closes the socket connection.
print(response.decode())
client.close()
