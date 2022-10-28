"""
It is time for you to set the table - the iptable of course. To complete this challenge, 
you need to set it so that your local machine does not respond to ping requests and blocks all outbound TCP requests except SSH. 
Once complete, run set-the-table to verify these steps and receive the flag.
"""

#!/bin/bash

sudo iptables -A OUTPUT -p tcp -m tcp --dport 22 -j ACCEPT
#allows ssh traffic

sudo iptables -A INPUT --proto icmp -j DROP
#disables pinging

sudo iptables -A OUTPUT -p tcp -j REJECT
#disables tcp traffic
