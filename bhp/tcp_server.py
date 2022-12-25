#!/usr/bin/python3

# import modules
import socket
import threading
import sys

#Defines the ip address and port number as variables that are passed as parameters from the command line.
ip_addr = sys.argv[1]
port = int(sys.argv[2])

#Function that creates a new socket object using IPv4 (AF_INET) and socket type tcp (SOCK_STREAM)
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Binds the socket to specified IP address and port number.
    server.bind((ip_addr, port))
    # Puts socket into listen mode allowing it to accept incoming requests and sets a maximum of 5 queued connections.
    server.listen(5)
    #prints a message to indicate that the server is listening 
    print(f'[*] Listening on {ip_addr} : {port}')
    
    #While loop that waits for client to connect to the server. When connections is accepted it returns a new socket object and the client's address
    while True:
        client, address = server.accept()
        #Print message to indicate the connection was accepted
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        # Create a new thread and start it, with the "client" socket object passed as an argument to the hand_client function below
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
        
# Function that receives data from the client socket with a max buffer size of 1024bytes
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        #Prints data that has been converted from bytes to a string.
        print(f'[*] Received: {request.decode("utf-8")}')
        # Sends the "ACK" message to the client socket in bytes format
        sock.send(b'ACK')
      
#Dunder check that specifies that the main fucntion should be called when the script is run.
if __name__ == '__main__':
    main()
