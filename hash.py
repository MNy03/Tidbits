#!python
# Just a small replacement for FCIV.exe from Microsoft because the lack of support for sha256.
# Usage:
# 	Option to create a bash script with content:
#   	@echo off
#   	py.exe filenameofthisscript.py %*

import os, hashlib, sys

def algorithmsAvailable():
	algos = ""
	for i in hashlib.algorithms_guaranteed:
		algos += i + " "
	return(algos)

usage = str('''
hash <file_to_calculate>
	will output  md5,sha1,sha256
hash sha1 <file_to_calculate>
	will output specified hash
hash sha1 <file_to_calculate> <checksum to check>
	will output specified hash and checksum.
hash -m <file1> <file2>
	will check if both files match using sha256
possible options:
''' + algorithmsAvailable())


def hashIt(fileName, algorithm='sha256'):
	BLOCKSIZE = 65536
	hasher = hashlib.new(algorithm)
	with open(fileName, 'rb') as afile:
	    buf = afile.read(BLOCKSIZE)
	    while len(buf) > 0:
	        hasher.update(buf)
	        buf = afile.read(BLOCKSIZE)
	if len(sys.argv) == 4:
		match = hasher.hexdigest() == sys.argv[3].lower()
		return('Checksum match: '+ str(match))
	else:
		return(hasher.hexdigest() + ' '*4 + algorithm + ' '*4 + fileName)


if len(sys.argv) == 1:
	print(usage)
elif sys.argv[1] == '-m':
	matchFiles = hashIt(sys.argv[2]) == hashIt(sys.argv[3])
	print(sys.argv[2] + ' == ' + sys.argv[3] + '\nmatch sha256: ' + str(matchFiles))
elif len(sys.argv) == 2:
	fileName = sys.argv[1]
	hashAlgorithm = ['md5','sha1','sha256']
	for i in hashAlgorithm:
		print(hashIt(fileName,i))
elif len(sys.argv) == 3 or 4:
	hashAlgorithm = sys.argv[1].lower()
	fileName = sys.argv[2]
	if hashAlgorithm in str(hashlib.algorithms_guaranteed):
		print(hashIt(fileName,hashAlgorithm))
	else:
		print(usage)
else:
	print(usage)
