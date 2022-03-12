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
from os.path import isfile, join, normpath, basename
import hashlib


def get_files():
    current_path = normpath(getcwd())
    return [join(current_path, f) for f in listdir(current_path) if isfile(join(current_path, f))]


def get_hashes():
    files = get_files()
    list_of_hashes = []
    for each_file in files:
        hash_sha = hashlib.sha256()
        with open(each_file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha.update(chunk)
        list_of_hashes.append('Filename: {}\tHash: {}\n'.format(basename(each_file), hash_sha.hexdigest()))
    return list_of_hashes


def write_hashes():
    hashes = get_hashes()
    with open('list_of_hashes.txt', 'w') as f:
        for sha_hash in hashes:
            f.write(sha_hash)


if __name__ == '__main__':
    write_hashes()
