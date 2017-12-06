#! /usr/bin/python3


import os
import os.path
from scanner import tokenize


if __name__ == '__main__':
	cur_dir = os.path.dirname (__file__)
	scanner_test_file_path = os.path.join (cur_dir, './scanner_test.python')
	scanner_test_file = open(scanner_test_file_path, 'tr')
	source_code = scanner_test_file.read()
	tokens = tokenize(source_code)
	for i in tokens:
		print (i.name, i.text)
