#!python
# Just a small replacement for FCIV.exe from Microsoft because the lack of support for sha256.
# Usage:
# 		hash sha1 <file_to_calculate>
# 		hash sha1 <file_to_calculate> <checksum to check>
# 		only md5, sha1 or sha256
#
# TODO: Something with a line up of the default.
import os, hashlib, sys

def algo():
	algos = ""
	for i in hashlib.algorithms_guaranteed:
		algos += i + " "
	return(algos)

usage = str('''
hash <file_to_calculate>
	will output md5, sha1 & sha256 for the file.
hash sha1 <file_to_calculate>
	will output specified hash
hash sha1 <file_to_calculate> <checksum to check>
	will output specified hash and checksum.
possible options:
''' + algo())


def hashit(fileName, algorithm):
	BLOCKSIZE = 65536
	hasher = hashlib.new(algorithm)
	with open(fileName, 'rb') as afile:
	    buf = afile.read(BLOCKSIZE)
	    while len(buf) > 0:
	        hasher.update(buf)
	        buf = afile.read(BLOCKSIZE)
	print(hasher.hexdigest() + ' '*4 + algorithm + ' '*4 + fileName)
	if len(sys.argv) == 4:
		print(sys.argv[3].lower()+ ' '*4 + 'Checksum to check')
		print('Match?: '+ hasher.hexdigest() == sys.argv[3].lower())


if len(sys.argv) == 1:
	print(usage)
elif len(sys.argv) == 2:
	fileName = sys.argv[1]
	hashit(fileName,'md5')
	hashit(fileName,'sha1')
	hashit(fileName,'sha256')
	print(usage)
elif len(sys.argv) == 3 or 4:
	hashAlgorithm = sys.argv[1].lower()
	fileName = sys.argv[2]
	if hashAlgorithm in str(hashlib.algorithms_guaranteed):
		hashit(fileName,hashAlgorithm)
	else:
		print(usage)
else:
	print(usage)

