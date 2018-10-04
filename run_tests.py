#! /usr/bin/env python

import os, os.path
from os.path import join, abspath
import pytest


files_dir = os.path.dirname(__file__)
if files_dir.startswith('.'):  # is relative
    cwd = os.getcwd()
    files_dir = abspath(join(cwd, files_dir))

os.chdir(files_dir)


pythonscript_dir = files_dir
os.environ['PYTHONSCRIPT_DIR'] = pythonscript_dir


rel_parser_dir = './tests/automatic/parser/'
abs_parser_dir = abspath(join(files_dir, rel_parser_dir))

pytest.main([abs_parser_dir, '--verbose'])
