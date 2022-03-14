"""
Connect to shell.fullstackacademy.com:60033 and filter out the 'rubbish' transmissions to get the flag. The flag is sent exactly in order.
"""

#!/bin/bash
echo "Y" | nc shell.fullstackacademy.com 60033| grep -v "rubbish" | grep -v " " | tr -d "\n\r"
# when netcat connects to the shell you are prompted to enter yes or no, so I started my command with "echo "Y"" so that it would automatically start the text dump with out any additional user input. 
# grep -v "rubbish tells bash to ignore every instance of the workd rubbish in the text dump (which needed to be filterted out). 
# the flag would then be outputted 1 character per line so I used translate -d to delete all newline characters and spaces resulting in an output of just the flag on a single line
