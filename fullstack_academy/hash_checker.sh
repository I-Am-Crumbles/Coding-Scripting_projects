"""
We intercepted traffic of a cybercriminal downloading malware onto a victim's computer. We have the network signature of the file, 
but we do not know where exactly this criminal copied the file. Based on logs, we know it is one of the files contained in this directory. 
The hash of the downloaded malware is 6859e1d10d08c1ea91f6e53ba6d601149b08d4efab8f8c2d586f6858ae1773a7. Find the file that matches this match.
"""

#!/bin/bash
find -type f -exec sha256sum "{}" + > hashlist.chk | grep -e 6859e1d10d08c1ea91f6e53ba6d601149b08d4efab8f8c2d586f6858ae1773a7
# searches the current working directory for files and then hashes them with sha256 then ouputs them to the terminal. 
#Since I was looking for a specific hash I piped grep into the command and told it to look for paterns that match the known hash
