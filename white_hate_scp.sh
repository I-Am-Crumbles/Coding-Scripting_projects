"""
Download a special version of the white-hat-manifesto.txt from the shell server in /problems/secp-a--services_0_fc0be14ed4e13814029817801ff91f81. 
You must download this new copy (an older copy will not work). Then, serve this file up via HTTP at http://127.0.0.1/ethics/white-hat-manifesto.txt. 
Once complete, run services to get the flag.
"""

#!/bin/bash
scp -rp username@52.1.103.48:/problems/secp-a--services ~Desktop/ehtics
# this line secure copied the file from the shell server onto my virtual machine into a directory called "ethics" as required by the challenge, the file was hidden so I used the recursive option to find it
python3 -m http.server 80 -bind 127.0.0.1
# from the ethics directory I ran this python module to serve up all the files from that directory on a simple web server at the required IP address and port
# I then ran the binary that searches for the file at the desired URL and produces a flag when it finds it.

