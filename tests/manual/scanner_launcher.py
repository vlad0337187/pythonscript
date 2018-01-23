#! /usr/bin/python3


import os
import os.path
import sys
from scanner import tokenize


scanner_test_code = """
import os


b = [1, 2, 3, 4, 5]
'some_string'

for x in b:
	print(x)
	print (x)

switch b
	when list 1, 2, 3, 4, 5
		print 'some string'
	else
		print 'not found'
"""


if __name__ == '__main__':
	cur_dir = os.path.dirname (__file__)

    scanner_dir = os.path.join (cur_dir, '../../scanner')
    sys.path.append (scanner_dir)

	tokens = tokenize(scanner_test_code)
	for i in tokens:
		print (i.name, i.text)
