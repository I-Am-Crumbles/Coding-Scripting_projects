"""
The site http://shell.fullstackacademy.com:60031 only accepts HTTP GET requests. 
Send it a request that includes all three of the below paramater:value pairs to get the flag.

usertype:admin
school:fullstack cyber bootcamp
access-level:super duper top secret
"""

#!/bin/bash
curl -X GET "http://shell.fullstackacademy.com:60031/?usertype=admin&school=fullstack+cyber+bootcamp&access-level=super+duper+top+secret"
# used curl to send a URL encoded request with the desired data, the tricky part is the URL syntax and remembering to put it in quotes.
