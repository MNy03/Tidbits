#!python
# Just a small replacement for FCIV.exe from Microsoft because the lack of support for sha256.
# Usage:
# 		hash sha1 <file_to_calculate>
# 		hash sha1 <file_to_calculate> <checksum to check>
# 		only md5, sha1 or sha256
#

# Todo: Compare checksums automagically. perhaps as optional argv[3]
# 	Some issue in matching str(hasher.hexdigest()) and str(sys.argv[3].lower())
usage = str('''
hash <file_to_calculate>
	will output all hashes
hash sha1 <file_to_calculate>
	will output specified hash
hash sha1 <file_to_calculate> <checksum to check>
	will output specified hash and checksum.
only md5, sha1 or sha256
''')
import os, hashlib, sys

def hashit(fileName):
	BLOCKSIZE = 65536
	with open(fileName, 'rb') as afile:
	    buf = afile.read(BLOCKSIZE)
	    while len(buf) > 0:
	        hasher.update(buf)
	        buf = afile.read(BLOCKSIZE)
	print(hasher.hexdigest() + ' '*4 + hashAlgorithm + ' '*4 + fileName)
	if len(sys.argv) == 4:
		print(sys.argv[3].lower()+ ' '*4 + 'Checksum to check')
		if (hasher.hexdigest() == sys.argv[3].lower()) == True:
			print('Boys and girls, it\'s a match!')
		else:
			print('Nope, just nope..')


if len(sys.argv) == 1:
	print(usage)
elif len(sys.argv) == 2:
	fileName = sys.argv[1]
	hasher = hashlib.sha256()
	hashAlgorithm = 'sha256'
	hashit(fileName)
	hasher = hashlib.md5()
	hashAlgorithm = 'md5'
	hashit(fileName)
	hasher = hashlib.sha1()
	hashAlgorithm = 'sha1'
	hashit(fileName)
elif len(sys.argv) == 3 or 4:
	hashAlgorithm = sys.argv[1].lower()
	fileName = sys.argv[2]
	if hashAlgorithm == "sha256":
		hasher = hashlib.sha256()
		hashit(fileName)
	elif hashAlgorithm == "md5":
		hasher = hashlib.md5()
		hashit(fileName)
	elif hashAlgorithm == "sha1":
		hasher = hashlib.sha1()
		hashit(fileName)
	else:
		print(usage)
else:
	print(usage)
