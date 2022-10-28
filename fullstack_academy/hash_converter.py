"""
This is a bonus problem.
We intercepted traffic of a cybercriminal downloading malware onto a victim's computer. We have the network signature of the file, 
but we do not know where exactly this criminal copied the file. Based on logs, we know it is one of the files contained in this directory. 
The hash of the downloaded malware is 6859e1d10d08c1ea91f6e53ba6d601149b08d4efab8f8c2d586f6858ae1773a7. 
Find the file that matches this match. 
"""

"""
Incidently I was also able to solve this problem with just one line in bash
find -type f -exec sha256sum "{}" + > hash.chk | grep -e 6859e1d10d08c1ea91f6e53ba6d601149b08d4efab8f8c2d586f6858ae1773a7
"""
from os import listdir, getcwd
# imports functions for python to be able to interact with the operating system with
from os.path import isfile, join, normpath, basename
#imports modules for processing files in different placees in the system such as diving into a directory and retrieving file paths
import hashlib
# importating the ability for python to read and convert hashes


def get_files():
    # function to retrieve file paths
    current_path = normpath(getcwd())
    #sets the curretn working directory of the process to a varialbe called current path
    return [join(current_path, f) for f in listdir(current_path) if isfile(join(current_path, f))]
    # returns files in the current working directory


def get_hashes():
    #function for turning the files found with get files into hashes
    files = get_files()
    #setting the file paths returned in the get_files function as a variable called files
    list_of_hashes = []
    # empty list to store hashes of the files
    for each_file in files:
        # iterates through each file path
        hash_sha = hashlib.sha256()
        # sets sha256 hash library as a variable called hash_sah for later use
        with open(each_file, "rb") as f:
            #opens each file path iterated through from the files retrieved in the get_files function in binary format for reading as a variable "f"
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha.update(chunk)
                #iterates through python "chunks" and then hashes the files
        list_of_hashes.append('Filename: {}\tHash: {}\n'.format(basename(each_file), hash_sha.hexdigest()))
        #appends everything to a list that has the file name followed by the sha256 hash of it
    return list_of_hashes
    # returns the list of files and hashes to be used later


def write_hashes():
    #defines a functions to write the list of hashes to a file
    hashes = get_hashes()
    # sets the returned list_of hashes from get_hashes function as a variable "hashes"
    with open('list_of_hashes.txt', 'w') as f:
        # opens a file called list_of_hashes.txt, to be written over, as a variable called "f"
        for sha_hash in hashes:
            # itterates through the hash list
            f.write(sha_hash)
            # writes each item it finds in the above for loop to the file "list_of_hashes.txt" and saves it


if __name__ == '__main__':
    write_hashes()
    # calls the write_hashes function and starts the whole above script
