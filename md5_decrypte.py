#!usr/bin/env python3
import hashlib
import sys
import itertools
import time

def bruteforce(solution, nb):
	items = ["a", "b", "c", "d", "e", "f", "g", "h"
	"i", "j", "h", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
	"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	for p in itertools.permutations(items, nb):
		str = ''.join(p)
		hash_object = hashlib.md5(str)
		if (hash_object.hexdigest() == solution):
			print(str)
			break
bruteforce(sys.argv[1], int(sys.argv[2]))