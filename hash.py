#!python
'''
Just a small replacement for FCIV.exe from Microsoft because the lack of support for sha256.

Usage:
    Option to create a bash script with content:
      @echo off
      py.exe file_nameofthisscript.py %*
'''

import hashlib
import sys
import random

def random_algorithm():
    '''
    Just returns a random algorithm from the available ones in the library
    '''
    algo_list = [k for k in hashlib.algorithms_guaranteed]
    position = random.randrange(len(hashlib.algorithms_guaranteed))
    return algo_list[position]


def algorithms_available():
    '''
    Just queries the hashlib module for guaranteed algorithms, probably:
    sha384 shake_128 blake2b sha512 sha3_224 sha256 sha3_256
    shake_256 md5 blake2s sha3_384 sha1 sha224 sha3_512
    '''
    algos = ""
    for hashes in hashlib.algorithms_guaranteed:
        algos += hashes + " "
    return algos

USAGE = str('''
hash <file_to_calculate>
    will output  md5,sha1,sha256
hash <algorithm> <file1>
    will output specified hash based on algorithm e.g. {0}
hash <algorithm> <file1> <checksum to check>
    will output specified hash and checksum based on algorithm e.g. {0}
hash -m <file1> <file2>
    will check if both files match
algorithms available:
{1}
''').format(random_algorithm(), algorithms_available())

def hash_it(file_name, algorithm='sha256'):
    ''' Ingests the file and without extra options it generates the SHA256 hash'''
    block_size = 65536
    hasher = hashlib.new(algorithm)
    '''
    Available algorithms to be generated at "algorithms_available"
    '''
    with open(file_name, 'rb') as afile:
        buf = afile.read(block_size)
        while buf: #Fixed this, was while len(buf) > 0. Seems slower, would be weird, just check.
            hasher.update(buf)
            buf = afile.read(block_size)

    '''
    Here it expects a hash to compare. Make sure you add the right algorithm
    '''
    if len(sys.argv) == 4 and sys.argv[1] != '-m':
        match = hasher.hexdigest() == sys.argv[3].lower()
        match_response = 'Checksum match: '+ str(match)
    else:
        match_response = hasher.hexdigest() + ' '*4 + algorithm + ' '*4 + file_name
    return match_response


if len(sys.argv) == 1:
    '''
    Prints "usage"...
    '''
    print(USAGE)
elif sys.argv[1] == '-m':
    '''
    Compares 2 files using blake2b if you add the option "-m"
    '''
    HASH_ALGORITHM = 'blake2b'
    MATCH_FILES = hash_it(sys.argv[2], HASH_ALGORITHM) == hash_it(sys.argv[3], HASH_ALGORITHM)
    if MATCH_FILES is False:
        MATCH_FILES = " != "
    else:
        MATCH_FILES = " == "
    print(sys.argv[2] + MATCH_FILES + sys.argv[3] + str('''
                        \nchecked using {0} for performance
                        ''').format(HASH_ALGORITHM))
elif sys.argv[1] == '-r':
    '''
    Random hash from file, excl shake_128 & shake_256, not in USAGE
    '''
    ALGO = random_algorithm()
    while ALGO[:5] == 'shake':
        ALGO = random_algorithm()
    FILE_NAME = sys.argv[2]
    print(hash_it(FILE_NAME, ALGO))
elif len(sys.argv) == 2:
    '''
    Processes the file and returns hashes md5,sha1 & sha256
    '''
    FILE_NAME = sys.argv[1]
    HASH_ALGORITHM = ['md5', 'sha1', 'sha256']
    for i in HASH_ALGORITHM:
        print(hash_it(FILE_NAME, i))

elif len(sys.argv) == 3 or 4:
    '''
    Processes the file and depending on the extra option it processes it with a
    specified algorithm or tries to match it with a hashvalue
    '''
    HASH_ALGORITHM = sys.argv[1].lower()
    FILE_NAME = sys.argv[2]
    if HASH_ALGORITHM in str(hashlib.algorithms_guaranteed):
        print(hash_it(FILE_NAME, HASH_ALGORITHM))
    else:
        print(USAGE)
else:
    print(USAGE)
