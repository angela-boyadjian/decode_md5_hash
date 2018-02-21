#!usr/bin/env python3
import hashlib
import sys
import itertools

if (len(sys.argv) < 3):
	print("Not enough arguments")
	sys.exit()
def bruteforce(solution, nb):
	items = ["a", "b", "c", "d", "e", "f", "g", "h"
	"i", "j", "h", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
	"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	for p in itertools.permutations(items, nb):
		str = ''.join(p)
		hash_object = hashlib.md5(str.encode('utf-8'))
		if (hash_object.hexdigest() == solution):
			print('Password is: {0}'.format(str))
			break
bruteforce(sys.argv[1], int(sys.argv[2]))