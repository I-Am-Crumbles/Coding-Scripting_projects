"""
This site loves cookies and wants to know how many you would like to eat. 
Send a request (HTTP GET or POST) that includes a cookie named amount with the value of how many cookies you like to eat to get the flag.
"""

#!/bin/bash
curl –cookie “amount:3” http://shell.fullstackacademy.com:60030/
# used curl to send the specified cookie name and value to the specified URL 
