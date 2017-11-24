#! /usr/bin/python3


import os
import os.path
from scanner import generate_tokens


if __name__ == '__main__':
	cur_dir = os.path.dirname (__file__)
	scanner_test_file_path = os.path.join (cur_dir, './scanner_test.python')
	scanner_test_file = open(scanner_test_file_path, 'tr')
	source_code_example = scanner_test_file.readline
	tokens = generate_tokens(source_code_example)
	for i in tokens:
		print (i)
